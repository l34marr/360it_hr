# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class 360it_hr(models.Model):
#     _name = '360it_hr.360it_hr'
#     _description = '360it_hr.360it_hr'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
