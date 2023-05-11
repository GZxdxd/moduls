from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    codi = fields.Integer('Codi', required=True)
    continentOrigen = fields.Char('ContinentDeOrigen')
    dataNaix = fields.Date('DataDeNaixament', required=True)
    paisOrigen = fields.Char('PaisOrigen')
    sexe = fields.Char('Sexe')