from odoo import models, Command, fields

class SaleOrderTask(models.Model):
    _inherit = "sale.order"

    is_commission = fields.Boolean("Add Commission")