from odoo import models, fields, api


class PersonalDoctor(models.TransientModel):
    _name = 'hr_hospital.personal.doctor.wizard'
    _description = 'Personal Doctor Wizard'

    name = fields.Char(string='Name')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='New Personal Doctor', required=True)
    patient_ids = fields.Many2many('hr_hospital.patient', string='Patients', relation='patient_personal_doctor_rel')

    def assign_personal_doctor(self):
        for wizard in self:
            for patient in wizard.patient_ids:
                patient.personal_doctor_id = wizard.doctor_id
