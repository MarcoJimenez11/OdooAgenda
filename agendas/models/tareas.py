from odoo import models, fields, api, _


class tareas(models.Model):
    _name = 'agendas.tareas'
    cod = fields.Char('Tarea', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    proveedor = fields.Many2one('agendas.empleados', 'Empleado', required=True)
    autor = fields.Many2one('res.users', default=lambda self: self.env.user, help='Autor de la tarea')
    image = fields.Binary()

    def name_get(self):
        res = []
        for record in self:
            name = record.cod + ' - ' + record.descripcion
            res.append((record.id, name))
        return res
