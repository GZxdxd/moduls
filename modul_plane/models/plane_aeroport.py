from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom', required=True)
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais', required=True)
    latitud = fields.Float('Latitud', required=True)
    longitud = fields.Float('Longitud', required=True)

    def _get_name(self):
        for record in self:
            record.name = str(record.codi) + ": " + str(record.nom)