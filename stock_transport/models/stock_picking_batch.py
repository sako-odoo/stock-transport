from odoo import fields,models,api

class StockPickingBatch(models.Model):
    _inherit = ["stock.picking.batch"]

    dock_id = fields.Many2one('stock.dock.list',string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle.model',string="Vehicle")
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
    weight = fields.Float(compute="_compute_weight_and_volume", store=True)
    volume = fields.Float(compute="_compute_weight_and_volume", store=True)

    @api.depends('move_line_ids')
    def _compute_weight_and_volume(self):
        for record in self:
            com_weight = 0
            com_volume = 0
            for product_line in record.move_line_ids:
                com_weight += product_line.product_id.weight * product_line.quantity
                com_volume += product_line.product_id.volume * product_line.quantity
            record.weight = com_weight
            record.volume = com_volume
