from odoo import fields,models,api

class StockPickingBatch(models.Model):
    _inherit = ["stock.picking.batch"]

    dock_id = fields.Many2one('stock.dock.list',string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle',string="Vehicle")
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category", related="vehicle_id.category_id", store=True)
    weight = fields.Float(compute="_compute_weight", store=True)
    weight_pr = fields.Float(compute="_compute_weight_pr")
    volume = fields.Float(compute="_compute_volume", store=True)
    volume_pr = fields.Float(compute="_compute_volume_pr")
    transfers = fields.Integer(compute="_compute_transfers_of_stocks", store=True)
    lines = fields.Integer(compute="_compute_lines_of_stocks", store=True)

    @api.depends('move_line_ids','vehicle_category_id')
    def _compute_weight(self):
        for record in self:
            com_weight = 0
            for product_line in record.move_line_ids:
                com_weight += product_line.product_id.weight * product_line.quantity
            record.weight = com_weight

    @api.depends('move_line_ids','vehicle_category_id')
    def _compute_weight_pr(self):
        for record in self:
            if record.vehicle_category_id.max_weight != 0:
                record.weight_pr = (100*record.weight)/record.vehicle_category_id.max_weight
            else:
                record.weight_pr = 0

    @api.depends('move_line_ids','vehicle_category_id')
    def _compute_volume(self):
        for record in self:
            com_volume = 0
            for product_line in record.move_line_ids:
                com_volume += product_line.product_id.volume * product_line.quantity
            record.volume = com_volume

    @api.depends('move_line_ids','vehicle_category_id')
    def _compute_volume_pr(self):
        for record in self:
            if record.vehicle_category_id.max_volume != 0:
                record.volume_pr = (100*record.volume)/record.vehicle_category_id.max_volume
            else:
                record.volume_pr = 0
    
    @api.depends('weight','volume','name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}: {record.weight}Kg, {record.volume}m³"

    @api.depends('picking_ids')
    def _compute_transfers_of_stocks(self):
        for record in self:
            record.transfers = len(record.picking_ids)

    @api.depends('move_line_ids')
    def _compute_lines_of_stocks(self):
        for record in self:
            record.lines = len(record.move_line_ids)
