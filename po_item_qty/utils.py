import frappe


@frappe.whitelist()
def get_all_qty(item_code):
    qty = frappe.db.sql(
        'SELECT SUM(actual_qty) FROM `tabBin` WHERE `item_code`= %s',
        item_code
    )

    if qty[0] and qty[0][0]:
        return qty[0][0]
    else:
        return 0
