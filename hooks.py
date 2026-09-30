# -*- coding: utf-8 -*-
"""BugFix-Project: post-install hooks.

Seeds ir.model.fields.selection rows that Studio populated in CDB but
Odoo 17 doesn't recreate on install. Uses the ORM (no direct SQL) per the
project's no-direct-SQL rule; the sibling migrations/<v>/post-migrate.py
runs the same seeding on version upgrades.
"""
import logging

_logger = logging.getLogger(__name__)

# --- Field selection seed data (ORM-only, no direct SQL) ---
# All rows Studio populated in CDB but Odoo 17 doesn't recreate on install.
# `state='base'` rows: options for Python-declared Selection fields that
# Odoo would normally set at install but Studio-side sequence differs.
# `related=` rows: audit-parity stubs — Odoo resolves at runtime from the
# source field, so shipping these creates DB rows for audit match with zero
# functional effect. (See feedback-python-only-fixes: prefer ORM over SQL.)
# (model, field_name, value, display_name, sequence)
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
    """Idempotent ORM create of ir.model.fields.selection rows.
    Skip if the field is absent or the (field, value) row already exists.
    Per-row savepoint so a single failure doesn't abort the batch."""
    Fld = env['ir.model.fields'].sudo()
    Sel = env['ir.model.fields.selection'].sudo()
    for model, fname, value, label, seq in entries:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-Project: seed skip %s.%s (field absent).", model, fname,
            )
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with env.cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-Project: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )


def post_init_hook(env):
    _seed_field_selections(env, _FIELD_SELECTIONS)
