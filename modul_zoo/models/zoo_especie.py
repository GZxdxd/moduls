from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    id = fields.Intiger('Id', required=True)
    perill = fields.Boolean('PerillExtincio', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('NomCientific')
    nomVulgar = fields.Char('NomVulgar')