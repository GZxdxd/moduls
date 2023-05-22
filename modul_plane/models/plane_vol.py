from odoo import models, fields
class plane_vol(models.Model):
    _name = 'plane.vol'
    name = fields.Char(compute='_get_name', string="Nom Complet", readonly='True', store=False)
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Datetime('DataSortida')
    dataArrivada = fields.Datetime('DataArrivada')
    aeroportDesti_id = fields.Many2one('plane.aeroport', String='Destí')
    aeroportOrigen_id = fields.Many2one('plane.aeroport', String='Origen')
    avio_id = fields.Many2one('plane.avio', String='Avio')
    pilot_id = fields.Many2one('plane.pilot', String='Pilot')

    def _get_name(self):
        for record in self:
            record.name = str(record.codi) + ": " + str(record.nom)