from odoo import models, fields
class zoo_zoo(models.Model):
    _name = 'zoo.zoo'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom', required=True)
    grandaria = fields.Char('Grandaria')
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais',required=True)

    def _get_name(self):
        for record in self:
            record.name = str(record.codi) + ": " + str(record.nom)