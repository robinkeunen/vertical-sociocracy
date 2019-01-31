# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Circle(models.Model):
    _name = 'shared.governance.circle'

    name = fields.Char(
        string='Name',
    )
    mandate_id = fields.Many2one(
        comodel_name='shared.governance.mandate',
        string='Mandate')
    state = fields.Selection(
        related='mandate_id.state',
        string='State')
    parent_circle_id = fields.Many2one(
        comodel_name='shared.governance.circle',
        string='Parent circle')
    childs_circle = fields.One2many(
        'shared.governance.mandate',
        'parent_circle_id',
        string='Mandate')
    members = fields.Many2many(
        comodel_name='res.users',
        string='Members')
