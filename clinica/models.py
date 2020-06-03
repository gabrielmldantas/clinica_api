import datetime
from clinica import db

class Especialidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao}

class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    crm = db.Column(db.String(10), nullable=False, unique=True)
    id_especialidade = db.Column(db.Integer, db.ForeignKey('especialidade.id'), nullable=False)

    especialidade = db.relationship('Especialidade')

    def to_dict(self):
        return {
                'id': self.id,
                'nome': self.nome,
                'crm': self.crm,
                'especialidade': self.especialidade.to_dict()
            }

class Cobertura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao}

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(150), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.Integer)

    def to_dict(self):
        return {'id': self.id, 'rua': self.rua, 'bairro': self.bairro, 'numero': self.numero}

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    rg = db.Column(db.String(8), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)

    endereco = db.relationship('Endereco')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'dataNascimento': self.data_nascimento.strftime('%d/%m/%Y'),
            'telefone': self.telefone,
            'rg': self.rg,
            'cpf': self.cpf,
            'endereco': self.endereco.to_dict()
        }

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    senha = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'username': self.username,
            'email': self.email
        }

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False)
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    id_cobertura = db.Column(db.Integer, db.ForeignKey('cobertura.id'), nullable=False)

    medico = db.relationship('Medico')
    paciente = db.relationship('Paciente')
    cobertura = db.relationship('Cobertura')
    pagamentos = db.relationship('Pagamento')
    receitas_medicas = db.relationship('ReceitaMedica')
    requisicoes_exames = db.relationship('RequisicaoExames')

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.strftime('%d/%m/%Y %H:%M'),
            'medico': self.medico.to_dict(),
            'paciente': self.paciente.to_dict(),
            'cobertura': self.cobertura.to_dict(),
            'pagamentos': [pagamento.to_dict() for pagamento in self.pagamentos],
            'receitasMedicas': [receita.to_dict() for receita in self.receitas_medicas],
            'requisicoesExames': [exame.to_dict() for exame in self.requisicoes_exames]
        }

class FormaPagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), nullable=False)
    vista = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'descricao': self.descricao, 'vista': 'true' if self.vista else 'false'}

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data_pagamento = db.Column(db.DateTime, nullable=False)
    id_forma_pagamento = db.Column(db.Integer, db.ForeignKey('forma_pagamento.id'), nullable=False)
    id_consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)

    forma_pagamento = db.relationship('FormaPagamento')
    consulta = db.relationship('Consulta')

    def to_dict(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'dataPagamento': self.data_pagamento,
            'formaPagamento': self.forma_pagamento.to_dict()
        }

class ReceitaMedica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data = db.Column(db.Date, nullable=False)
    id_consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)

    consulta = db.relationship('Consulta')

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'data': self.data.strftime('%d/%m/%Y')
        }

class RequisicaoExames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    data = db.Column(db.Date, nullable=False)
    id_consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable=False)

    consulta = db.relationship('Consulta')

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'data': self.data.strftime('%d/%m/%Y')
        }