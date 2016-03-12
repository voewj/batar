# -*- coding: utf-8 -*-

from openerp.osv import fields,osv

class res_country_state_city(osv.Model):
    _name = 'res.country.state.city'
    _columns ={
        'name':fields.char(size=50,string='city name'),
        'province_id': fields.many2one('res.country.state',ondelete='cascade',string='province name'),
        'district_ids':fields.one2many('res.country.state.city.district','city_id',string='districts belong to one city')
    }

class res_country_state_city_district(osv.Model):
    _name = 'res.country.state.city.district'
    _columns = {
       'name': fields.char(size=100,string='district name'),
       'city_id': fields.many2one('res.country.state.city',ondelete='cascade',string='city name'),
       'province_id':fields.related('city_id','province_id',type='many2one',relation='res.country.state',string='province name')
    }

class res_country_state(osv.Model):
    _inherit = 'res.country.state'
    _columns = {
        'city_ids':fields.one2many('res.country.state.city','province_id',string='citys belong to one state')
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: