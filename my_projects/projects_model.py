# -*- coding: utf-8 -*-
from openerp import models, fields

STATE = [('draft', 'Draft'), 
		('in_progress', 'In Progress'),
		 ('cancel', 'Cancel'), 
		 ('done', 'Done')]
class project(models.Model):
	#model name
	_name = 'my.project'
	
	name = fields.Char('Name', required=True)
	
	
	description = fields.Text('Description')
	start_date = fields.Date('Start Date')
	end_date = fields.Date('End Date')
	is_done = fields.Boolean('Is Done?')
	is_active = fields.Boolean('Is Active', default=True)
	total = fields.Char('Total')
