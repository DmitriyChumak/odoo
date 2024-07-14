# patient model

from odoo import models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _inherit = 'hr_hospital.person'
    _description = 'Hospital Patients'

    personal_doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Personal Doctor'
    )

    supervised_doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Supervised Doctor'
    )

    disease_ids = fields.Many2many(
        comodel_name='hr_hospital.disease',
        string='Diseases'
    )

    visit_ids = fields.One2many(
        comodel_name='hr_hospital.visit',
        inverse_name='patient_id',
        string='Visits'
    )

    passport_info = fields.Char(
        string='Passport Information'
    )

    contact_person = fields.Char(
        string='Contact Person'
    )

    # def name_get(self):
    #     result = []
    #     for patient in self:
    #         name = f"{patient.first_name} {patient.last_name}"
    #         result.append((patient.id, name))
    #     return result
