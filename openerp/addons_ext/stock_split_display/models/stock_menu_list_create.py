# -*- coding: utf-8 -*-
'''
Created on 2016年3月11日

@author: cloudy
'''

from openerp import fields,models,api


class ir_actions_act_window(models.Model):
    _inherit= 'ir.actions.act_window'
   
    stock_action_code = fields.Char(string='stock action code',readonly=True)

class ir_ui_menu(models.Model):
    _inherit='ir.ui.menu'
    stock_menu_code = fields.Char(string='stock menu code')

class stock_warehouse(models.Model):
    _inherit = "stock.warehouse"
    act_window_id = fields.Integer(string='ir actions act_window ID')
    
class stock_menu_list_create(models.Model):
    _name = 'stock.menu.list.create'
    
    warehouse_id = fields.Many2one('stock.warehouse',string='stock warehouse')
    en_code = fields.Char(related='warehouse_id.en_code',string='stock warehouse english code')
    act_window_id = fields.Many2one('ir.actions.act_window',string='ir actions act_window')
    menuitem_id = fields.Many2one('ir.ui.menu',string='ir ui menu')
    domain = fields.Text(string='domain',default='')
    groups = fields.Many2many('res.groups',string="access control")
    
    @api.multi
    @api.depends('warehouse_id')
    def name_get(self):
        result = []
        for line in self:
            name = "%s" % (line.warehouse_id.name)
            result.append((line.id,name))
        return result
    @api.multi
    def action_auto_delete_warehouse_list(self):
        ''''''
        list = self.search([()])
        print list
    @api.multi
    def action_auto_create_warehouse_list(self):
        ''''''
        parent_id = self.env['ir.model.data'].get_object_reference('stock','menu_stock_inventory_control')[1]
        stock_warehouse_list = self.env['stock.warehouse'].sudo().search([])
        
        for stock_warehouse in stock_warehouse_list:
            
            menu_list = self.search([('warehouse_id','=',stock_warehouse.id)])
            obj = None
            if not menu_list:
                obj = self.create({'warehouse_id':stock_warehouse.id})
            else:
                obj = menu_list[0]
                
            
            en_code = stock_warehouse.en_code
           
            domain = obj.domain
            groups = obj.groups
            if not domain:
                domain= "[('en_code','=','%s')]" % en_code
            action_values ={
                'stock_action_code':en_code,
                'name':stock_warehouse.code,
                'type':"ir.actions.act_window",
                'res_model':'stock.move.detail',
                'view_type':'form',
                'view_mode':"tree,form",
                'domain':domain,
            }
            act_window_id = obj.act_window_id
            
            
            if act_window_id:
                obj.act_window_id.write(action_values)
                act_window_id = act_window_id.id
            else:
                action_obj = self.env['ir.actions.act_window'].sudo().create(action_values)
                act_window_id = action_obj.id
            menu_values = {
                'name':"%s:%s" % (stock_warehouse.code,u'库存明细'), 
            }
            if groups:
                menu_values['groups_id']= [group.id for group in groups]
            if parent_id and act_window_id:
                menu_values['parent_id'] = parent_id
                menu_values['action'] ="ir.actions.act_window,%s" % act_window_id 
                menuitem_id = obj.menuitem_id
                
                if menuitem_id:
                    obj.menuitem_id.write(menu_values)
                    menuitem_id = obj.menuitem_id.id
                else:
                    menuitem_id= self.env['ir.ui.menu'].sudo().create(menu_values)
                    menuitem_id = menuitem_id.id
                values ={
                    'act_window_id':act_window_id,
                    'menuitem_id':menuitem_id,
                    'domain':domain,
                }
                
                obj.write(values)
            
    
