from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    continentOrigen = fields.Char('ContinentDeOrigen')
    dataNaix = fields.Date('DataDeNaixament', required=True)
    paisOrigen = fields.Char('PaisOrigen')
    sexe = fields.Char('Sexe')

    def _get_name(self):
        for record in self:
            record.name = str(record.codi)