# person model

from odoo import models, fields, api

class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Person'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    birthdate = fields.Date(string='Birthdate')
    phone = fields.Char(string='Phone')
    photo = fields.Binary(string='Photo')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')

    name = fields.Char(
        string='Name',
        compute='_compute_names',
        store=True
    )

    @api.depends('first_name', 'last_name')
    def _compute_names(self):
        for record in self:
            if record.first_name and record.last_name:
                record.name = f'{record.first_name} {record.last_name}'.strip()
            else:
                record.name = "Unnamed Person"