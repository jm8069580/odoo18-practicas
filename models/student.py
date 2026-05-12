from odoo import models, fields

class Student(models.Model):
    _name = 'practice.student'
    _description = 'Estudiante'

    name = fields.Char(string='Nombre completo', required=True)
    age = fields.Integer(string='Edad', help='Edad cronológica del estudiante')
    email = fields.Char(string='Correo electrónico')
    enrollment_date = fields.Date(string='Fecha de inscripción', default=fields.Date.today)
    active = fields.Boolean(string='Activo', default=True)
    notes = fields.Text(string='Notas')
