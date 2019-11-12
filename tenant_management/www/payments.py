import frappe

def get_context(context):

	context['payment'] = frappe.get_all("Payment",
                            	fields=["payment_date","property","agent","amount"],
                          	order_by="payment_date desc")
