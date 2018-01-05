# -*- coding: utf-8 -*-
{
    'name': "CCRM",

    'summary': """
        This module is usefull to Trainig and Placement Officer(TPO) as  well  as  Student.Both user can use this Software very easily.""",

    'description': """
        This Module is for Gujarat Power Engineering and Research Institute.
    """,

    'author': "Jinal , Riya and Vidhi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
	'views/company_view.xml',
    ],
    # only loaded in demonstration mode
#    'demo': [
#       'demo/demo.xml',
#    ],
}
