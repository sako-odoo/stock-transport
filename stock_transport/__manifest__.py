{
    'name' : 'Transport Management System',
    'version' : "1.0",
    'category': 'Inventory/Inventory',
    'discription' : "",
    'depends': ['stock_picking_batch','fleet'],
    'license': "LGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
    ],
    'installable' : True,
}
