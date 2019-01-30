# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Assignee(models.Model):
    _name = 'assignee'

    name = fields.Char(
        string='Name',
    )
