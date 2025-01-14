{
    'name': "estate",
    'depends': ['mail', 'base'],
    'author': "sndibwami@virunga.org",
    'license': "AGPL-3",
    'summary': "Real Estate Management",
    'application': True,
    'installable': True,
    'demo': [
        'demo/demo.xml',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_tags_views.xml',
        'views/res_users_views.xml',
        'views/estate_menus.xml',
    ],
}
