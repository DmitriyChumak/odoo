# diagnosis model

from odoo import models, fields, api


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(
        string='Name',
        required=True
    )

    visit_id = fields.Many2one(
        comodel_name='hr_hospital.visit',
        string='Visit',
        required=False
    )

    disease_id = fields.Many2one(
        comodel_name='hr_hospital.disease',
        string='Disease',
        required=True
    )

    description = fields.Text(
        string='Description (Treatment)'
    )

    approved = fields.Boolean(
        string='Approved',
        default=False
    )

    mentor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Mentor',
        domain="[('is_intern', '=', False)]",
        help="This diagnosis, made by the doctor-intern, has been reviewed and approved by their mentor."
    )

    doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Assigned Doctor',
        required=True
    )

    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string='Patient',
        required=True
    )

    @api.model
    def create(self, vals):
        if vals.get('visit_id'):
            visit = self.env['hr_hospital.visit'].browse(vals['visit_id'])
            vals['doctor_id'] = visit.doctor_id.id
            vals['patient_id'] = visit.patient_id.id
        return super(Diagnosis, self).create(vals)