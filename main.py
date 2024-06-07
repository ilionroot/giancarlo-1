import streamlit as st
from lxml import etree


def generate_xml(data):
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


st.title("Gerador de XML de Diploma Digital")

nome = st.text_input("Nome")
cpf = st.text_input("CPF")
rg = st.text_input("RG")
orgao_expedidor = st.text_input("Órgão Expedidor")
data_nascimento = st.date_input("Data de Nascimento")
naturalidade = st.text_input("Naturalidade")
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

assinante_nome = st.text_input("Nome do Assinante")
assinante_cargo = st.text_input("Cargo do Assinante")

numero_registro = st.text_input("Número de Registro")
data_registro = st.date_input("Data de Registro")
livro = st.text_input("Livro")
folha = st.text_input("Folha")

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
ies_registradora_cred_data = st.date_input("Data de Credenciamento da IES Registradora")
ies_registradora_cred_orgao = st.text_input(
    "Órgão de Credenciamento da IES Registradora"
)

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
    "ies_registradora_cred_data": ies_registradora_cred_data.strftime("%Y-%m-%d"),
    "ies_registradora_cred_orgao": ies_registradora_cred_orgao,
}

xml_output = generate_xml(data)

st.download_button(
    label="Download XML",
    data=xml_output,
    file_name="registro.xml",
    mime="application/xml",
)
