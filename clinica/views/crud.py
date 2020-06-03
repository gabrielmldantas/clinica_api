import datetime
from clinica import app, db
from clinica.models import Especialidade, Medico, Cobertura, Paciente, Endereco, Usuario, Consulta, FormaPagamento, Pagamento, RequisicaoExames, ReceitaMedica
from flask import request, make_response
from werkzeug.security import generate_password_hash, check_password_hash

# Especialidade
@app.route('/especialidade', defaults={'id_especialidade': None}, methods=['GET', 'POST'])
@app.route('/especialidade/<int:id_especialidade>', methods=['PUT', 'DELETE'])
def especialidade(id_especialidade):
    if request.method == 'GET':
        especialidades = db.session.query(Especialidade).order_by(Especialidade.descricao).all()
        response = _to_result_list([esp.to_dict() for esp in especialidades])
        return response
    elif request.method == 'POST':
        especialidade = Especialidade()
        especialidade.descricao = request.json['descricao']
        db.session.add(especialidade)
        db.session.commit()
        return make_response(especialidade.to_dict())
    elif request.method == 'PUT':
        especialidade = db.session.query(Especialidade).get(id_especialidade)
        especialidade.descricao = request.json['descricao']
        db.session.commit()
        return make_response(especialidade.to_dict())
    else:
        especialidade = db.session.query(Especialidade).get(id_especialidade)
        db.session.delete(especialidade)
        db.session.commit()
        return ''

# Médico
@app.route('/medico', defaults={'id_medico': None}, methods=['GET', 'POST'])
@app.route('/medico/<int:id_medico>', methods=['PUT', 'DELETE'])
def medico(id_medico):
    if request.method == 'GET':
        medicos = db.session.query(Medico).order_by(Medico.nome).all()
        response = _to_result_list([medico.to_dict() for medico in medicos])
        return response
    elif request.method == 'POST':
        medico = Medico()
        medico.nome = request.json['nome']
        medico.crm = request.json['crm']
        medico.especialidade = db.session.query(Especialidade).get(request.json['especialidade']['id'])
        db.session.add(medico)
        db.session.commit()
        return make_response(medico.to_dict())
    elif request.method == 'PUT':
        medico = db.session.query(Medico).get(id_medico)
        medico.nome = request.json['nome']
        medico.crm = request.json['crm']
        medico.especialidade = db.session.query(Especialidade).get(request.json['especialidade']['id'])
        db.session.commit()
        return make_response(medico.to_dict())
    else:
        medico = db.session.query(Medico).get(id_medico)
        db.session.delete(medico)
        db.session.commit()
        return ''

# Cobertura
@app.route('/cobertura', defaults={'id_cobertura': None}, methods=['GET', 'POST'])
@app.route('/cobertura/<int:id_cobertura>', methods=['PUT', 'DELETE'])
def cobertura(id_cobertura):
    if request.method == 'GET':
        coberturas = db.session.query(Cobertura).order_by(Cobertura.descricao).all()
        response = _to_result_list([cobertura.to_dict() for cobertura in coberturas])
        return response
    elif request.method == 'POST':
        cobertura = Cobertura()
        cobertura.descricao = request.json['descricao']
        db.session.add(cobertura)
        db.session.commit()
        return make_response(cobertura.to_dict())
    elif request.method == 'PUT':
        cobertura = db.session.query(Cobertura).get(id_cobertura)
        cobertura.descricao = request.json['descricao']
        db.session.commit()
        return make_response(cobertura.to_dict())
    else:
        cobertura = db.session.query(Cobertura).get(id_cobertura)
        db.session.delete(cobertura)
        db.session.commit()
        return ''

# Paciente
@app.route('/paciente', defaults={'id_paciente': None}, methods=['GET', 'POST'])
@app.route('/paciente/<int:id_paciente>', methods=['PUT', 'DELETE'])
def paciente(id_paciente):
    if request.method == 'GET':
        pacientes = db.session.query(Paciente).order_by(Paciente.nome).all()
        response = _to_result_list([paciente.to_dict() for paciente in pacientes])
        return response
    elif request.method == 'POST':
        paciente = Paciente()
        paciente.nome = request.json['nome']
        paciente.data_nascimento = datetime.datetime.strptime(request.json['dataNascimento'], '%d/%m/%Y')
        paciente.cpf = request.json['cpf']
        paciente.rg = request.json['rg']
        paciente.telefone = request.json['telefone']
        paciente.endereco = Endereco()
        paciente.endereco.rua = request.json['endereco']['rua']
        paciente.endereco.bairro = request.json['endereco']['bairro']
        paciente.endereco.numero = request.json['endereco'].get('numero', None)
        db.session.add(paciente)
        db.session.commit()
        return make_response(paciente.to_dict())
    elif request.method == 'PUT':
        paciente = db.session.query(Paciente).get(id_paciente)
        paciente.nome = request.json['nome']
        paciente.dataNascimento = datetime.datetime.strptime(request.json['dataNascimento'], '%d/%m/%Y')
        paciente.cpf = request.json['cpf']
        paciente.rg = request.json['rg']
        paciente.telefone = request.json['telefone']
        paciente.endereco.rua = request.json['endereco']['rua']
        paciente.endereco.bairro = request.json['endereco']['bairro']
        paciente.endereco.numero = request.json['endereco'].get('numero', None)
        db.session.commit()
        return make_response(paciente.to_dict())
    else:
        paciente = db.session.query(Paciente).get(id_paciente)
        endereco = paciente.endereco
        db.session.delete(paciente)
        db.session.delete(endereco)
        db.session.commit()
        return ''

@app.route('/usuario', methods=['POST'])
def usuario():
    usuario = Usuario()
    usuario.nome = request.json['nome']
    usuario.username = request.json['username']
    usuario.email = request.json['email']
    usuario.senha = generate_password_hash(request.json['senha'])
    db.session.add(usuario)
    db.session.commit()
    return '', 201

@app.route('/usuario/login', methods=['POST'])
def login():
    usuario = db.session.query(Usuario).filter(Usuario.username==request.json['username']).one_or_none()
    if usuario is not None and check_password_hash(usuario.senha, request.json['senha']):
        return make_response(usuario.to_dict())
    return 'Usuário ou senha inválidos.', 401

# Consulta
@app.route('/consulta', defaults={'id_consulta': None}, methods=['GET', 'POST'])
@app.route('/consulta/<int:id_consulta>', methods=['PUT', 'DELETE'])
def consulta(id_consulta):
    if request.method == 'GET':
        consultas = db.session.query(Consulta).order_by(Consulta.data).all()
        response = _to_result_list([consulta.to_dict() for consulta in consultas])
        return response
    elif request.method == 'POST':        
        consulta = Consulta()
        consulta.data = datetime.datetime.strptime(request.json['data'], '%d/%m/%Y %H:%M')
        consulta.medico = db.session.query(Medico).get(request.json['medico']['id'])
        consulta.paciente = db.session.query(Paciente).get(request.json['paciente']['id'])
        consulta.cobertura = db.session.query(Cobertura).get(request.json['cobertura']['id'])

        response = _validar_consulta(consulta)
        if response:
            return response

        db.session.add(consulta)
        db.session.commit()
        return make_response(consulta.to_dict())
    elif request.method == 'PUT':
        consulta = db.session.query(Consulta).get(id_consulta)
        consulta.data = datetime.datetime.strptime(request.json['data'], '%d/%m/%Y %H:%M')

        response = _validar_consulta(consulta)
        if response:
            return response

        db.session.commit()
        return make_response(consulta.to_dict())
    else:
        consulta = db.session.query(Consulta).get(id_consulta)
        db.session.delete(consulta)
        db.session.commit()
        return ''

def _validar_consulta(consulta):
    query_validar_medico = db.session.query(Consulta).filter(
        Consulta.medico==consulta.medico, Consulta.data==consulta.data
    )
    if consulta.id is not None:
        query_validar_medico = query_validar_medico.filter(Consulta.id!=consulta.id)
    if query_validar_medico.count() > 0:
        return 'O médico já possui uma consulta marcada para a data solicitada.', 400

    query_validar_paciente = db.session.query(Consulta).filter(
        Consulta.paciente==consulta.paciente, Consulta.data==consulta.data
    )
    if consulta.id is not None:
        query_validar_paciente = query_validar_paciente.filter(Consulta.id!=consulta.id)
    if query_validar_paciente.count() > 0:
        return 'O paciente já possui uma consulta marcada para a data solicitada.', 400

    return None

# Forma de Pagamento
@app.route('/formapagamento', defaults={'id_forma_pagamento': None}, methods=['GET', 'POST'])
@app.route('/formapagamento/<int:id_forma_pagamento>', methods=['PUT', 'DELETE'])
def forma_pagamento(id_forma_pagamento):
    if request.method == 'GET':
        formas_pagamento = db.session.query(FormaPagamento).order_by(FormaPagamento.descricao).all()
        response = _to_result_list([forma_pagamento.to_dict() for forma_pagamento in formas_pagamento])
        return response
    elif request.method == 'POST':
        forma_pagamento = FormaPagamento()
        forma_pagamento.descricao = request.json['descricao']
        forma_pagamento.vista = request.json['vista'] == 'true'
        db.session.add(forma_pagamento)
        db.session.commit()
        return make_response(forma_pagamento.to_dict())
    elif request.method == 'PUT':
        forma_pagamento = db.session.query(FormaPagamento).get(id_forma_pagamento)
        forma_pagamento.descricao = request.json['descricao']
        forma_pagamento.vista = request.json['vista'] == 'true'
        db.session.commit()
        return make_response(forma_pagamento.to_dict())
    else:
        forma_pagamento = db.session.query(FormaPagamento).get(id_forma_pagamento)
        db.session.delete(forma_pagamento)
        db.session.commit()
        return ''

@app.route('/consulta/<int:id_consulta>/pagamento', methods=['POST'])
def registro_pagamentos_consulta(id_consulta):
    consulta = db.session.query(Consulta).get(id_consulta)
    forma_pagamento = db.session.query(FormaPagamento).get(request.json['idFormaPagamento'])
    valor_pagamento = request.json['valor'] / request.json['parcelas']
    data_pagamento = datetime.datetime.now()
    delta_proximo_pagamento = datetime.timedelta(days=30)
    for _ in range(request.json['parcelas']):
        pagamento = Pagamento()
        pagamento.consulta = consulta
        pagamento.forma_pagamento = forma_pagamento
        pagamento.valor = valor_pagamento
        pagamento.data_pagamento = data_pagamento
        db.session.add(pagamento)
        consulta.pagamentos.append(pagamento)

        data_pagamento += delta_proximo_pagamento
    db.session.commit()
    return make_response(consulta.to_dict())

@app.route('/consulta/<int:id_consulta>/exames', methods=['POST'])
def requisicao_exames(id_consulta):
    consulta = db.session.query(Consulta).get(id_consulta)
    requisicao_exames = RequisicaoExames()
    requisicao_exames.consulta = consulta
    requisicao_exames.descricao = request.json['descricao']
    requisicao_exames.data = datetime.datetime.now()
    db.session.add(requisicao_exames)
    consulta.requisicoes_exames.append(requisicao_exames)
    db.session.commit()
    return make_response(consulta.to_dict())

@app.route('/consulta/<int:id_consulta>/receita', methods=['POST'])
def receita(id_consulta):
    consulta = db.session.query(Consulta).get(id_consulta)
    receita_medica = ReceitaMedica()
    receita_medica.consulta = consulta
    receita_medica.descricao = request.json['descricao']
    receita_medica.data = datetime.datetime.now()
    db.session.add(receita_medica)
    consulta.receitas_medicas.append(receita_medica)
    db.session.commit()
    return make_response(consulta.to_dict())

def _to_result_list(results):
    return {'results': results}
