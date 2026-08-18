# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    x_studio_cancelled = fields.Boolean(string='Cancelled', readonly=True)
    x_studio_created_date = fields.Datetime(string='Created Date')
    # TODO: x_studio_diagnosis_ids = fields.One2many(...) -- Studio inverse name unknown; port from Clear-DB manually.
    x_studio_end_quick_repair = fields.Boolean(string='End Quick Repair')
    x_studio_fully_invoiced_so = fields.Boolean(string='Fully Invoiced SO', readonly=True, store=False)
    x_studio_incomplete_delivery_available = fields.Boolean(string='Incomplete Delivery Available', readonly=True, store=False)
    x_studio_material_availability = fields.Selection([], string='Material Availability', readonly=True, store=False)
    x_studio_payment_type = fields.Selection([], string='Payment Type', readonly=True)
    x_studio_priority = fields.Selection([], string='Priority')
    x_studio_quick_repair_status_1 = fields.Selection([], string='Quick Repair Status')
    x_studio_quotation_type = fields.Selection([], string='Quotation Type', readonly=True)
    x_studio_related_information = fields.Binary(string='Related Information', readonly=True)
    x_studio_repair_completed_stage_updated = fields.Boolean(string='Repair Completed Stage Updated', readonly=True)
    x_studio_repair_image_01 = fields.Binary(string='Repair Image 01')
    x_studio_repair_image_02 = fields.Binary(string='Repair Image 02')
    x_studio_repair_reason = fields.Many2many('x_repair_reason', 'project_task_x_studio_repair_reason_rel', 'project_id', 'x_repair_reason_id', string='Repair Reason')
    x_studio_starting_date = fields.Datetime(string='Starting Date')
    x_studio_valid_confirm2_so = fields.Boolean(string='Valid Confirm2 SO', readonly=True, store=False)
    x_studio_valid_confirm_so = fields.Boolean(string='Valid Confirm SO', readonly=True, store=False)
    x_studio_valid_delivered_so = fields.Boolean(string='Valid Delivered SO', readonly=True, store=False)
    x_studio_valid_delivered_so2 = fields.Boolean(string='Valid Delivered SO2')
    x_studio_valid_diagnosis = fields.Boolean(string='Valid Diagnosis', readonly=True, store=False)
    x_studio_valid_invoiced_so = fields.Boolean(string='Valid Invoiced SO', readonly=True, store=False)
    x_studio_warranty_card = fields.Binary(string='Warranty Card', readonly=True)
    x_task_id_sale_order_count = fields.Integer(string='Task count', store=False)
