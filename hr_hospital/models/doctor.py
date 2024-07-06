# doctor model

from odoo import models, fields, api


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Doctor'

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

    @api.onchange('is_intern')
    def _onchange_is_intern(self):
        if not self.is_intern:
            self.mentor_id = False

    @api.constrains('mentor_id')
    def _check_mentor(self):
        for record in self:
            if record.mentor_id and record.mentor_id.is_intern:
                raise ValidationError("An intern cannot be assigned as a mentor.")

