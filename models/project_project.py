# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    x_studio_document_1 = fields.Binary(string='Document 1')
    x_studio_document_2 = fields.Binary(string='Document 2')
    x_studio_document_3 = fields.Binary(string='Document 3')
    x_studio_image_1 = fields.Binary(string='Image 1')
    x_studio_image_2 = fields.Binary(string='Image 2')
    x_studio_image_3 = fields.Binary(string='Image 3')
    x_studio_project_group = fields.Many2one('x_project_groups', string='Project Group', readonly=True)
    x_studio_quotation_type = fields.Selection([], string='Quotation Type', readonly=True)
    x_studio_repair_project = fields.Boolean(string='Repair Project')
    x_studio_valid_gm = fields.Boolean(string='Valid GM', readonly=True, store=False)
    x_x_studio_created_from_project_no_account_move_count = fields.Integer(string='Created From Project No count', store=False)
    x_x_studio_main_project_2_sale_order_line_count = fields.Integer(string='Main Project 2 count', store=False)
    x_x_studio_project_no_account_move_line_count = fields.Integer(string='Project No count', store=False)
    x_x_studio_project_no_bill_account_move_count = fields.Integer(string='Project No Bill count', store=False)
    x_x_studio_project_no_issue_account_move_count = fields.Integer(string='Project No Issue count', store=False)
    x_x_studio_project_no_settle_account_move_count = fields.Integer(string='Project No Settle count', store=False)
    x_x_studio_project_no_x_sales_report_model_count = fields.Integer(string='Project No count', store=False)
