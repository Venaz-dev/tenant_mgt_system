import frappe

def get_context(context):

	context['tenant'] = frappe.get_all("Tenant",
                            	fields=["name","first_name","last_name","passport","agent"],
                          	order_by="name desc")
