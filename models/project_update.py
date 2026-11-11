from odoo import fields, models


class ProjectUpdate(models.Model):
    _inherit = "project.update"

    actual_gp = fields.Float(string="Actual GP")
    estimated_gp = fields.Float(string="Estimated GP")
    financial_progress = fields.Float(string="Financial Project Progress")
    gross_margin_report = fields.Many2one(
        "sales_report_model", string="Gross Margin Report"
    )
    selection_field_0zgmv = fields.Selection(
        [("Pending", "Pending"), ("Completed", "Completed")],
        string="Project Update Status",
    )
