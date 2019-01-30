# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Role(models.Model):
    _name = 'role'

    name = fields.Char(
        string='Name',
    )

    circle_id = fields.Many2one(
        string='Assigned Circle',
        comodel_name='circle',
    )

    person_id = fields.Many2one(
        string='Assigned Person',
        comodel_name='res.users',
    )

    # todo constraint: either circle or res_users