"""Phase F1: seed missing ir.model.fields.selection records for state=base fields.
Odoo blocks XML/ORM writes to state=base field selections. This migration uses
direct SQL to bypass that restriction — safe because our tuples come from
CDB's ground truth and match the Python selection= tuples in fields.Selection().
"""

def migrate(cr, version):
    if not version:
        return
    # (model, field_name, value, display_name, sequence)
    data = [
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
    for model, name, value, display, seq in data:
        cr.execute("""
            INSERT INTO ir_model_fields_selection
                (field_id, value, name, sequence, create_uid, create_date, write_uid, write_date)
            SELECT f.id, %s, %s, %s, 1, NOW() AT TIME ZONE 'UTC', 1, NOW() AT TIME ZONE 'UTC'
            FROM ir_model_fields f
            WHERE f.model = %s AND f.name = %s AND NOT EXISTS (
                SELECT 1 FROM ir_model_fields_selection s
                WHERE s.field_id = f.id AND s.value = %s
            )
        """, (value, display, seq, model, name, value))