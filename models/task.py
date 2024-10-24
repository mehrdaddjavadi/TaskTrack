from odoo import models, fields, api

class Task(models.Model):
    _name = 'project.task'
    _description = 'Task Management'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    state = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default='new')
    project_id = fields.Many2one('project.management', string='Project')
    assigned_employee_id = fields.Many2one('hr.employee', string='Assigned Employee')
    dependent_task_id = fields.Many2one('project.task', string='Dependent Task')

    # Prevent marking a task as done if dependent task is not done
    @api.constrains('state', 'dependent_task_id')
    def _check_dependent_task_done(self):
        for task in self:
            if task.dependent_task_id and task.state == 'done' and task.dependent_task_id.state != 'done':
                raise models.ValidationError('You cannot complete this task until the dependent task is done.')
