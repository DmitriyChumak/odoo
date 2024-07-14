# doctor model

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Hospital Doctors'

    specialization_id = fields.Many2one(
        comodel_name='hr_hospital.specialization',
        string='Specialization'
    )

    is_intern = fields.Boolean(
        string='Is Intern',
        default=False
    )

    mentor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Mentor',
        domain="[('is_intern', '=', False)]",
        help="This diagnosis, made by the doctor-intern, has been reviewed and approved by their mentor.",
        readonly=True if not is_intern else False
    )

    personal_doctor_patient_ids = fields.One2many(
        comodel_name='hr_hospital.patient',
        inverse_name='personal_doctor_id',
        string='Personal Patients'
    )

    supervised_doctor_patient_ids = fields.One2many(
        comodel_name='hr_hospital.patient',
        inverse_name='supervised_doctor_id',
        string='Supervised Patients'
    )



    @api.constrains('mentor_id')
    def _check_mentor(self):
        for record in self:
            if record.mentor_id and record.mentor_id.is_intern:
                raise ValidationError("An intern cannot be assigned as a mentor.")

    # def name_get(self):
    #     result = []
    #     for doctor in self:
    #         name = f"{doctor.first_name} {doctor.last_name}"
    #         result.append((doctor.id, name))
    #     return result

    def write(self, vals):
        if 'is_intern' in vals and not vals.get('is_intern'):
            vals['is_intern'] = False
        return super(Doctor, self).write(vals)