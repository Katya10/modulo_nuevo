# -*- coding: utf-8 -*-


from openerp import models, fields, api


class biblioteca_libro(models.Model):

    _name = 'biblioteca.libro' #nombre del modelo


    name = fields.Char(string='Titulo', required=True,)



    description = fields.Text('Observacion')

    date = fields.Date(string='Fecha de registro')