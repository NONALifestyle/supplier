# Copyright (c) 2022, mustakim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SupplierCatalogueItem(Document):
    def after_insert(self):
        # after insert login
        # 1. Add item to actual item doc in stock module.
        # 2. Generate Item Price List
        return True
