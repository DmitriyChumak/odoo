{
    'name': 'School Lesson 6-2',
    'version': '1.0',
    'summary': 'Module for school lesson 6-2',
    'category': 'Extra Tools',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'school_lesson_6_1'
    ],
    'data': [
        'security/security.xml',  # Security groups and access rules
        'security/ir.model.access.csv',  # Access rights
        'data/ir_rule.xml',  # Record rules
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
