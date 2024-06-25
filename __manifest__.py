# -*- encoding: utf-8 -*-
{
    'name': 'Odoo Sample Module',
    'description': 'Módulo de exemplo do Odoo.',
    'summary': '',
    'category': 'Sample',
    'version': '17.0.0.0',
    'author': "Eduardo Luiz",
    'website': '',
    'company': 'e-Masters Tecnologia',
    'maintainer': 'e-Masters Tecnologia',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail'
    ],
    'data': [
        # 'data/sample_data.xml',
        # 'security/ir.rules.access.xml',
        'security/ir.model.access.csv',
        'views/sample_view.xml',
        'views/get_started_view.xml',
        'views/metodo_pagamento_view.xml',
        'views/app.xml',
    ],
    'assets': {},
    'qweb': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
