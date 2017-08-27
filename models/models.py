# -*- coding: utf-8 -*-

from odoo import models, fields, api

class checklist(models.Model):
    _name = 'checklist.checklist'
    name = fields.Char(string="Subject", required=True)
    description = fields.Text("Description")
    complete = fields.Boolean("Complete",help="status of this task. are u finish?")
    _order = "id asc" 

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100