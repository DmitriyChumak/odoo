{
    'name': 'School Lesson 6-1',
    'version': '1.0',
    'summary': 'Module for school lesson 6-1',
    'category': 'Extra Tools',
    'author': 'Dmitriy Chumak',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [

        'data/library_module_category.xml',

        'security/library_security.xml',
        'security/ir.model.access.csv',  # Access rights

        'data/library_book_category_data.xml',  # Master data
        'data/library_book_update.xml',

        'views/library_book_views.xml',
        'views/library_book_category_views.xml',
        'views/library_book_menus.xml',  # Menus
    ],

    'demo': [
        'demo/library_book_demo.xml',  # Demo data
    ],


    'application': False,
    'installable': True,
    'auto_install': False,
}
