from odoo import fields, models


class CustomerPaymentWizard(models.Model):
    _name = 'customer.payment.wizard'
    _description = 'Customer Payment Wizard'

    from_date = fields.Datetime(string="From Date")
    to_date = fields.Datetime(string="To Date")

    def action_generate_report(self):
        """
            Function to check the customers sale orders in between given dates and return a PDF Report having,
            Customer name
            First Sale Order Date
            Total Sale Count
            Total Amount
            Paid Amount
            Balance
        """

        # SQL query for fetch all sale orders
        query_sale_orders = """
            SELECT id, partner_id, create_date 
            FROM sale_order 
            WHERE state = 'sale' 
            AND create_date >= %s 
            AND create_date <= %s 
            ORDER BY id DESC
        """

        self.env.cr.execute(query_sale_orders, (self.from_date, self.to_date))
        sale_orders = self.env.cr.fetchall()

        datas = []

        if sale_orders:
            for sale_order in sale_orders:
                partner_id = sale_order[1]
                sale_order_create_date = sale_order[2]

                # SQL query for fetching partner's sale orders
                query_partner_orders = """
                    SELECT amount_total 
                    FROM sale_order 
                    WHERE partner_id = %s 
                    AND state = 'sale'
                """

                self.env.cr.execute(query_partner_orders, (partner_id,))
                partner_orders = self.env.cr.fetchall()

                total_amount = sum(order[0] for order in partner_orders)

                # SQL query for fetching payments for the specific partner
                query_payments = """
                    SELECT amount 
                    FROM account_payment 
                    WHERE partner_id = %s 
                    AND payment_type = 'inbound'
                    
                """

                self.env.cr.execute(query_payments, (partner_id,))
                payments = self.env.cr.fetchall()

                paid_amount = sum(payment[0] for payment in payments)

                # SQL query for fetching the partner name
                query_partner_name = """
                    SELECT name 
                    FROM res_partner 
                    WHERE id = %s
                """

                self.env.cr.execute(query_partner_name, (partner_id,))
                partner_name = self.env.cr.fetchone()[0]

                val = {
                    'customer_name': partner_name,
                    'first_sale_date': sale_order_create_date,
                    'total_sale_count': len(partner_orders),
                    'total_amount': total_amount,
                    'paid_amount': paid_amount,
                    'balance_amount': total_amount - paid_amount
                }
                if not datas:
                    datas.append(val)
                else:
                    add_val = True
                    for data in datas:
                        if data.get('customer_name') == partner_name:
                            add_val = False
                    if add_val:
                        datas.append(val)

        data = {'data': datas}
        return self.env.ref('yg_cust_payment.action_customer_payment_report').report_action(None, data=data)
