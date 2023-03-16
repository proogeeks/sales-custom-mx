{
    'name': "Sales Custom",

    'summary': """""",
    'author': "ProoGeeks",
    'website': "http://proogeeks.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Sales',
    'version': '16.0.0.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "data/ir_cron.xml",
        "data/mail_template.xml",
        "views/sale_order.xml",
    ]
}
