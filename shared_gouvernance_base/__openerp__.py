# -*- coding: utf-8 -*-
#
#  Copyright (C) 2019  Coop IT Easy SCRLfs. <http://www.coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shared Gouvernance Base",
    "version": "1.0",
    "depends": ["base",
                'mail',],
    "author": "Coop IT Easy SCRLfs",
    "category": "Cooperative management",
    "website": "www.coopiteasy.be",
    "license": "AGPL-3",
    "description": """
    
    """,
    'data': [
        'security/shared_gouvernance_security.xml',
#        'security/ir.model.access.csv',
        'views/sociocracy_menu.xml',
        'views/mandate.xml',
        'views/circle.xml',
    ],
    'installable': True,
    'application': True,
}
