from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    cancelled = fields.Boolean(string="Cancelled", readonly=True)
    created_date = fields.Datetime()
    # TODO: diagnosis_ids = fields.One2many(...) -- Studio inverse name
    # unknown; port from Clear-DB manually.
    end_quick_repair = fields.Boolean()
    fully_invoiced_so = fields.Boolean(
        string="Fully Invoiced SO", readonly=True, store=False
    )
    incomplete_delivery_available = fields.Boolean(readonly=True, store=False)
    material_availability = fields.Selection(
        [
            ("Material Not Ready", "Material Not Ready"),
            ("Material Ready", "Material Ready"),
        ],
        readonly=True,
        store=False,
    )
    payment_type = fields.Selection(
        [("Cash", "Cash"), ("Credit", "Credit")], string="Payment Type", readonly=True
    )
    custom_reports_priority = fields.Selection(
        [
            ("Highest", "Highest"),
            ("High", "High"),
            ("Normal", "Normal"),
            ("Low", "Low"),
            ("Lowest", "Lowest"),
        ],
        string="Priority",
    )
    quick_repair_status_1 = fields.Selection(
        [("None", "None"), ("Quick Repair", "Quick Repair")],
        string="Quick Repair Status",
    )
    quotation_type = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
        string="Quotation Type",
        readonly=True,
    )
    related_information = fields.Binary(string="Related Information", readonly=True)
    repair_completed_stage_updated = fields.Boolean(
        string="Repair Completed Stage Updated", readonly=True
    )
    repair_image_01 = fields.Binary()
    repair_image_02 = fields.Binary()
    repair_reason = fields.Many2many(
        "repair_reason",
        "project_task_x_studio_repair_reason_rel",
        "project_id",
        "x_repair_reason_id",
    )
    starting_date = fields.Datetime()
    valid_confirm2_so = fields.Boolean(
        string="Valid Confirm2 SO", readonly=True, store=False
    )
    valid_confirm_so = fields.Boolean(
        string="Valid Confirm SO", readonly=True, store=False
    )
    valid_delivered_so = fields.Boolean(
        string="Valid Delivered SO", readonly=True, store=False
    )
    valid_delivered_so2 = fields.Boolean(string="Valid Delivered SO2")
    valid_diagnosis = fields.Boolean(readonly=True, store=False)
    valid_invoiced_so = fields.Boolean(
        string="Valid Invoiced SO", readonly=True, store=False
    )
    warranty_card = fields.Binary(string="Warranty Card", readonly=True)
    task_id_sale_order_count = fields.Integer(string="Task count", store=False)


class ProjectTaskGap(models.Model):
    _inherit = "project.task"

    task_id_sale_order_count = fields.Integer(string="Task count")
