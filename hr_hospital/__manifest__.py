{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Module for managing hospital operations',
    'author': 'Dmitriy',
    'website': 'http://www.example.com',
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [

        'security/ir.model.access.csv',
        'data/disease_data.xml',

        'views/diagnosis_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/specialization_views.xml',

        'views/hospital_menu.xml',

        'wizard/disease_report_wizard_views.xml',
        'wizard/personal_doctor_views.xml',
    ],
    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
        'demo/visit_demo.xml',
    ],
    'installable': True,
    'application': True,
}
