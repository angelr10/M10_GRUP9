{
    'name': 'empleadosM10',
    'version': '1.0',
    'summary': 'Módulo para gestionar información de empleados',
    'sequence': 10,
    'description': """Este módulo permite gestionar información de empleados, incluyendo datos personales, información de contacto y detalles de empleo.""",
    'category': 'Empleados',
    'author': 'Aleix',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/empleado_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

