from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class TodoTasks(models.Model):
    _name = "todo.tasks"
    _description = "Todo Task"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Task Name',required=True)
    assign_to = fields.Many2one('res.partner', string="Assign to", required=True,tracking=1)
    description = fields.Text(String='Description')
    due_date = fields.Date(String='Due Date',required=True,tracking=1)
    status = fields.Selection(
        [('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed'),('closed', 'Closed')],
        default='new',
        string="Status")
    time_sheet = fields.One2many("task.time.sheet", "task_id", string="Time Sheet")
    estimated_time = fields.Float(string="Estimated Time")
    is_late = fields.Boolean()
    active = fields.Boolean(default=True)
    total_hours = fields.Float(string="Hours spend",readonly=True)
    _sql_constraints = [
        ('unique_task', 'unique (name)', "This task already exists!"),
    ]

    @api.constrains('estimated_time','time_sheet')
    def _check_estimated_time(self):
        for rec in self:
            # print(rec.estimated_time)
            total_hours = 0
            for record in rec.time_sheet:
                # Search for all timesheets with the same task_id
                timesheets = self.env['task.time.sheet'].search([('task_id', '=', record.task_id.id)])
                # Sum up the hours from all timesheets with the same task_id
                total_hours = sum(timesheet.hours for timesheet in timesheets)
            # print(total_hours)
            rec.total_hours = total_hours
            if total_hours > rec.estimated_time:
                raise ValidationError("Total Time should be less than the estimated time")

    def close_task(self):
        for rec in self:
            rec.status = 'closed'

    def action_check_due_date(self):

        record_ids = self.search([('due_date', '<', date.today()), ('status', 'in', ['new', 'in_progress'])])
        print(fields.date.today())
        for rec in record_ids:
            print(rec.name)
            rec.is_late = True

