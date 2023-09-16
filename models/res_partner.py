# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _name = 'res.partner.detail'
    sales_person = fields.Many2one('res.users',string='Salesperson')
    # , domain="[('id', '=', crm_team_id.member_ids.ids)]"
    target = fields.Float(string='Target')
    achieved = fields.Float(string='Achieved')
    tier = fields.Selection([('tier1','Tier1'),('tier2','Tier2'),('Tier3','Tier3'),('tier4','Tier4')],string='Tier')
    percentage = fields.Float(string='Commission%')
    commission = fields.Float(string="commission", compute='compute_commission')
    min_eligibility = fields.Float(string='Min eligibility',compute='compute_eligibility')
    crm_team_id = fields.Many2one('crm.team')

    @api.depends('achieved', 'min_eligibility')
    def compute_commission(self):
        for record in self:
            if record.achieved > record.min_eligibility:
                record.commission = record.achieved * record.percentage
            else:
                record.commission = 0.0

    @api.depends('target')
    def compute_eligibility(self):
        for record in self:
            record.min_eligibility = 80*record.target/100
