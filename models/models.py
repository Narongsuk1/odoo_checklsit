# -*- coding: utf-8 -*-

from odoo import models, fields, api

class checklist(models.Model):
    _name = 'checklist.checklist'
    name = fields.Char(string="Subject", required=True)
    description = fields.Text("Description")
    complete = fields.Boolean("Complete",help="status of this task. are u finish?")
    _order = "id asc" 
