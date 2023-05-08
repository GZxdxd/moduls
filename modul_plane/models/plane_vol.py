from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.DateTime('DataSortida')
    dataArrivada = fields.DateTime('DataArrivada')