from odoo import fields, models, api
from odoo.tools import format_amount



class PurchaseOrder(models.Model):
    """Inherited the model for adding the dashboard values"""
    _inherit = 'purchase.order'

    @api.model
    def get_dashboard_values(self):
        """This method returns values to the dashboard in sale order views."""
        result = {
            'total_orders': 0,
            'total_purchase_untaxed_amount': 0,
            'total_purchase_amount': 0,
        }
        purchase_order = self.env['purchase.order']
        user = self.env.user
        result['total_orders'] = purchase_order.search_count([])
        order_sum = """select sum(amount_total) from purchase_order where state 
        in ('purchase', 'done')"""
        self._cr.execute(order_sum)
        res = self.env.cr.fetchone()
        result['total_purchase_amount'] = format_amount(self.env, res[0] or 0,
                                                    self.env.company.currency_id)
        untaxed_sum = """select sum(amount_untaxed) from purchase_order where state 
        in ('purchase', 'done')"""
        self._cr.execute(untaxed_sum)
        res = self.env.cr.fetchone()
        result['total_purchase_untaxed_amount'] = format_amount(self.env, res[0] or 0,
                                                    self.env.company.currency_id)

        return result
