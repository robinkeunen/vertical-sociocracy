# -*- coding: utf-8 -*-
from openerp import api, fields, models


class ResUsers(models.Model):

    _inherit = 'res.users'
    _inherits = ['assignee']
