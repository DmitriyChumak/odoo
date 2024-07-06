# visit model

from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _

class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'


    state = fields.Selection(
        selection=[
        ('planned', 'Planned'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ],
        string='Status',
        default='planned'
    )

    planned_date_time = fields.Datetime(
        string='Planned Date & Time'
    )

    actual_date_time = fields.Datetime(
        string='Actual Date & Time'
    )

    doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Doctor',
        required=True
    )

    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string='Patient',
        required=True
    )

    diagnosis_ids = fields.One2many(
        comodel_name='hr_hospital.diagnosis',
        inverse_name='visit_id',
        string='Diagnoses'
    )

    symptoms = fields.Text(string='Symptoms')
    notes = fields.Text(string='Notes')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'completed':
            self.actual_date_time = fields.Datetime.now()
            self.planned_date_time = self.actual_date_time
            self.doctor_id = self.doctor_id

    @api.constrains('patient_id', 'doctor_id', 'planned_date_time')
    def _check_unique_patient_doctor_date(self):
        for rec in self:
            if rec.planned_date_time:
                overlapping_visits = self.search([
                    ('doctor_id', '=', rec.doctor_id.id),
                    ('patient_id', '=', rec.patient_id.id),
                    ('planned_date_time', '>=', rec.planned_date_time.date()),
                    ('planned_date_time', '<', rec.planned_date_time.date() + timedelta(days=1)),
                    ('id', '!=', rec.id)
                ])
                if overlapping_visits:
                    raise ValidationError("The doctor already has an appointment with this patient on the same date.")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_with_diagnosis(self):
        for visit in self:
            if visit.diagnosis_ids:
                raise UserError(_(
                    "You cannot delete a visit that has diagnoses associated with it."
                ))

    @api.model
    def create(self, vals):
        if 'actual_date_time' in vals:
            try:
                vals['actual_date_time'] = datetime.strptime(vals['actual_date_time'], '%d-%m-%Y %H:%M:%S').strftime(
                    '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValidationError("Incorrect date format, should be DD-MM-YYYY HH:MM:SS")
        if 'planned_date_time' in vals:
            try:
                vals['planned_date_time'] = datetime.strptime(vals['planned_date_time'], '%d-%m-%Y %H:%M:%S').strftime(
                    '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValidationError("Incorrect date format, should be DD-MM-YYYY HH:MM:SS")
        return super(Visit, self).create(vals)

    def write(self, vals):
        if 'actual_date_time' in vals:
            try:
                vals['actual_date_time'] = datetime.strptime(vals['actual_date_time'], '%d-%m-%Y %H:%M:%S').strftime(
                    '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValidationError("Incorrect date format, should be DD-MM-YYYY HH:MM:SS")
        if 'planned_date_time' in vals:
            try:
                vals['planned_date_time'] = datetime.strptime(vals['planned_date_time'], '%d-%m-%Y %H:%M:%S').strftime(
                    '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValidationError("Incorrect date format, should be DD-MM-YYYY HH:MM:SS")
        return super(Visit, self).write(vals)