import streamlit as st
from lxml import etree


def generate_xml1(data):
    root = etree.Element(
        "Diploma",
        xmlns="http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        xmlns_ds="http://www.w3.org/2000/09/xmldsig#",
    )
    infDiploma = etree.SubElement(
        root,
        "infDiploma",
        versao="1.05",
        id="VDip12345678901234567890123456789012345678901234",
        ambiente="Produção",
    )

    DadosDiploma = etree.SubElement(
        infDiploma, "DadosDiploma", id="Dip12345678901234567890123456789012345678901234"
    )

    Diplomado = etree.SubElement(DadosDiploma, "Diplomado")
    etree.SubElement(Diplomado, "Nome").text = data["nome"]
    etree.SubElement(Diplomado, "CPF").text = data["cpf"]
    etree.SubElement(Diplomado, "RG").text = data["rg"]
    etree.SubElement(Diplomado, "OrgaoExpedidor").text = data["orgao_expedidor"]
    etree.SubElement(Diplomado, "DataNascimento").text = data["data_nascimento"]
    etree.SubElement(Diplomado, "Naturalidade").text = data["naturalidade"]

    etree.SubElement(DadosDiploma, "DataConclusao").text = data["data_conclusao"]

    DadosCurso = etree.SubElement(DadosDiploma, "DadosCurso")
    etree.SubElement(DadosCurso, "NomeCurso").text = data["nome_curso"]
    etree.SubElement(DadosCurso, "NivelCurso").text = data["nivel_curso"]
    etree.SubElement(DadosCurso, "ModalidadeCurso").text = data["modalidade_curso"]
    etree.SubElement(DadosCurso, "Cargahoraria").text = data["cargahoraria"]
    etree.SubElement(DadosCurso, "Habilitacao").text = data["habilitacao"]
    etree.SubElement(DadosCurso, "DataInicio").text = data["data_inicio"]
    etree.SubElement(DadosCurso, "DataFim").text = data["data_fim"]

    IesEmissora = etree.SubElement(DadosDiploma, "IesEmissora")
    etree.SubElement(IesEmissora, "Nome").text = data["ies_nome"]
    etree.SubElement(IesEmissora, "CodigoMEC").text = data["ies_codigo_mec"]
    etree.SubElement(IesEmissora, "CNPJ").text = data["ies_cnpj"]

    Endereco = etree.SubElement(IesEmissora, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data["ies_logradouro"]
    etree.SubElement(Endereco, "Numero").text = data["ies_numero"]
    etree.SubElement(Endereco, "Complemento").text = data["ies_complemento"]
    etree.SubElement(Endereco, "Bairro").text = data["ies_bairro"]
    etree.SubElement(Endereco, "CEP").text = data["ies_cep"]
    etree.SubElement(Endereco, "Cidade").text = data["ies_cidade"]
    etree.SubElement(Endereco, "UF").text = data["ies_uf"]

    Credenciamento = etree.SubElement(IesEmissora, "Credenciamento")
    etree.SubElement(Credenciamento, "Numero").text = data["ies_cred_numero"]
    etree.SubElement(Credenciamento, "Data").text = data["ies_cred_data"]
    etree.SubElement(Credenciamento, "Orgao").text = data["ies_cred_orgao"]

    Assinantes = etree.SubElement(DadosDiploma, "Assinantes")
    Assinante = etree.SubElement(Assinantes, "Assinante")
    etree.SubElement(Assinante, "Nome").text = data["assinante_nome"]
    etree.SubElement(Assinante, "Cargo").text = data["assinante_cargo"]

    DadosRegistro = etree.SubElement(infDiploma, "DadosRegistro")
    etree.SubElement(DadosRegistro, "NumeroRegistro").text = data["numero_registro"]
    etree.SubElement(DadosRegistro, "DataRegistro").text = data["data_registro"]
    etree.SubElement(DadosRegistro, "Livro").text = data["livro"]
    etree.SubElement(DadosRegistro, "Folha").text = data["folha"]

    IesRegistradora = etree.SubElement(DadosRegistro, "IesRegistradora")
    etree.SubElement(IesRegistradora, "Nome").text = data["ies_registradora_nome"]
    etree.SubElement(IesRegistradora, "CodigoMEC").text = data[
        "ies_registradora_codigo_mec"
    ]
    etree.SubElement(IesRegistradora, "CNPJ").text = data["ies_registradora_cnpj"]

    EnderecoReg = etree.SubElement(IesRegistradora, "Endereco")
    etree.SubElement(EnderecoReg, "Logradouro").text = data[
        "ies_registradora_logradouro"
    ]
    etree.SubElement(EnderecoReg, "Numero").text = data["ies_registradora_numero"]
    etree.SubElement(EnderecoReg, "Complemento").text = data[
        "ies_registradora_complemento"
    ]
    etree.SubElement(EnderecoReg, "Bairro").text = data["ies_registradora_bairro"]
    etree.SubElement(EnderecoReg, "CEP").text = data["ies_registradora_cep"]
    etree.SubElement(EnderecoReg, "Cidade").text = data["ies_registradora_cidade"]
    etree.SubElement(EnderecoReg, "UF").text = data["ies_registradora_uf"]

    CredenciamentoReg = etree.SubElement(IesRegistradora, "Credenciamento")
    etree.SubElement(CredenciamentoReg, "Numero").text = data[
        "ies_registradora_cred_numero"
    ]
    etree.SubElement(CredenciamentoReg, "Data").text = data[
        "ies_registradora_cred_data"
    ]
    etree.SubElement(CredenciamentoReg, "Orgao").text = data[
        "ies_registradora_cred_orgao"
    ]

    return etree.tostring(
        root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
    )


def generate_school_records_xml(dados):
    # Cria o elemento raiz
    root = etree.Element(
        "{http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd}infHistoricoEscolar",
        versao="1.05",
        ambiente="Produção",
    )

    # Adiciona os dados do aluno
    aluno = etree.SubElement(root, "Aluno")
    etree.SubElement(aluno, "Nome").text = dados["nome_aluno"]
    etree.SubElement(aluno, "CPF").text = dados["cpf_aluno"]
    etree.SubElement(aluno, "RG").text = dados["rg_aluno"]
    etree.SubElement(aluno, "OrgaoExpedidor").text = dados["orgao_expedidor"]
    etree.SubElement(aluno, "DataNascimento").text = dados["data_nascimento"]
    etree.SubElement(aluno, "Naturalidade").text = dados["naturalidade"]

    # Adiciona os dados do curso
    dados_curso = etree.SubElement(root, "DadosCurso")
    etree.SubElement(dados_curso, "NomeCurso").text = dados["nome_curso"]
    etree.SubElement(dados_curso, "CodigoCursoEMEC").text = dados["codigo_curso_emec"]
    # Adicionar outras informações do curso, como habilitações, autorizações, etc.

    # Adiciona os dados da IES emissora
    ies_emissora = etree.SubElement(root, "IesEmissora")
    etree.SubElement(ies_emissora, "Nome").text = dados["nome_ies"]
    etree.SubElement(ies_emissora, "CodigoMEC").text = dados["codigo_mec"]
    etree.SubElement(ies_emissora, "CNPJ").text = dados["cnpj_ies"]
    # Adicionar outras informações da IES, como endereço, credenciamento, etc.

    # Adiciona os dados do histórico escolar
    historico_escolar = etree.SubElement(root, "HistoricoEscolar")
    etree.SubElement(historico_escolar, "CodigoCurriculo").text = dados[
        "codigo_curriculo"
    ]
    etree.SubElement(historico_escolar, "DataEmissaoHistorico").text = dados[
        "data_emissao_historico"
    ]
    etree.SubElement(historico_escolar, "HoraEmissaoHistorico").text = dados[
        "hora_emissao_historico"
    ]
    etree.SubElement(historico_escolar, "SituacaoAtualDiscente").text = dados[
        "situacao_atual_discente"
    ]
    etree.SubElement(historico_escolar, "CargaHorariaCursoIntegralizada").text = dados[
        "carga_horaria_integralizada"
    ]
    etree.SubElement(historico_escolar, "CargaHorariaCurso").text = dados[
        "carga_horaria_curso"
    ]

    ingresso_curso = etree.SubElement(historico_escolar, "IngressoCurso")
    etree.SubElement(ingresso_curso, "Data").text = dados["data_ingresso_curso"]
    etree.SubElement(ingresso_curso, "FormaAcesso").text = dados["forma_acesso_curso"]

    # Adiciona as disciplinas cursadas
    elementos_historico = etree.SubElement(historico_escolar, "ElementosHistorico")
    for disciplina in dados["disciplinas"]:
        disciplina_elem = etree.SubElement(elementos_historico, "Disciplina")
        etree.SubElement(disciplina_elem, "CodigoDisciplina").text = disciplina[
            "codigo"
        ]
        etree.SubElement(disciplina_elem, "NomeDisciplina").text = disciplina["nome"]
        etree.SubElement(disciplina_elem, "PeriodoLetivo").text = disciplina[
            "periodo_letivo"
        ]
        carga_horaria_elem = etree.SubElement(disciplina_elem, "CargaHoraria")
        etree.SubElement(carga_horaria_elem, "Etiqueta").text = disciplina[
            "carga_horaria"
        ]["etiqueta"]
        etree.SubElement(carga_horaria_elem, "Valor").text = str(
            disciplina["carga_horaria"]["valor"]
        )
        etree.SubElement(disciplina_elem, "Nota").text = str(disciplina["nota"])
        situacao_elem = etree.SubElement(
            disciplina_elem, "Aprovado" if disciplina["aprovado"] else "Reprovado"
        )
        if disciplina["aprovado"]:
            etree.SubElement(situacao_elem, "FormaIntegralizacao").text = disciplina[
                "forma_integralizacao"
            ]

    # Adiciona os dados de segurança do histórico
    seguranca_historico = etree.SubElement(root, "SegurancaHistorico")
    etree.SubElement(seguranca_historico, "CodigoValidacao").text = dados[
        "codigo_validacao"
    ]

    # Converte o elemento raiz para uma string XML
    xml_output = etree.tostring(
        root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
    )

    return xml_output


st.set_page_config(page_title="XML Generator", layout="wide")

tabs = st.tabs(["Diploma Digital", "Histórico Escolar"])

with tabs[0]:
    st.title("Gerador de XML de Diploma Digital")

    st.header("Dados do Aluno")
    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    rg = st.text_input("RG")
    orgao_expedidor = st.text_input("Órgão Expedidor")
    data_nascimento = st.date_input("Data de Nascimento")
    naturalidade = st.text_input("Naturalidade")

    st.header("Dados do Curso")
    data_conclusao = st.date_input("Data de Conclusão")
    nome_curso = st.text_input("Nome do Curso")
    nivel_curso = st.selectbox(
        "Nível do Curso", ["Graduação", "Pós-Graduação", "Mestrado", "Doutorado"]
    )
    modalidade_curso = st.selectbox(
        "Modalidade do Curso", ["Presencial", "EaD", "Semipresencial"]
    )
    cargahoraria = st.number_input("Carga Horária", step=1)
    habilitacao = st.text_input("Habilitação")
    data_inicio = st.date_input("Data de Início")
    data_fim = st.date_input("Data de Fim")

    st.header("Dados da IES Emissora")
    ies_nome = st.text_input("Nome da IES Emissora")
    ies_codigo_mec = st.text_input("Código MEC da IES Emissora")
    ies_cnpj = st.text_input("CNPJ da IES Emissora")
    ies_logradouro = st.text_input("Logradouro da IES Emissora")
    ies_numero = st.text_input("Número da IES Emissora")
    ies_complemento = st.text_input("Complemento da IES Emissora")
    ies_bairro = st.text_input("Bairro da IES Emissora")
    ies_cep = st.text_input("CEP da IES Emissora")
    ies_cidade = st.text_input("Cidade da IES Emissora")
    ies_uf = st.text_input("UF da IES Emissora")
    ies_cred_numero = st.text_input("Número de Credenciamento da IES Emissora")
    ies_cred_data = st.date_input("Data de Credenciamento da IES Emissora")
    ies_cred_orgao = st.text_input("Órgão de Credenciamento da IES Emissora")

    st.header("Dados do Assinante")
    assinante_nome = st.text_input("Nome do Assinante")
    assinante_cargo = st.text_input("Cargo do Assinante")

    st.header("Dados do Registro")
    numero_registro = st.text_input("Número de Registro")
    data_registro = st.date_input("Data de Registro")
    livro = st.text_input("Livro")
    folha = st.text_input("Folha")

    st.header("Dados da IES Registradora")
    ies_registradora_nome = st.text_input("Nome da IES Registradora")
    ies_registradora_codigo_mec = st.text_input("Código MEC da IES Registradora")
    ies_registradora_cnpj = st.text_input("CNPJ da IES Registradora")
    ies_registradora_logradouro = st.text_input("Logradouro da IES Registradora")
    ies_registradora_numero = st.text_input("Número da IES Registradora")
    ies_registradora_complemento = st.text_input("Complemento da IES Registradora")
    ies_registradora_bairro = st.text_input("Bairro da IES Registradora")
    ies_registradora_cep = st.text_input("CEP da IES Registradora")
    ies_registradora_cidade = st.text_input("Cidade da IES Registradora")
    ies_registradora_uf = st.text_input("UF da IES Registradora")
    ies_registradora_cred_numero = st.text_input(
        "Número de Credenciamento da IES Registradora"
    )
    ies_registradora_cred_data = st.date_input(
        "Data de Credenciamento da IES Registradora"
    )
    ies_registradora_cred_orgao = st.text_input(
        "Órgão de Credenciamento da IES Registradora"
    )

    submitted = st.button("Gerar XML")

    if submitted:
        data = {
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "orgao_expedidor": orgao_expedidor,
            "data_nascimento": data_nascimento.strftime("%Y-%m-%d"),
            "naturalidade": naturalidade,
            "data_conclusao": data_conclusao.strftime("%Y-%m-%d"),
            "nome_curso": nome_curso,
            "nivel_curso": nivel_curso,
            "modalidade_curso": modalidade_curso,
            "cargahoraria": str(cargahoraria),
            "habilitacao": habilitacao,
            "data_inicio": data_inicio.strftime("%Y-%m-%d"),
            "data_fim": data_fim.strftime("%Y-%m-%d"),
            "ies_nome": ies_nome,
            "ies_codigo_mec": ies_codigo_mec,
            "ies_cnpj": ies_cnpj,
            "ies_logradouro": ies_logradouro,
            "ies_numero": ies_numero,
            "ies_complemento": ies_complemento,
            "ies_bairro": ies_bairro,
            "ies_cep": ies_cep,
            "ies_cidade": ies_cidade,
            "ies_uf": ies_uf,
            "ies_cred_numero": ies_cred_numero,
            "ies_cred_data": ies_cred_data.strftime("%Y-%m-%d"),
            "ies_cred_orgao": ies_cred_orgao,
            "assinante_nome": assinante_nome,
            "assinante_cargo": assinante_cargo,
            "numero_registro": numero_registro,
            "data_registro": data_registro.strftime("%Y-%m-%d"),
            "livro": livro,
            "folha": folha,
            "ies_registradora_nome": ies_registradora_nome,
            "ies_registradora_codigo_mec": ies_registradora_codigo_mec,
            "ies_registradora_cnpj": ies_registradora_cnpj,
            "ies_registradora_logradouro": ies_registradora_logradouro,
            "ies_registradora_numero": ies_registradora_numero,
            "ies_registradora_complemento": ies_registradora_complemento,
            "ies_registradora_bairro": ies_registradora_bairro,
            "ies_registradora_cep": ies_registradora_cep,
            "ies_registradora_cidade": ies_registradora_cidade,
            "ies_registradora_uf": ies_registradora_uf,
            "ies_registradora_cred_numero": ies_registradora_cred_numero,
            "ies_registradora_cred_data": ies_registradora_cred_data.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_cred_orgao": ies_registradora_cred_orgao,
        }

        xml_output = generate_xml1(data)

        st.code(xml_output.decode("utf-8"), language="xml")

        st.download_button(
            label="Baixar",
            data=xml_output,
            file_name="registro.xml",
            mime="application/xml",
        )

with tabs[1]:
    st.title("Gerador de XML de Registros Escolares")

    st.header("Dados do Aluno")
    nome_aluno = st.text_input("Nome do Aluno", key="nome_aluno")
    cpf_aluno = st.text_input("CPF do Aluno", key="cpf_aluno")
    rg_aluno = st.text_input("RG do Aluno", key="rg_aluno")
    orgao_expedidor = st.text_input("Órgão Expedidor", key="orgao_expedidor")
    data_nascimento = st.date_input("Data de Nascimento", key="data_nascimento")
    naturalidade = st.text_input("Naturalidade", key="naturalidade")

    st.header("Dados do Curso")
    nome_curso = st.text_input("Nome do Curso", key="nome_curso")
    codigo_curso_emec = st.text_input(
        "Código do Curso no e-MEC", key="codigo_curso_emec"
    )

    st.header("Dados da IES Emissora")
    nome_ies = st.text_input("Nome da IES", key="nome_ies")
    codigo_mec = st.text_input("Código MEC da IES", key="codigo_mec")
    cnpj_ies = st.text_input("CNPJ da IES", key="cnpj_ies")

    st.header("Dados do Histórico Escolar")
    codigo_curriculo = st.text_input("Código do Currículo", key="codigo_curriculo")
    data_emissao_historico = st.date_input(
        "Data de Emissão do Histórico", key="data_emissao_historico"
    )
    hora_emissao_historico = st.time_input(
        "Hora de Emissão do Histórico", value=None, key="hora_emissao_historico"
    )
    situacao_atual_discente = st.text_input(
        "Situação Atual do Discente", key="situacao_atual_discente"
    )
    carga_horaria_integralizada = st.number_input(
        "Carga Horária Integralizada", step=1, key="carga_horaria_integralizada"
    )
    carga_horaria_curso = st.number_input(
        "Carga Horária Total do Curso", step=1, key="carga_horaria_curso"
    )
    data_ingresso_curso = st.date_input(
        "Data de Ingresso no Curso", key="data_ingresso_curso"
    )
    forma_acesso_curso = st.text_input(
        "Forma de Acesso ao Curso", key="forma_acesso_curso"
    )

    disciplinas = []
    adicionar_disciplina = st.checkbox(
        "Adicionar Disciplina", key="adicionar_disciplina"
    )
    if adicionar_disciplina:
        disciplina = {
            "codigo": st.text_input("Código da Disciplina", key="codigo_disciplina"),
            "nome": st.text_input("Nome da Disciplina", key="nome_disciplina"),
            "periodo_letivo": st.text_input("Período Letivo", key="periodo_letivo"),
            "carga_horaria": {
                "etiqueta": st.text_input(
                    "Etiqueta da Carga Horária", key="etiqueta_carga_horaria"
                ),
                "valor": st.number_input(
                    "Valor da Carga Horária", step=1, key="valor_carga_horaria"
                ),
            },
            "nota": st.number_input("Nota", step=0.1, key="nota"),
            "aprovado": st.checkbox("Aprovado", key="aprovado"),
            "forma_integralizacao": st.text_input(
                "Forma de Integralização",
                value="Cursado" if st.session_state.get("aprovado") else "",
                key="forma_integralizacao",
            ),
        }
        disciplinas.append(disciplina)
        adicionar_mais_disciplinas = st.checkbox(
            "Adicionar Mais Disciplinas", key="adicionar_mais_disciplinas"
        )
        while adicionar_mais_disciplinas:
            disciplina = {
                "codigo": st.text_input(
                    "Código da Disciplina", key=f"codigo_disciplina_{len(disciplinas)}"
                ),
                "nome": st.text_input(
                    "Nome da Disciplina", key=f"nome_disciplina_{len(disciplinas)}"
                ),
                "periodo_letivo": st.text_input(
                    "Período Letivo", key=f"periodo_letivo_{len(disciplinas)}"
                ),
                "carga_horaria": {
                    "etiqueta": st.text_input(
                        "Etiqueta da Carga Horária",
                        key=f"etiqueta_carga_horaria_{len(disciplinas)}",
                    ),
                    "valor": st.number_input(
                        "Valor da Carga Horária",
                        step=1,
                        key=f"valor_carga_horaria_{len(disciplinas)}",
                    ),
                },
                "nota": st.number_input(
                    "Nota", step=0.1, key=f"nota_{len(disciplinas)}"
                ),
                "aprovado": st.checkbox("Aprovado", key=f"aprovado_{len(disciplinas)}"),
                "forma_integralizacao": st.text_input(
                    "Forma de Integralização",
                    value=(
                        "Cursado"
                        if st.session_state.get(f"aprovado_{len(disciplinas)}")
                        else ""
                    ),
                    key=f"forma_integralizacao_{len(disciplinas)}",
                ),
            }
            disciplinas.append(disciplina)
            adicionar_mais_disciplinas = st.checkbox(
                "Adicionar Mais Disciplinas",
                key=f"adicionar_mais_disciplinas_{len(disciplinas)}",
            )

    codigo_validacao = st.text_input(
        "Código de Validação do Histórico", key="codigo_validacao"
    )

    if st.button("Gerar XML", key="gerar_xml"):
        dados = {
            "nome_aluno": nome_aluno,
            "cpf_aluno": cpf_aluno,
            "rg_aluno": rg_aluno,
            "orgao_expedidor": orgao_expedidor,
            "data_nascimento": data_nascimento.isoformat(),
            "naturalidade": naturalidade,
            "nome_curso": nome_curso,
            "codigo_curso_emec": codigo_curso_emec,
            "nome_ies": nome_ies,
            "codigo_mec": codigo_mec,
            "cnpj_ies": cnpj_ies,
            "codigo_curriculo": codigo_curriculo,
            "data_emissao_historico": data_emissao_historico.isoformat(),
            "hora_emissao_historico": hora_emissao_historico.strftime("%H:%M:%S"),
            "situacao_atual_discente": situacao_atual_discente,
            "carga_horaria_integralizada": str(carga_horaria_integralizada),
            "carga_horaria_curso": str(carga_horaria_curso),
            "data_ingresso_curso": data_ingresso_curso.isoformat(),
            "forma_acesso_curso": forma_acesso_curso,
            "disciplinas": disciplinas,
            "codigo_validacao": codigo_validacao,
        }

        xml_output = generate_school_records_xml(dados)
        st.download_button(
            label="Baixar XML",
            data=xml_output,
            file_name="historico_escolar.xml",
            mime="application/xml",
        )
