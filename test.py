import streamlit as st
from lxml import etree


def generate_school_records_xml(data):
    root = etree.Element("HistoricoEscolar")

    Aluno = etree.SubElement(root, "Aluno")
    etree.SubElement(Aluno, "Nome").text = data["nome"]
    etree.SubElement(Aluno, "CPF").text = data["cpf"]
    etree.SubElement(Aluno, "RG").text = data["rg"]
    etree.SubElement(Aluno, "OrgaoExpedidor").text = data["orgao_expedidor"]
    etree.SubElement(Aluno, "DataNascimento").text = data["data_nascimento"]
    etree.SubElement(Aluno, "Naturalidade").text = data["naturalidade"]

    Curso = etree.SubElement(root, "Curso")
    etree.SubElement(Curso, "Nome").text = data["nome_curso"]
    etree.SubElement(Curso, "Nivel").text = data["nivel_curso"]
    etree.SubElement(Curso, "Modalidade").text = data["modalidade_curso"]
    etree.SubElement(Curso, "CargaHoraria").text = str(data["carga_horaria"])
    etree.SubElement(Curso, "Habilitacao").text = data["habilitacao"]
    etree.SubElement(Curso, "DataInicio").text = data["data_inicio"]
    etree.SubElement(Curso, "DataFim").text = data["data_fim"]

    IesEmissora = etree.SubElement(root, "IesEmissora")
    etree.SubElement(IesEmissora, "Nome").text = data["ies_nome"]
    etree.SubElement(IesEmissora, "CodigoMEC").text = data["ies_codigo_mec"]
    etree.SubElement(IesEmissora, "CNPJ").text = data["ies_cnpj"]

    EnderecoIes = etree.SubElement(IesEmissora, "Endereco")
    etree.SubElement(EnderecoIes, "Logradouro").text = data["ies_logradouro"]
    etree.SubElement(EnderecoIes, "Numero").text = data["ies_numero"]
    etree.SubElement(EnderecoIes, "Complemento").text = data["ies_complemento"]
    etree.SubElement(EnderecoIes, "Bairro").text = data["ies_bairro"]
    etree.SubElement(EnderecoIes, "CEP").text = data["ies_cep"]
    etree.SubElement(EnderecoIes, "Cidade").text = data["ies_cidade"]
    etree.SubElement(EnderecoIes, "UF").text = data["ies_uf"]

    return etree.tostring(
        root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
    )


# Streamlit UI
st.title("School Records XML Generator")

st.header("Aluno")
data = {
    "nome": st.text_input("Nome"),
    "cpf": st.text_input("CPF"),
    "rg": st.text_input("RG"),
    "orgao_expedidor": st.text_input("Orgão Expedidor"),
    "data_nascimento": st.date_input("Data de Nascimento").isoformat(),
    "naturalidade": st.text_input("Naturalidade"),
    "nome_curso": st.text_input("Nome do Curso"),
    "nivel_curso": st.text_input("Nível do Curso"),
    "modalidade_curso": st.text_input("Modalidade do Curso"),
    "carga_horaria": st.number_input("Carga Horária", min_value=0),
    "habilitacao": st.text_input("Habilitação"),
    "data_inicio": st.date_input("Data de Início").isoformat(),
    "data_fim": st.date_input("Data de Fim").isoformat(),
    "ies_nome": st.text_input("Nome da IES"),
    "ies_codigo_mec": st.text_input("Código MEC da IES"),
    "ies_cnpj": st.text_input("CNPJ da IES"),
    "ies_logradouro": st.text_input("Logradouro"),
    "ies_numero": st.text_input("Número"),
    "ies_complemento": st.text_input("Complemento"),
    "ies_bairro": st.text_input("Bairro"),
    "ies_cep": st.text_input("CEP"),
    "ies_cidade": st.text_input("Cidade"),
    "ies_uf": st.text_input("UF"),
}

if st.button("Generate XML"):
    xml_str = generate_school_records_xml(data)
    st.code(xml_str.decode("utf-8"), language="xml")

    # Provide download link for the XML
    st.download_button(
        "Download XML",
        data=xml_str,
        file_name="school_records.xml",
        mime="application/xml",
    )
