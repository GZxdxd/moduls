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
    volDesti_ids = fields.One2many('plane.vol', 'aeroportDesti_id', String='Vol Desti')
    volOrigen_ids = fields.One2many('plane.vol', 'aeroportOrigen_id', String='Vol Origen')

    def _get_name(self):
        for record in self:
            record.name = str(record.codi) + ": " + str(record.nom)