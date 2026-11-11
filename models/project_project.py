from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    document_1 = fields.Binary()
    document_2 = fields.Binary()
    document_3 = fields.Binary()
    image_1 = fields.Binary()
    image_2 = fields.Binary()
    image_3 = fields.Binary()
    project_group = fields.Many2one("project_groups", readonly=True)
    quotation_type = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
        readonly=True,
    )
    repair_project = fields.Boolean()
    valid_gm = fields.Boolean(string="Valid GM", readonly=True, store=False)
    created_from_project_no_account_move_count = fields.Integer(
        string="Created From Project No count", store=False
    )
    main_project_2_sale_order_line_count = fields.Integer(
        string="Main Project 2 count", store=False
    )
    project_no_account_move_line_count = fields.Integer(
        string="Project No count", store=False
    )
    project_no_bill_account_move_count = fields.Integer(
        string="Project No Bill count", store=False
    )
    project_no_issue_account_move_count = fields.Integer(
        string="Project No Issue count", store=False
    )
    project_no_settle_account_move_count = fields.Integer(
        string="Project No Settle count", store=False
    )
    project_no_x_sales_report_model_count = fields.Integer(
        string="Project No count", store=False
    )
