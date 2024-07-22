{
    'name': 'School Lesson 6-2',
    'version': '1.0',
    'summary': 'Module for school lesson 6-2',
    'category': 'Extra Tools',
    'author': 'Dmitriy Chumak',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'school_lesson_6_1',
    ],
    'data': [
        'security/groups.xml',

        'security/ir.model.access.csv',  # Access rights

        'views/library_author_views.xml',
        'views/library_author_menu.xml',
        'views/library_book_views.xml',

        'data/library_author_data.xml',
    ],

    'i18n': [

    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
