from odoo import api, models, fields, tools, _
from odoo.exceptions import ValidationError


class SampleModelBusinessLogic(models.Model):

    # ----------------------------------------------------
    #
    # Model Definition
    #
    # ----------------------------------------------------

    _name = 'app.odoo_sample_module.sample_model'
    _inherit = ['app.odoo_sample_module.sample_model']

    # ----------------------------------------------------
    #
    # Fields Compute
    #
    # ----------------------------------------------------

    def action_set_state_pendente(self):
        self.state = 'pendente'
        return True

    def action_set_state_concluido(self):
        self.state = 'concluido'
        return True

    def action_set_state_cancelado(self):
        self.state = 'cancelado'
        return True
