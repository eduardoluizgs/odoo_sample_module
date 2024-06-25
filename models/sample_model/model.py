from odoo import models, fields

from datetime import datetime


class SampleModelModel(models.Model):

    # ----------------------------------------------------
    #
    # Model Definition
    #
    # ----------------------------------------------------

    _name = 'app.odoo_sample_module.sample_model'
    _inherit = ['mail.thread']

    # ----------------------------------------------------
    #
    # Fields Default's
    #
    # ----------------------------------------------------

    def _get_default_data(self):
        """Retorna valor default para campo `Data`.

        Returns:
            _type_: _description_
        """
        return datetime.now().date()

    # ----------------------------------------------------
    #
    # Fields
    #
    # ----------------------------------------------------

    # Exemplo do campo de TEXTO
    name = fields.Char(
        string='Nome', # Indica o label que será exibido para o usuário
        size=100, # Indica o tamanho máximo do campo
        requrired=True, # Indica se o campo é obrigatório
        help='Informa o nome do registro' # Indica o texto de ajuda a ser mostrado para o usuário
    )

    # Exemplo do campo de TEXTO
    descricao = fields.Char(
        string='Descrição'
        # Caso não seja indicado o parâmetro `size` o tamanho do campo será 255.
    )

    # Exemplo do campo de DATA
    data = fields.Date(
        string='Data',
        requrired=True,
        default=_get_default_data # Chama uma função customizada para retornar o valor padrão/inicial do campo quando criamos novos registros.
    )

    # Exemplo do campo de RELACIONAMENTO 1..* (um p/ muitos)
    # utilizando o modelo padrão do Odoo para cadastro de pessoas
    partner_id = fields.Many2one(
        sttring='Pessoa',
        comodel_name='res.partner',
        requrired=True
    )

    # Exemplo do campo de RELACIONAMENTO 1..* (um p/ muitos)
    # utilizando o modelo padrão do Odoo para cadastro de usuários
    user_id = fields.Many2one(
        sttring='Usuário',
        comodel_name='res.users'
    )

    # Exemplo do campo de RELACIONAMENTO 1..* (um p/ muitos)
    # utilizando o modelo padrão do Odoo para cadastro de empresas
    company_id = fields.Many2one(
        sttring='Empresa',
        comodel_name='res.company'
    )

    # Exemplo de campo de VALOR
    valor = fields.Float(
        string='Valor do Pagamento',
        default=0 # Indica um valor fixo padrão/inicial do campo quando está incluindo novos registros.
    )

    # Exemplo de campo INTEIRO
    numero_inteiro = fields.Integer(
        string='Número Inteiro',
        default=0
    )

    # Exemplo de campo de Estado/Situação
    # Manter o nome do campo `state` para compatilizar com os recursos nativos do Odoo.
    state = fields.Selection(
        string='Situação',
        selection=[ # Indica as opções do campo de estado ('value', 'Descrição')
            ('pendente', 'Pendente'),
            ('concluido', 'Concluído'),
            ('cancelado', 'Cancelado'),
        ],
        help='''Indica o estado do registro:
            * Pendente: ...
            * Conclído: ...
            * Cancelado: ...
        ''',
        tracking=True # Indica se o campo será logado no registro de Atividades
    )