# -*- coding: utf-8 -*-

from openerp.osv import fields,osv

class res_country_state_city(osv.Model):
    _name = 'res.country.state.city'
    _columns ={
        'name':fields.char(size=50,string='city name'),
        'province_id': fields.many2one('res.country.state',ondelete='cascade',string='province name'),
    }

class res_country_state_city_district(osv.Model):
    _name = 'res.country.state.city.district'
    _columns = {
       'name': fields.char(size=100,string='district name'),
       'city_id': fields.many2one('res.country.state.city',ondelete='cascade',string='city name'),
       'province_id':fields.related('city_id','province_id',type='many2one',relation='res.country.state',string='province name')
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: