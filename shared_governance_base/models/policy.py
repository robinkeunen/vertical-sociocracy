# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Policy(models.Model):
    _name = 'shared.governance.policy'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Name',
        required=True,
    )
    circles = fields.One2many(
        comodel_name='shared.governance.circle',
        inverse_name='policy_id',
        string='Circles',
    )
    policy = fields.Html(
        string='Policy',
    )
    # attachment_ids = fields.One2many(
    #     'ir.attachment',
    #     'res_id',
    #     domain=[('res_model', '=', 'shared.governance.policy')],
    #     string='Attachments',
    # )
