from odoo import models,fields,api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume",compute="_compute_weight_and_volume")

    @api.depends('move_ids')
    def _compute_weight_and_volume(self):
        for record in self:
            com_volume = 0
            for transfers in record.move_ids:
                com_volume += transfers.product_id.volume * transfers.quantity
            record.volume = com_volume
