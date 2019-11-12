import frappe

def get_context(context):
	context['agents'] =frappe.get_all("Agent",
                          	fields=["name","first_name", "last_name", "phone_no"],
                          	order_by="name desc")

	context['prop'] =frappe.get_all("Property",
                          	fields=["name","property_name","agent"],
                          	order_by="name desc")

	context['tenant'] = frappe.get_all("Tenant",
                          	fields=["name","agent"],
                          	order_by="name desc")
