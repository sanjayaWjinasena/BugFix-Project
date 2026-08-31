# -*- coding: utf-8 -*-
"""x_sales_report_model is owned by Jinasena_Masterdata_Reporting.

All fields (scalar, Many2one, Many2many, related O2Ms) are declared there.
BugFix-Project has no additional fields to contribute.

v10: converted from _name (sentinel) to _inherit — same reason as
BugFix-Sales v53 fix for x_sales_report_type: two competing _name
declarations without a dep chain caused registry KeyError on startup.
"""
from odoo import models


class XSalesReportModel(models.Model):
    _inherit = 'x_sales_report_model'
