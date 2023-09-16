# -*- coding: utf-8 -*-

from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    sales_persons = fields.One2many('res.partner.detail',
                                    'crm_team_id',
                                    string='Sales Persons')
