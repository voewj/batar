# -*- coding: utf-8 -*-


from openerp import api, fields,models,_
from ..utils import deliveryExcelAction
from openerp.exceptions import UserError
 
class delivery_bill_import(models.TransientModel):
    _name = 'delivery.bill.import'
    
#     _columns = {
#         'file': fields.binary('excel File',help='order info file',filter='*.xls|*.csv'),
#     }
#     
    file = fields.Binary(string='delivery bill import file')
    line = fields.Integer(string='line start',default=8)
    @api.multi
    def apply(self):
        '''导入文件'''
       
        exceObj = deliveryExcelAction.deliveryExcelFile(file_contents=self.file,line=self.line)
        data_dict = exceObj.readFile()
        
        if data_dict is None:
            raise UserError(_("Import failed,The excel file some data is not support")) 
        #数据处理
        values = {}
        values['purchase_number'] = data_dict['purchase_number']
        values['charge_man'] = self.env.uid
        purchase_obj = self.env['purchase.order'].search([('name','=',values['purchase_number'])])
        if purchase_obj:
            values['purchase_id'] = purchase_obj.id
        values['partner_person']=data_dict['partner_person']
        values['partner_mobile'] = data_dict['partner_mobile']
        values['delivery_method'] = data_dict.get('delivery_method','')
        values['delivery_man'] = data_dict.get('delivery_man','')
        values['delivery_mobile'] = data_dict['delivery_mobile']
        data_lines = data_dict['data']
        pkg_line = []
        for line in data_lines:
            
            value_lines = {
                'pkg_number':line.get(u'包号',''),
                'supplier_code':line.get(u'供应商编号',''),
                'default_code':line.get(u'尚金缘编码',''),
                'product_qty':line.get(u'件数',0),
                'net_weight':line.get(u'净重',0),
                'gross_weight':line.get(u'毛重',0)  
            }
            product_obj = self.env['product.product'].search([('default_code','=',line.get('default',None))])
            if product_obj:
                value_lines['product_id'] = product_obj.id
            pkg_line.append((0,0,value_lines))
        
        values['line_id'] = pkg_line
        obj = self.env['delivery.bill'].create(values)
        id =None or obj.id
         
            
        return {
                'name': _('Delivery Bill Import Result'),
                'view_type': 'form',
                "view_mode": 'tree,form',
                'res_model': 'delivery.bill',
                "domain": [('id', '=', id)],
                'type': 'ir.actions.act_window',
            }
                    
                
            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:      