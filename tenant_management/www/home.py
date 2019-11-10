import frappe

def get_context(context):
    context['users'] = frappe.get_all('User')
    context['hub_items'] = frappe.get_all('Hub Item')
