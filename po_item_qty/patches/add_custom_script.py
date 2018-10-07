import frappe


def execute():
    js = """
frappe.ui.form.on("Purchase Order Item", {
	item_code: function(frm, cdt, cdn) {
		const row = locals[cdt][cdn];
		if (row.item_code) {
			frappe.call({
				method: 'po_item_qty.utils.get_all_qty',
				args: {'item_code': row.item_code},
				callback: function(r) {
					if (r.message) {
						frappe.model.set_value(cdt, cdn, 'quantity_in_all_warehouses', r.message);
					}
				}
			});
		} else {
			frappe.model.set_value(cdt, cdn, 'quantity_in_all_warehouses', 0);
		}
	}
});
"""

    if frappe.db.exists('Custom Script', 'Puchase Order-Client'):
        custom_script = frappe.get_doc('Custom Script', 'Puchase Order-Client')
    else:
        custom_script = frappe.new_doc('Custom Script')
        custom_script.dt = 'Purchase Order'
        custom_script.script = ''

    custom_script.script = '{0} \n{1}'.format(custom_script.script, js)
    custom_script.save()
