# -*- coding: utf-8 -*-
"""BugFix-Project v17.0.0.0.61: seed ir.model.fields.selection rows via
Odoo's own _update_selection helper (framework API, not cr.execute).

Companion to _seed_field_selections in ../../hooks.py; this covers
version-upgrade path (post_init_hook covers fresh install).
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
    Sel = env['ir.model.fields.selection'].sudo()
    Fld = env['ir.model.fields'].sudo()
    grouped = {}
    for model, fname, value, label, seq in _FIELD_SELECTIONS:
        grouped.setdefault((model, fname), []).append((value, label, seq))
    for (model, fname), values in grouped.items():
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            continue
        existing_recs = Sel.search(
            [('field_id', '=', fld.id)], order='sequence',
        )
        existing_pairs = [(r.value, r.name) for r in existing_recs]
        existing_values = {v for v, _ in existing_pairs}
        added = []
        for v, l, _seq in sorted(values, key=lambda t: t[2]):
            if v in existing_values:
                continue
            existing_pairs.append((v, l))
            existing_values.add(v)
            added.append(v)
        if not added:
            continue
        try:
            with cr.savepoint():
                Sel._update_selection(model, fname, existing_pairs)
                _logger.info(
                    "BugFix-Project v17.0.0.0.61: seeded %s.%s += %s.",
                    model, fname, added,
                )
        except Exception as e:
            _logger.warning(
                "BugFix-Project v17.0.0.0.61: seed failed %s.%s (%s).",
                model, fname, e,
            )
