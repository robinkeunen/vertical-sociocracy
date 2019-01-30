# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Circle(models.Model):
    _name = 'circle'
    _inherits = ['assignee']

    name = fields.Char(
        string='Name',
    )
