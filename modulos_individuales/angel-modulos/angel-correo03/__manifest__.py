# -*- coding: utf-8 -*-
#encargggggggggado de informacion del modulo
{
    'name': "angel-correov001",

    'summary': """
        Modulo encargado de enviar correos a los clientes segun su preferencia""",

    'description': """
        Este modulo se centra en permitir al administrador enviar un modulo a los grupos de personas que hayan permitido recibir contenido promocional
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vista01.xml',
    ],
    'installable': True,
    'application': True,
}
