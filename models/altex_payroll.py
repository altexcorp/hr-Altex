# -*- coding: utf-8 -*-

from openerp import models , fields , api , _

class Hr_Contract(models.Model):

    _inherit = 'hr.contract'
    #bonus = fields.Float(string='Prime' ,default=0.0)
    #transport = fields.Float(string='Transport' ,default=0.0)
    #code = fields.char('Code', size=52, required=True, help="The code that can be used in the salary rules")

class Hr_Payslip(models.Model):

    _inherit = 'hr.payslip'
    date_today = fields.Date('Date de Buelltin',default=fields.Datetime.now)
    #contract_id = fields.Many2one('hr.contract', 'Contract to payslip')
    #transfer_now = fields.Many2one('hr.payslip.line','Transfer Now')
    prim_sud = fields.Float(string='Prime de Sud' ,default=0.0)
    frais_remboursables = fields.Float(string='Frais Remboursables' ,default=0.0)
    prim_rendement = fields.Float(string='Prime de Rendement' ,default=0.0)
    nombre_jour = fields.Integer(string='Nombre de Jour' ,default=0.0)
    indemnite_panier = fields.Float(string='Indemnite Panier' ,default=0.0)

class Hr_Employee(models.Model):

    _inherit = 'hr.employee'
    securite_sociale = fields.Char(string='N de securite sociele')