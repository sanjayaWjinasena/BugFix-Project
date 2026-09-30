# -*- coding: utf-8 -*-
"""BugFix-Project v17.0.0.0.59: seed ir.model.fields.selection rows via ORM.

Same content as post_init_hook in ../hooks.py; this covers the version-upgrade
path (post-migrate runs on upgrade; hooks.py runs on fresh install). Uses the
ORM (no direct SQL) per the project's no-direct-SQL rule.

Idempotent: skips rows whose (field_id, value) already exists.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

_FIELD_SELECTIONS = [
    ('project.task', 'x_studio_quotation_type', 'Sales', 'Sales', 10),
    ('x_project_category_gro', 'x_studio_transaction_type', 'Item', 'Item', 10),
    ('x_project_category', 'x_studio_transaction_type', 'Item', 'Item', 10),
    ('x_project_category', 'x_studio_claimability', 'None', 'None', 10),
    ('project.project', 'x_studio_quotation_type', 'Sales', 'Sales', 10),
    ('project.update', 'x_studio_selection_field_0zgmv', 'Pending', 'Pending', 10),
    ('project.task', 'x_studio_quotation_type', 'Project', 'Project', 1),
    ('x_project_category_gro', 'x_studio_transaction_type', 'Expense', 'Expense', 1),
    ('x_project_category', 'x_studio_transaction_type', 'Expense', 'Expense', 1),
    ('x_project_category', 'x_studio_claimability', 'Claimable', 'Claimable', 1),
    ('project.project', 'x_studio_quotation_type', 'Project', 'Project', 1),
    ('project.update', 'x_studio_selection_field_0zgmv', 'Completed', 'Completed', 1),
    ('project.task', 'x_studio_quotation_type', 'Repair', 'Repair', 2),
    ('x_project_category_gro', 'x_studio_transaction_type', 'Fee', 'Fee', 2),
    ('x_project_category', 'x_studio_transaction_type', 'Fee', 'Fee', 2),
    ('x_project_category', 'x_studio_claimability', 'Non-Claimable', 'Non-Claimable', 2),
    ('project.project', 'x_studio_quotation_type', 'Repair', 'Repair', 2),
    ('x_project_category_gro', 'x_studio_transaction_type', 'Hour', 'Hour', 3),
    ('x_project_category', 'x_studio_transaction_type', 'Hour', 'Hour', 3),
]


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Fld = env['ir.model.fields']
    Sel = env['ir.model.fields.selection']
    for model, fname, value, label, seq in _FIELD_SELECTIONS:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-Project v17.0.0.0.59: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )
