# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Circle(models.Model):
    _name = 'circle'

    name = fields.Char(
        string='Name',
    )
