{
    'name': 'School Lesson 6.1',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Module for managing library books and categories',
    'description': """
        School Lesson 6.1
        =================
        This module allows the management of library books and their categories.

        Key Features:
        -------------
        * Create and manage book records
        * Categorize books into different categories
        * Assign readers to books
        * Track checkout and return dates
        * Manage user access rights for books and categories
    """,
    'author': 'Dmitriy Chumak',
    'website': 'https://www.example.com',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'data/library_book_category_data.xml',
        'views/library_book_views.xml',
        'views/library_book_category_views.xml',
        'views/library_menu.xml',
    ],
    'demo': [
        'demo/library_book_demo.xml',
        'demo/library_book_update_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
