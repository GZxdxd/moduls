from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    codi = fields.Integer('Codi', required=True)
    perill = fields.Boolean('PerillExtincio', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('NomCientific')
    nomVulgar = fields.Char('NomVulgar')