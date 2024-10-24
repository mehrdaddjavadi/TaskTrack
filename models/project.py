from odoo import models, fields, api

class Project(models.Model):
    _name = 'project.management'
    _description = 'Project Management'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    task_ids = fields.One2many('project.task', 'project_id', string='Tasks')
    employee_ids = fields.Many2many('hr.employee', string='Assigned Employees')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Project name must be unique.')
    ]

    # Auto-generate end date based on task deadlines (optional)
    @api.depends('task_ids.deadline')
    def _compute_end_date(self):
        for record in self:
            if record.task_ids:
                record.end_date = max(record.task_ids.mapped('deadline'))
