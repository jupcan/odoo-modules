# -*- coding: utf-8 -*-
from openerp.osv import fields, orm

class edicion(orm.Model):

  _inherit = "product.template"
  _description = "ediciones de cursos"
  _columns = {
    "is_course": fields.boolean("es edicion"),
    "profesor" : fields.many2one('hr.employee', "profesor", domain=[('job_id', '=', 'Profesor')]),
    "cursos"   : fields.many2one("res.curso", "curso de la edicion"),
    "fecha_in" : fields.date('fecha inicio'),
	"fecha_fin": fields.date('fecha fin'),
  }

  _sql_constraints = [('fecha_ccheck', 'CHECK(fecha_fin > fecha_in)', "la fecha inicial debe ser anterior a la final")]

edicion()