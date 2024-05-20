{
    'name': 'inventarioM10',
    'version': '1.0',
    'summary': 'Gestión de Inventario para productos',
    'sequence': 10,
    'description': "Gestión de inventarios de productos.",
    'category': 'Inventory',
    'author': 'Tu Nombre',
    'website': 'https://www.tuempresa.com',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'data/model_product_data.xml',
        'security/ir.model.access.csv',
        'views/producto_views.xml',
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
