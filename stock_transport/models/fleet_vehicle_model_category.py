from odoo import fields,models,api

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Char(string='Max Weight(Kg)')
    max_volume = fields.Char(string='Max Volume(m³)')

    @api.depends('name','max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight}Kg, {record.max_volume}m³)"
