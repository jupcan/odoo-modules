# -*- coding: utf-8 -*-
from openerp import api, fields, models

class inscripcion(models.Model):

	_name = 'academy.inscripcion'
	_description = 'inscripcion'
	
	alumno = fields.Many2one(comodel_name ='res.partner', string= 'alumno', required=True)
	edicion = fields.Many2one(comodel_name ='product.product', string= 'ediciones')
	estado = fields.Selection([('pendiente','pendiente'),('inscrito','inscrito'),('aprobado','aprobado'),('suspenso','suspenso')],'estado', required=True)