import frappe

def get_context(context):

	context['house'] = frappe.get_all("Property",
                            	fields=["name","property_name","property_owner","status","agent"],
                          	order_by="name desc")
