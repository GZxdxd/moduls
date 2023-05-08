from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom', required=True)
    cognoms = fields.Char('Cognoms', required=True)
    nif = fields.Char('NIF', required=True)
    telf = fields.Char('Telf', required=True)
    email = fields.Char('Email')