# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Mandate(models.Model):
    _name = 'shared.gouvenance.mandate'

    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    name = fields.Char(
        string='Name',
    )

    circle_id = fields.One2many(
        'shared.gouvenance.circle',
        'mandate_id',
        string='Assigned Circle',
    )

    person_id = fields.Many2one(
        string='Assigned Person',
        comodel_name='res.users',
    )

    state = fields.Selection(
        [('draft','Draft'),
         ('alive','Alive'),
         ('rip','Rest in peace')],
        string='State',
        default='draft')
    # todo constraint: either circle or res_users