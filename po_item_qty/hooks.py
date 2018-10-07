# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "po_item_qty"
app_title = "Po Item Qty"
app_publisher = "Tunde Akinyanmi"
app_description = "Purchase Item Quantity modification"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tunde@francisakindele.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/po_item_qty/css/po_item_qty.css"
# app_include_js = "/assets/po_item_qty/js/po_item_qty.js"

# include js, css files in header of web template
# web_include_css = "/assets/po_item_qty/css/po_item_qty.css"
# web_include_js = "/assets/po_item_qty/js/po_item_qty.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "po_item_qty.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "po_item_qty.install.before_install"
# after_install = "po_item_qty.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "po_item_qty.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"po_item_qty.tasks.all"
# 	],
# 	"daily": [
# 		"po_item_qty.tasks.daily"
# 	],
# 	"hourly": [
# 		"po_item_qty.tasks.hourly"
# 	],
# 	"weekly": [
# 		"po_item_qty.tasks.weekly"
# 	]
# 	"monthly": [
# 		"po_item_qty.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "po_item_qty.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "po_item_qty.event.get_events"
# }

