from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom', required=True)
    imatge = fields.Char('Imatge')
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais', required=True)
    latitud = fields.Float('Latitud', required=True)
    longitud = fields.Float('Longitud', required=True)