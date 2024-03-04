from odoo import models,fields

class StockDockList(models.Model):
    _name = "stock.dock.list"
    _discription = "Fleet Dock List"

    name = fields.Char(string="Dock")
