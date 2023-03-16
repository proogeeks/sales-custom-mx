# © <2023> <ProoGeeks (dev@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class SaleOrderInh(models.Model):
    _inherit = 'sale.order'

    x_cusomer_rfc = fields.Char(string='RFC Cliente', related='partner_id.vat')
    x_sale_products = fields.Many2many('product.product', string='Products', compute='_compute_sale_products')

    @api.depends('order_line')
    def _compute_sale_products(self):
        for rec in self:
            rec.x_sale_products = rec.order_line.mapped('product_id')

    def send_pending_quotations_action(self):
        template = self.env.ref('sales_custom_mx.pending_sales_mail')
        mail_ctx = self.env.context.copy()
        self.env.cr.execute("""SELECT count(*), user_id FROM sale_order WHERE state IN ('draft', 'sent') GROUP BY user_id""")

        for r in self.env.cr.fetchall():
            user = self.env['res.users'].browse(r[1])
            mail_ctx.update({
                'pending_count': r[0]
            })
            template.with_context(mail_ctx).send_mail(self.id, force_send=True)
