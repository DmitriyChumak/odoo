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
        'data/hr_hospital_disease_data.xml',



        'views/diagnosis_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/specialization_views.xml',

        'views/hospital_actions.xml',

        'views/hospital_menu.xml',


        'wizard/disease_report_wizard_views.xml',
        'wizard/personal_doctor_views.xml',
    ],
    'demo': [
        'demo/hr_hospital_doctor_demo.xml',
        'demo/hr_hospital_patient_demo.xml',
        'demo/hr_hospital_visit_demo.xml',
    ],
    'installable': True,
    'application': True,
}
