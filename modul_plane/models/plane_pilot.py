from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom', required=True)
    cognoms = fields.Char('Cognoms', required=True)
    nif = fields.Char('NIF', required=True)
    telf = fields.Char('Telf', required=True)
    email = fields.Char('Email')
    vols_ids = fields.One2many('plane.vol', 'pilot_id', String='Vols')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + ": " + str(record.cognoms)