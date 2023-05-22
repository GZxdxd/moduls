from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca', required=True)
    model = fields.Char('Model', required=True)
    maxVel = fields.Float('maxVel')
    vols_ids = fields.One2many('plane.vol', 'avio_id', String='Vols')

    def _get_name(self):
        for record in self:
            record.name = str(record.codi) + ": " + str(record.nom)