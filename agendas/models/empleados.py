from odoo import models, fields, api, _


class empleados(models.Model):
    _name = 'agendas.empleados'
    cif = fields.Char('CIF', required=True)
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Dirección', required=False)

    def name_get(self):
        res = []
        for record in self:
            name = record.cif + ' - ' + record.nombre
            res.append((record.id, name))
        return res
