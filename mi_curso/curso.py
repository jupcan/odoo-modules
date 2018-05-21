# -*- coding: utf-8 -*-
from openerp.osv import fields, orm
from types import *

class curso(orm.Model):

	_name = "res.curso"
	_description = "lista de cursos"
	_columns = {
		'nombre' : fields.char('nombre', size=64, required=True),
		'edicion': fields.many2many('product.template', 'cursoedicion','nombre', 'name', 'ediciones')
	}

	_sql_constraints = [('nombre_unique', 'UNIQUE(nombre)', "no puede haber dos cursos con el mismo nombre")]