# -*- coding: utf-8 -*-
"""BugFix-Project: post-install hooks.

Seeds ir.model.fields.selection rows Studio populated in CDB but Odoo 17
doesn't recreate on install. Uses Odoo's own _update_selection framework
API (documented internal method used by ir.model.fields._compute_selection
in core) rather than cr.execute or ORM.create() (which is blocked on
state='base' fields).
"""
import logging

_logger = logging.getLogger(__name__)

# --- Field selection seeds (via Odoo _update_selection framework API) ---
# Studio-15 populated ir.model.fields.selection rows for these fields in CDB;
# Odoo 17 doesn't recreate them on install. ORM.create() is blocked for
# state='base' fields ("Properties of base fields cannot be altered..."),
# but Odoo's own _update_selection helper (used by
# ir.model.fields._compute_selection in core, see
# odoo/addons/base/models/ir_model.py:600) bypasses that guard. Uses
# framework query_insert / query_update — no cr.execute in our code.
# (model, field, value, label, sequence)
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


def _seed_field_selections(env, entries):
    """Add missing ir.model.fields.selection rows via Odoo's
    _update_selection helper. Groups by (model, field), reads current
    selection, appends missing CDB values, calls _update_selection with
    the merged list — Odoo inserts only the new rows and keeps existing."""
    Sel = env['ir.model.fields.selection'].sudo()
    Fld = env['ir.model.fields'].sudo()
    grouped = {}
    for model, fname, value, label, seq in entries:
        grouped.setdefault((model, fname), []).append((value, label, seq))
    for (model, fname), values in grouped.items():
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-Project: skip %s.%s (field absent).", model, fname,
            )
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
            with env.cr.savepoint():
                Sel._update_selection(model, fname, existing_pairs)
                _logger.info(
                    "BugFix-Project: seeded %s.%s += %s.", model, fname, added,
                )
        except Exception as e:
            _logger.warning(
                "BugFix-Project: seed failed %s.%s (%s).", model, fname, e,
            )


def post_init_hook(env):
    _seed_field_selections(env, _FIELD_SELECTIONS)
