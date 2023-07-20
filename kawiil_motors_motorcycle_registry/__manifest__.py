{
    'name' : 'Motorcycle Registry',
    'summary' : 'Manage Registration of Motorcycles',
    'description' : """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'license' : 'OPL-1',
    'author' : 'levm-odoo',
    'website' : 'https://www.github.com/levm-odoo',
    'category' : 'Kawiil',
    'depends' : ['base'],
    'data' : [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'security/registry_security.xml',
        'data/registry_data.xml',
        'views/registry_menuitems.xml',
        'views/registred_motorcycles_views.xml'
    ],
    'demo' : [
        'demo/registries_demo.xml'
    ],
    'application' : True,
}