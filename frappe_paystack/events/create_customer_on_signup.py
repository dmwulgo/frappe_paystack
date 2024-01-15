import frappe



def after_insert(doc, method):
    print(doc)
    """
    Create a customer when a new user is signed up
    """
    # Check if the user is newly created
    if doc.docstatus == 0:
        # Create a new customer
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": doc.first_name,
            "customer_type": "Individual",
            "first_name": doc.first_name,
            "last_name": doc.last_name,
            "email_id": doc.email,
            # Add other relevant customer fields as needed

        })
        
        # Save the customer document
        customer.insert(ignore_permissions=True)

                # Create a new portal user as a child of the customer
        portal_user = frappe.get_doc({
            "doctype": "Portal User",
            "parenttype": "Customer",
            "parentfield": "portal_users",
            "parent": customer.name,
            "email": doc.email,
            "user": doc.name,
            # Add other relevant portal user fields as needed
        })

        # Save the portal user document
        portal_user.insert(ignore_permissions=True)

