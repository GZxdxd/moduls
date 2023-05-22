from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    perill = fields.Boolean('PerillExtincio', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('NomCientific')
    nomVulgar = fields.Char('NomVulgar')
    animals_ids = fields.One2many('zoo.animal', 'especie_id', String='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.codi) + ": " + str(record.familia)