from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Definición correcta de campos Many2one y Many2many
    mp_flujo_id = fields.Many2one('mp.flujo', string='Flujo')
    mp_grupo_flujo_ids = fields.Many2many(
        comodel_name='mp.grupo.flujo', 
        relation='account_move_mp_grupo_flujo_rel',  # Asegúrate de usar un nombre único y válido
        column1='move_id', 
        column2='grupo_flujo_id', 
        string='Grupo de Flujos'
    )
    mp_grupo_flujo_id = fields.Many2one('mp.grupo.flujo', string='Grupo de Flujo')


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # Definiciones de campos related ajustadas para asegurar que apunten correctamente
    invoice_date = fields.Date(related='move_id.invoice_date', store=True)
    l10n_latam_document_type_id = fields.Many2one(related='move_id.l10n_latam_document_type_id', store=True)
    journal_id = fields.Many2one(related='move_id.journal_id', store=True)
    mp_flujo_id = fields.Many2one(related='move_id.mp_flujo_id', store=True)
    mp_grupo_flujo_ids = fields.Many2many(related='move_id.mp_grupo_flujo_ids', store=True)
    mp_grupo_flujo_id = fields.Many2one(related='move_id.mp_grupo_flujo_id', store=True)
    invoice_origin = fields.Char(related='move_id.invoice_origin', store=True)
    vat = fields.Char(related='move_id.partner_id.vat', store=True)
    code_account = fields.Char(related='account_id.code', string='Número de Cuenta Contable', store=True)
