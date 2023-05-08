from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca', required=True)
    model = fields.Char('Model', required=True)
    maxVel = fields.Float('maxVel')