from odoo import models, fields, api

class EmployeeEvaluation(models.Model):
    _name = 'employee.evaluation'
    _description = 'Employee Performance Evaluation'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    project_id = fields.Many2one('project.management', string='Project', required=True)
    task_ids = fields.One2many('project.task', 'assigned_employee_id', string='Tasks')
    performance_score = fields.Float(string='Performance Score', compute='_compute_performance_score')
    speed_score = fields.Float(string='Speed Score', compute='_compute_speed_score')
    quality_score = fields.Float(string='Quality Score')
    manager_feedback = fields.Text(string='Manager Feedback')

    # Compute performance score based on completed tasks
    @api.depends('task_ids')
    def _compute_performance_score(self):
        for record in self:
            completed_tasks = self.env['project.task'].search_count([
                ('assigned_employee_id', '=', record.employee_id.id),
                ('state', '=', 'done')
            ])
            total_tasks = self.env['project.task'].search_count([
                ('assigned_employee_id', '=', record.employee_id.id)
            ])
            record.performance_score = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Calculate speed score based on task deadlines
    @api.depends('task_ids.deadline')
    def _compute_speed_score(self):
        for record in self:
            timely_tasks = self.env['project.task'].search_count([
                ('assigned_employee_id', '=', record.employee_id.id),
                ('state', '=', 'done'),
                ('deadline', '>=', fields.Date.today())
            ])
            total_tasks = self.env['project.task'].search_count([
                ('assigned_employee_id', '=', record.employee_id.id)
            ])
            record.speed_score = (timely_tasks / total_tasks) * 100 if total_tasks > 0 else 0
