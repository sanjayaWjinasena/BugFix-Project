# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectTaskGap(models.Model):
    _inherit = 'project.task'

    x_task_id_sale_order_count = fields.Integer(string='Task count')
