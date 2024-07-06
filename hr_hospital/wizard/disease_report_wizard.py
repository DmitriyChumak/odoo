from odoo import models, fields


class DiseaseReportWizard(models.TransientModel):
    _name = 'hr_hospital.disease.report.wizard'
    _description = 'Disease Report Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    doctor_ids = fields.Many2many('hr_hospital.doctor', string='Doctors')
    disease_ids = fields.Many2many('hr_hospital.disease', string='Diseases')

    def generate_report(self):
        domain = [('visit_id.planned_date_time', '>=', self.start_date),
                  ('visit_id.planned_date_time', '<=', self.end_date)]
        if self.doctor_ids:
            domain.append(('visit_id.doctor_id', 'in', self.doctor_ids.ids))
        if self.disease_ids:
            domain.append(('disease_id', 'in', self.disease_ids.ids))

        diagnoses = self.env['hr_hospital.diagnosis'].search(domain)
        # Code to generate report from diagnoses
