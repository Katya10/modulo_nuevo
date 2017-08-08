# -*- coding: utf-8 -*-


{

    'name' : 'Biblioteca',

    'version' : '1.0',

    'author' : 'Ing. Salazar C. J.',

    'summary' : 'Modulo de odoo para demo',

    'description' : 'modulo varios demo',

    'depends' : [

            'base',

            ],

    'data' : [              

            'biblioteca_view.xml',
            'security/ir.model.access.csv',
            'security/user_groups.xml',


                ],

    'installable' : True,

    'aplication' : True,    

}