from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Tenant"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Agent",
              "label": _("Agent"),
              "description": _("People in charge of properties."),
            },
            {
              "type": "doctype",
              "name": "Tenant",
              "label": _("Tenant"),
              "description": _("People who have rented a property."),
            },
            {
              "type": "doctype",
              "name": "Property",
              "label": _("Property"),
              "description": _("Properties available for rent"),
            },
            {
              "type": "doctype",
              "name": "Payment",
              "label": _("Payment"),
              "description": _("Rental payments made by tenants."),
            }
          ]
      }
  ]

