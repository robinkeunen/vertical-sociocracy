# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Role(models.Model):
    _name = 'role'

    name = fields.Char(
        string='Name',
    )

    assignee_id = fields.Many2one(
        string='Assignee',
        comodel_name='assignee',
    )
