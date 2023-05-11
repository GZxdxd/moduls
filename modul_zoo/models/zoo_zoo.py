from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom', required=True)
    grandaria = fields.Char('Grandaria')
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais',required=True)