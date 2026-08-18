# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectUpdate(models.Model):
    _inherit = 'project.update'

    x_studio_actual_gp = fields.Float(string='Actual GP')
    x_studio_estimated_gp = fields.Float(string='Estimated GP')
    x_studio_financial_progress = fields.Float(string='Financial Project Progress')
    x_studio_gross_margin_report = fields.Many2one('x_sales_report_model', string='Gross Margin Report')
    x_studio_selection_field_0zgmv = fields.Selection([], string='Project Update Status')
