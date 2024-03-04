{
    'name' : 'Transport Management System',
    'version' : "1.0",
    'category': 'Human Resources/Fleet',
    'category': "",
    'discription' : "",
    'depends': ['stock_picking_batch','fleet','stock'],
    'license': "LGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
    ],
    'installable' : True,
    'application' : True,
}
