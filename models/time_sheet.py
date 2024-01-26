from odoo import models, fields, api

class TimeSheet(models.Model):
    _name = "task.time.sheet"

    # time_sheet_id = fields.Many2one("patients.details",string='Patient Name')
    task_id = fields.Many2one("todo.tasks", string='Task name')
    task_time = fields.Date(string='Task time')
    description = fields.Text(string='Description')
    hours = fields.Float(string='Hours Spent')

