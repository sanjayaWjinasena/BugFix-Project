from odoo import fields, models


class ProjectTaskGap(models.Model):
    _inherit = 'project.task'

    x_task_id_sale_order_count = fields.Integer(string='Task count')
