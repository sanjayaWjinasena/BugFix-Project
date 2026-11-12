"""Phase F1: seed ir.model.fields.selection records for state=base fields via SQL.
Odoo 17: `name` column is JSONB (translation) - must be JSON-encoded, not plain str."""

import json


def migrate(cr, version):
    if not version:
        return
    # (model, field_name, value, display_name, sequence)
    data = [
        ("project.task", "quotation_type", "Sales", "Sales", 10),
        ("project_category_gro", "transaction_type", "Item", "Item", 10),
        ("project_category", "transaction_type", "Item", "Item", 10),
        ("project_category", "claimability", "None", "None", 10),
        ("project.project", "quotation_type", "Sales", "Sales", 10),
        ("project.update", "selection_field_0zgmv", "Pending", "Pending", 10),
        ("project.task", "quotation_type", "Project", "Project", 1),
        (
            "project_category_gro",
            "transaction_type",
            "Expense",
            "Expense",
            1,
        ),
        ("project_category", "transaction_type", "Expense", "Expense", 1),
        ("project_category", "claimability", "Claimable", "Claimable", 1),
        ("project.project", "quotation_type", "Project", "Project", 1),
        (
            "project.update",
            "selection_field_0zgmv",
            "Completed",
            "Completed",
            1,
        ),
        ("project.task", "quotation_type", "Repair", "Repair", 2),
        ("project_category_gro", "transaction_type", "Fee", "Fee", 2),
        ("project_category", "transaction_type", "Fee", "Fee", 2),
        (
            "project_category",
            "claimability",
            "Non-Claimable",
            "Non-Claimable",
            2,
        ),
        ("project.project", "quotation_type", "Repair", "Repair", 2),
        ("project_category_gro", "transaction_type", "Hour", "Hour", 3),
        ("project_category", "transaction_type", "Hour", "Hour", 3),
    ]
    for model, name, value, display, seq in data:
        # Name is a JSONB translation field in Odoo 17
        name_json = json.dumps({"en_US": display})
        cr.execute(
            """
            INSERT INTO ir_model_fields_selection
                (field_id, value, name, sequence, create_uid, create_date, write_uid, write_date)
            SELECT f.id, %s, %s::jsonb, %s, 1, NOW() AT TIME ZONE 'UTC', 1, NOW() AT TIME ZONE 'UTC'
            FROM ir_model_fields f
            WHERE f.model = %s AND f.name = %s AND NOT EXISTS (
                SELECT 1 FROM ir_model_fields_selection s
                WHERE s.field_id = f.id AND s.value = %s
            )
        """,
            (value, name_json, seq, model, name, value),
        )
