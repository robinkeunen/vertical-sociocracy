# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Circle(models.Model):
    _name = 'shared.gouvernance.circle'

    name = fields.Char(
        string='Name',
    )
    mandate_id = fields.Many2one(
        comodel_name='shared.gouvenance.mandate',
        string='Mandate')
