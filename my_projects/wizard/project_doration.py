from openerp import models, fields, api
import datetime

class doration(models.TransientModel):
	_name = 'project.doration'

	doration_type = fields.Selection(string='Type', 
									selection=[('years', 'Years'), 
									('months', 'Months'), 
									('days', 'Days')])


	@api.multi
	def calc_doration(self):
		#get ids of records to be updated, then calcuate date doration
		projects_ids = self.env['my.project'].browse(self._context.get('active_ids'))
		for project in projects_ids:
			start_date = project.start_date
			end_date = project.end_date
			if self.doration_type == 'years':
				total_years_end = datetime.datetime.strptime(end_date, "%Y-%m-%d").year
				total_years_start = datetime.datetime.strptime(start_date, "%Y-%m-%d").year
				project.total =  str(total_years_end - total_years_start) + " yeas"
			elif self.doration_type == 'months':
				total_months_end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
				total_months_start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
				project.total = 'calc months here'
			else: 
				total_days_end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
				total_days_start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
				project.total = str((total_days_end - total_days_start).days) + " days" 
		return True

