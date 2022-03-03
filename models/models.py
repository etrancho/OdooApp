# -*- coding: utf-8 -*-

from odoo import models, fields, api


class regalos_regalos(models.Model):
    _name = 'regalos.regalos'

    id = fields.Integer(string="Id del regalo")
    name = fields.Char(string="Nombre del regalo")
    description = fields.Char(string="Descripción del regalo")
    tienda = fields.Many2one("regalos.tienda",
        string="Tienda",required=True,ondelete="cascade")
    imagen = fields.Binary(string="Foto del regalo")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

class regalos_tienda(models.Model):
    _name = 'regalos.tienda'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre de la tienda")
    direccion = fields.Char(string="Dirección de la tienda")
    regalos = fields.One2many("regalos.regalos",
        "tienda",string="Regalos")

    message_follower_ids = fields.One2many(
        'mail.followers', 'res_id', string='Followers', groups='base.group_user')
    activity_ids = fields.One2many(
        'mail.activity', 'res_id', 'Activities',
        auto_join=True,
        groups="base.group_user",)
    message_ids = fields.One2many(
        'mail.message', 'res_id', string='Messages',
        domain=lambda self: [('message_type', '!=', 'user_notification')], auto_join=True)


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100