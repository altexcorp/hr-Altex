# -*- coding: utf-8 -*-

from openerp import models , fields , api , _

class Hr_Payslip(models.Model):

    _inherit = 'hr.payslip'
    date_d = fields.Date('Date D ',default=fields.Datetime.now)
    #code = fields.char('Code', size=52, required=True, help="The code that can be used in the salary rules")

