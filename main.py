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
        id="VDip11111111111111111111111111111111111111111111",
        ambiente="Produção",
    )

    DadosDiploma = etree.SubElement(
        infDiploma, "DadosDiploma", id="Dip11111111111111111111111111111111111111111111"
    )

    Diplomado = etree.SubElement(DadosDiploma, "Diplomado")
    etree.SubElement(Diplomado, "ID").text = (
        "Dip11111111111111111111111111111111111111111111"
    )
    etree.SubElement(Diplomado, "Nome").text = data["nome"]
    etree.SubElement(Diplomado, "NomeSocial").text = data["nome_social"]
    etree.SubElement(Diplomado, "Sexo").text = data["sexo"]
    etree.SubElement(Diplomado, "Nacionalidade").text = data["nacionalidade"]
    Naturalidade = etree.SubElement(Diplomado, "Naturalidade")
    etree.SubElement(Naturalidade, "NomeMunicipioEstrangeiro").text = data[
        "nome_municipio_estrangeiro"
    ]
    etree.SubElement(Diplomado, "CPF").text = data["cpf"]
    RG = etree.SubElement(Diplomado, "RG")
    etree.SubElement(RG, "Numero").text = data["rg_numero"]
    etree.SubElement(RG, "OrgaoExpedidor").text = data["rg_orgao_expedidor"]
    etree.SubElement(RG, "UF").text = data["rg_uf"]
    etree.SubElement(Diplomado, "DataNascimento").text = data["data_nascimento"]

    etree.SubElement(DadosDiploma, "DataConclusao").text = data["data_conclusao"]

    DadosCurso = etree.SubElement(DadosDiploma, "DadosCurso")
    etree.SubElement(DadosCurso, "NomeCurso").text = data["nome_curso"]
    etree.SubElement(DadosCurso, "CodigoCursoEMEC").text = data["codigo_curso_emec"]
    Habilitacao1 = etree.SubElement(DadosCurso, "Habilitacao")
    etree.SubElement(Habilitacao1, "NomeHabilitacao").text = data["nome_habilitacao_1"]
    etree.SubElement(Habilitacao1, "DataHabilitacao").text = data["data_habilitacao_1"]
    Habilitacao2 = etree.SubElement(DadosCurso, "Habilitacao")
    etree.SubElement(Habilitacao2, "NomeHabilitacao").text = data["nome_habilitacao_2"]
    etree.SubElement(Habilitacao2, "DataHabilitacao").text = data["data_habilitacao_2"]
    etree.SubElement(DadosCurso, "Modalidade").text = data["modalidade_curso"]
    TituloConferido = etree.SubElement(DadosCurso, "TituloConferido")
    etree.SubElement(TituloConferido, "Titulo").text = data["titulo_conferido"]
    etree.SubElement(DadosCurso, "GrauConferido").text = data["grau_conferido"]
    etree.SubElement(DadosCurso, "Enfase").text = data["enfase_1"]
    etree.SubElement(DadosCurso, "Enfase").text = data["enfase_2"]
    EnderecoCurso = etree.SubElement(DadosCurso, "EnderecoCurso")
    etree.SubElement(EnderecoCurso, "Logradouro").text = data[
        "endereco_curso_logradouro"
    ]
    etree.SubElement(EnderecoCurso, "Numero").text = data["endereco_curso_numero"]
    etree.SubElement(EnderecoCurso, "Complemento").text = data[
        "endereco_curso_complemento"
    ]
    etree.SubElement(EnderecoCurso, "Bairro").text = data["endereco_curso_bairro"]
    etree.SubElement(EnderecoCurso, "CodigoMunicipio").text = data[
        "endereco_curso_codigo_municipio"
    ]
    etree.SubElement(EnderecoCurso, "NomeMunicipio").text = data[
        "endereco_curso_nome_municipio"
    ]
    etree.SubElement(EnderecoCurso, "UF").text = data["endereco_curso_uf"]
    etree.SubElement(EnderecoCurso, "CEP").text = data["endereco_curso_cep"]
    Polo = etree.SubElement(DadosCurso, "Polo")
    etree.SubElement(Polo, "Nome").text = data["polo_nome"]
    Endereco = etree.SubElement(Polo, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data["polo_endereco_logradouro"]
    etree.SubElement(Endereco, "Bairro").text = data["polo_endereco_bairro"]
    etree.SubElement(Endereco, "NomeMunicipioEstrangeiro").text = data[
        "polo_endereco_nome_municipio_estrangeiro"
    ]
    etree.SubElement(Endereco, "CEP").text = data["polo_endereco_cep"]
    etree.SubElement(Polo, "CodigoEMEC").text = data["polo_codigo_emec"]
    Autorizacao = etree.SubElement(DadosCurso, "Autorizacao")
    InformacoesTramitacaoEMEC = etree.SubElement(
        Autorizacao, "InformacoesTramitacaoEMEC"
    )
    etree.SubElement(InformacoesTramitacaoEMEC, "NumeroProcesso").text = data[
        "autorizacao_numero_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "TipoProcesso").text = data[
        "autorizacao_tipo_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataCadastro").text = data[
        "autorizacao_data_cadastro"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataProtocolo").text = data[
        "autorizacao_data_protocolo"
    ]
    Reconhecimento = etree.SubElement(DadosCurso, "Reconhecimento")
    etree.SubElement(Reconhecimento, "Tipo").text = data["reconhecimento_tipo"]
    etree.SubElement(Reconhecimento, "Numero").text = data["reconhecimento_numero"]
    etree.SubElement(Reconhecimento, "Data").text = data["reconhecimento_data"]
    etree.SubElement(Reconhecimento, "VeiculoPublicacao").text = data[
        "reconhecimento_veiculo_publicacao"
    ]
    etree.SubElement(Reconhecimento, "DataPublicacao").text = data[
        "reconhecimento_data_publicacao"
    ]
    etree.SubElement(Reconhecimento, "SecaoPublicacao").text = data[
        "reconhecimento_secao_publicacao"
    ]
    etree.SubElement(Reconhecimento, "PaginaPublicacao").text = data[
        "reconhecimento_pagina_publicacao"
    ]
    etree.SubElement(Reconhecimento, "NumeroDOU").text = data[
        "reconhecimento_numero_dou"
    ]
    RenovacaoReconhecimento = etree.SubElement(DadosCurso, "RenovacaoReconhecimento")
    etree.SubElement(RenovacaoReconhecimento, "Tipo").text = data[
        "renovacao_reconhecimento_tipo"
    ]
    etree.SubElement(RenovacaoReconhecimento, "Numero").text = data[
        "renovacao_reconhecimento_numero"
    ]
    etree.SubElement(RenovacaoReconhecimento, "Data").text = data[
        "renovacao_reconhecimento_data"
    ]
    etree.SubElement(RenovacaoReconhecimento, "VeiculoPublicacao").text = data[
        "renovacao_reconhecimento_veiculo_publicacao"
    ]
    etree.SubElement(RenovacaoReconhecimento, "DataPublicacao").text = data[
        "renovacao_reconhecimento_data_publicacao"
    ]
    etree.SubElement(RenovacaoReconhecimento, "SecaoPublicacao").text = data[
        "renovacao_reconhecimento_secao_publicacao"
    ]
    etree.SubElement(RenovacaoReconhecimento, "PaginaPublicacao").text = data[
        "renovacao_reconhecimento_pagina_publicacao"
    ]
    etree.SubElement(RenovacaoReconhecimento, "NumeroDOU").text = data[
        "renovacao_reconhecimento_numero_dou"
    ]

    DadosIesOriginalCursoPTA = etree.SubElement(
        DadosDiploma, "DadosIesOriginalCursoPTA"
    )
    etree.SubElement(DadosIesOriginalCursoPTA, "Nome").text = data[
        "dados_ies_original_curso_pta_nome"
    ]
    etree.SubElement(DadosIesOriginalCursoPTA, "CodigoMEC_Indisponivel")
    etree.SubElement(DadosIesOriginalCursoPTA, "CNPJ").text = data[
        "dados_ies_original_curso_pta_cnpj"
    ]
    Endereco = etree.SubElement(DadosIesOriginalCursoPTA, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data[
        "dados_ies_original_curso_pta_endereco_logradouro"
    ]
    etree.SubElement(Endereco, "Numero").text = data[
        "dados_ies_original_curso_pta_endereco_numero"
    ]
    etree.SubElement(Endereco, "Complemento").text = data[
        "dados_ies_original_curso_pta_endereco_complemento"
    ]
    etree.SubElement(Endereco, "Bairro").text = data[
        "dados_ies_original_curso_pta_endereco_bairro"
    ]
    etree.SubElement(Endereco, "CodigoMunicipio").text = data[
        "dados_ies_original_curso_pta_endereco_codigo_municipio"
    ]
    etree.SubElement(Endereco, "NomeMunicipio").text = data[
        "dados_ies_original_curso_pta_endereco_nome_municipio"
    ]
    etree.SubElement(Endereco, "UF").text = data[
        "dados_ies_original_curso_pta_endereco_uf"
    ]
    etree.SubElement(Endereco, "CEP").text = data[
        "dados_ies_original_curso_pta_endereco_cep"
    ]
    Descredenciamento = etree.SubElement(DadosIesOriginalCursoPTA, "Descredenciamento")
    etree.SubElement(Descredenciamento, "Tipo").text = data[
        "dados_ies_original_curso_pta_descredenciamento_tipo"
    ]
    etree.SubElement(Descredenciamento, "Numero").text = data[
        "dados_ies_original_curso_pta_descredenciamento_numero"
    ]
    etree.SubElement(Descredenciamento, "Data").text = data[
        "dados_ies_original_curso_pta_descredenciamento_data"
    ]
    etree.SubElement(Descredenciamento, "VeiculoPublicacao").text = data[
        "dados_ies_original_curso_pta_descredenciamento_veiculo_publicacao"
    ]
    etree.SubElement(Descredenciamento, "DataPublicacao").text = data[
        "dados_ies_original_curso_pta_descredenciamento_data_publicacao"
    ]
    etree.SubElement(Descredenciamento, "SecaoPublicacao").text = data[
        "dados_ies_original_curso_pta_descredenciamento_secao_publicacao"
    ]
    etree.SubElement(Descredenciamento, "PaginaPublicacao").text = data[
        "dados_ies_original_curso_pta_descredenciamento_pagina_publicacao"
    ]
    etree.SubElement(Descredenciamento, "NumeroDOU").text = data[
        "dados_ies_original_curso_pta_descredenciamento_numero_dou"
    ]

    IesEmissora = etree.SubElement(DadosDiploma, "IesEmissora")
    etree.SubElement(IesEmissora, "Nome").text = data["ies_emissora_nome"]
    etree.SubElement(IesEmissora, "CodigoMEC").text = data["ies_emissora_codigo_mec"]
    etree.SubElement(IesEmissora, "CNPJ").text = data["ies_emissora_cnpj"]
    Endereco = etree.SubElement(IesEmissora, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data[
        "ies_emissora_endereco_logradouro"
    ]
    etree.SubElement(Endereco, "Numero").text = data["ies_emissora_endereco_numero"]
    etree.SubElement(Endereco, "Complemento").text = data[
        "ies_emissora_endereco_complemento"
    ]
    etree.SubElement(Endereco, "Bairro").text = data["ies_emissora_endereco_bairro"]
    etree.SubElement(Endereco, "NomeMunicipioEstrangeiro").text = data[
        "ies_emissora_endereco_nome_municipio_estrangeiro"
    ]
    etree.SubElement(Endereco, "CEP").text = data["ies_emissora_endereco_cep"]
    Credenciamento = etree.SubElement(IesEmissora, "Credenciamento")
    InformacoesTramitacaoEMEC = etree.SubElement(
        Credenciamento, "InformacoesTramitacaoEMEC"
    )
    etree.SubElement(InformacoesTramitacaoEMEC, "NumeroProcesso").text = data[
        "ies_emissora_credenciamento_numero_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "TipoProcesso").text = data[
        "ies_emissora_credenciamento_tipo_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataCadastro").text = data[
        "ies_emissora_credenciamento_data_cadastro"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataProtocolo").text = data[
        "ies_emissora_credenciamento_data_protocolo"
    ]
    Recredenciamento = etree.SubElement(IesEmissora, "Recredenciamento")
    InformacoesTramitacaoEMEC = etree.SubElement(
        Recredenciamento, "InformacoesTramitacaoEMEC"
    )
    etree.SubElement(InformacoesTramitacaoEMEC, "NumeroProcesso").text = data[
        "ies_emissora_recredenciamento_numero_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "TipoProcesso").text = data[
        "ies_emissora_recredenciamento_tipo_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataCadastro").text = data[
        "ies_emissora_recredenciamento_data_cadastro"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataProtocolo").text = data[
        "ies_emissora_recredenciamento_data_protocolo"
    ]
    RenovacaoDeRecredenciamento = etree.SubElement(
        IesEmissora, "RenovacaoDeRecredenciamento"
    )
    etree.SubElement(RenovacaoDeRecredenciamento, "Tipo").text = data[
        "ies_emissora_renovacao_recredenciamento_tipo"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "Numero").text = data[
        "ies_emissora_renovacao_recredenciamento_numero"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "Data").text = data[
        "ies_emissora_renovacao_recredenciamento_data"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "VeiculoPublicacao").text = data[
        "ies_emissora_renovacao_recredenciamento_veiculo_publicacao"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "DataPublicacao").text = data[
        "ies_emissora_renovacao_recredenciamento_data_publicacao"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "SecaoPublicacao").text = data[
        "ies_emissora_renovacao_recredenciamento_secao_publicacao"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "PaginaPublicacao").text = data[
        "ies_emissora_renovacao_recredenciamento_pagina_publicacao"
    ]
    etree.SubElement(RenovacaoDeRecredenciamento, "NumeroDOU").text = data[
        "ies_emissora_renovacao_recredenciamento_numero_dou"
    ]
    Mantenedora = etree.SubElement(IesEmissora, "Mantenedora")
    etree.SubElement(Mantenedora, "RazaoSocial").text = data[
        "ies_emissora_mantenedora_razao_social"
    ]
    etree.SubElement(Mantenedora, "CNPJ").text = data["ies_emissora_mantenedora_cnpj"]
    Endereco = etree.SubElement(Mantenedora, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data[
        "ies_emissora_mantenedora_endereco_logradouro"
    ]
    etree.SubElement(Endereco, "Bairro").text = data[
        "ies_emissora_mantenedora_endereco_bairro"
    ]
    etree.SubElement(Endereco, "CodigoMunicipio").text = data[
        "ies_emissora_mantenedora_endereco_codigo_municipio"
    ]
    etree.SubElement(Endereco, "NomeMunicipio").text = data[
        "ies_emissora_mantenedora_endereco_nome_municipio"
    ]
    etree.SubElement(Endereco, "UF").text = data["ies_emissora_mantenedora_endereco_uf"]
    etree.SubElement(Endereco, "CEP").text = data[
        "ies_emissora_mantenedora_endereco_cep"
    ]

    Assinantes = etree.SubElement(DadosDiploma, "Assinantes")
    Assinante1 = etree.SubElement(Assinantes, "Assinante")
    etree.SubElement(Assinante1, "CPF").text = data["assinante_1_cpf"]
    etree.SubElement(Assinante1, "Cargo").text = data["assinante_1_cargo"]
    Assinante2 = etree.SubElement(Assinantes, "Assinante")
    etree.SubElement(Assinante2, "CPF").text = data["assinante_2_cpf"]
    etree.SubElement(Assinante2, "Cargo").text = data["assinante_2_cargo"]

    DadosRegistro = etree.SubElement(
        infDiploma,
        "DadosRegistro",
        id="RDip11111111111111111111111111111111111111111111",
    )

    IesRegistradora = etree.SubElement(DadosRegistro, "IesRegistradora")
    etree.SubElement(IesRegistradora, "Nome").text = data["ies_registradora_nome"]
    etree.SubElement(IesRegistradora, "CodigoMEC").text = data[
        "ies_registradora_codigo_mec"
    ]
    etree.SubElement(IesRegistradora, "CNPJ").text = data["ies_registradora_cnpj"]
    Endereco = etree.SubElement(IesRegistradora, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data[
        "ies_registradora_endereco_logradouro"
    ]
    etree.SubElement(Endereco, "Numero").text = data["ies_registradora_endereco_numero"]
    etree.SubElement(Endereco, "Complemento").text = data[
        "ies_registradora_endereco_complemento"
    ]
    etree.SubElement(Endereco, "Bairro").text = data["ies_registradora_endereco_bairro"]
    etree.SubElement(Endereco, "CodigoMunicipio").text = data[
        "ies_registradora_endereco_codigo_municipio"
    ]
    etree.SubElement(Endereco, "NomeMunicipio").text = data[
        "ies_registradora_endereco_nome_municipio"
    ]
    etree.SubElement(Endereco, "UF").text = data["ies_registradora_endereco_uf"]
    etree.SubElement(Endereco, "CEP").text = data["ies_registradora_endereco_cep"]
    Credenciamento = etree.SubElement(IesRegistradora, "Credenciamento")
    InformacoesTramitacaoEMEC = etree.SubElement(
        Credenciamento, "InformacoesTramitacaoEMEC"
    )
    etree.SubElement(InformacoesTramitacaoEMEC, "NumeroProcesso").text = data[
        "ies_registradora_credenciamento_numero_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "TipoProcesso").text = data[
        "ies_registradora_credenciamento_tipo_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataCadastro").text = data[
        "ies_registradora_credenciamento_data_cadastro"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataProtocolo").text = data[
        "ies_registradora_credenciamento_data_protocolo"
    ]
    Recredenciamento = etree.SubElement(IesRegistradora, "Recredenciamento")
    etree.SubElement(Recredenciamento, "Tipo").text = data[
        "ies_registradora_recredenciamento_tipo"
    ]
    etree.SubElement(Recredenciamento, "Numero").text = data[
        "ies_registradora_recredenciamento_numero"
    ]
    etree.SubElement(Recredenciamento, "Data").text = data[
        "ies_registradora_recredenciamento_data"
    ]
    etree.SubElement(Recredenciamento, "VeiculoPublicacao").text = data[
        "ies_registradora_recredenciamento_veiculo_publicacao"
    ]
    etree.SubElement(Recredenciamento, "DataPublicacao").text = data[
        "ies_registradora_recredenciamento_data_publicacao"
    ]
    etree.SubElement(Recredenciamento, "SecaoPublicacao").text = data[
        "ies_registradora_recredenciamento_secao_publicacao"
    ]
    etree.SubElement(Recredenciamento, "PaginaPublicacao").text = data[
        "ies_registradora_recredenciamento_pagina_publicacao"
    ]
    etree.SubElement(Recredenciamento, "NumeroDOU").text = data[
        "ies_registradora_recredenciamento_numero_dou"
    ]
    RenovacaoDeRecredenciamento = etree.SubElement(
        IesRegistradora, "RenovacaoDeRecredenciamento"
    )
    InformacoesTramitacaoEMEC = etree.SubElement(
        RenovacaoDeRecredenciamento, "InformacoesTramitacaoEMEC"
    )
    etree.SubElement(InformacoesTramitacaoEMEC, "NumeroProcesso").text = data[
        "ies_registradora_renovacao_recredenciamento_numero_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "TipoProcesso").text = data[
        "ies_registradora_renovacao_recredenciamento_tipo_processo"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataCadastro").text = data[
        "ies_registradora_renovacao_recredenciamento_data_cadastro"
    ]
    etree.SubElement(InformacoesTramitacaoEMEC, "DataProtocolo").text = data[
        "ies_registradora_renovacao_recredenciamento_data_protocolo"
    ]
    AtoRegulatorioAutorizacaoRegistro = etree.SubElement(
        IesRegistradora, "AtoRegulatorioAutorizacaoRegistro"
    )
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "Tipo").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_tipo"
    ]
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "Numero").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_numero"
    ]
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "Data").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_data"
    ]
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "VeiculoPublicacao").text = (
        data["ies_registradora_ato_regulatorio_autorizacao_registro_veiculo_publicacao"]
    )
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "DataPublicacao").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_data_publicacao"
    ]
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "SecaoPublicacao").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_secao_publicacao"
    ]
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "PaginaPublicacao").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_pagina_publicacao"
    ]
    etree.SubElement(AtoRegulatorioAutorizacaoRegistro, "NumeroDOU").text = data[
        "ies_registradora_ato_regulatorio_autorizacao_registro_numero_dou"
    ]
    Mantenedora = etree.SubElement(IesRegistradora, "Mantenedora")
    etree.SubElement(Mantenedora, "RazaoSocial").text = data[
        "ies_registradora_mantenedora_razao_social"
    ]
    etree.SubElement(Mantenedora, "CNPJ").text = data[
        "ies_registradora_mantenedora_cnpj"
    ]
    Endereco = etree.SubElement(Mantenedora, "Endereco")
    etree.SubElement(Endereco, "Logradouro").text = data[
        "ies_registradora_mantenedora_endereco_logradouro"
    ]
    etree.SubElement(Endereco, "Bairro").text = data[
        "ies_registradora_mantenedora_endereco_bairro"
    ]
    etree.SubElement(Endereco, "CodigoMunicipio").text = data[
        "ies_registradora_mantenedora_endereco_codigo_municipio"
    ]
    etree.SubElement(Endereco, "NomeMunicipio").text = data[
        "ies_registradora_mantenedora_endereco_nome_municipio"
    ]
    etree.SubElement(Endereco, "UF").text = data[
        "ies_registradora_mantenedora_endereco_uf"
    ]
    etree.SubElement(Endereco, "CEP").text = data[
        "ies_registradora_mantenedora_endereco_cep"
    ]

    LivroRegistro = etree.SubElement(DadosRegistro, "LivroRegistro")
    etree.SubElement(LivroRegistro, "LivroRegistro").text = data["livro_registro"]
    etree.SubElement(LivroRegistro, "NumeroFolhaDoDiploma").text = data[
        "numero_folha_diploma"
    ]
    etree.SubElement(LivroRegistro, "NumeroSequenciaDoDiploma").text = data[
        "numero_sequencia_diploma"
    ]
    etree.SubElement(LivroRegistro, "ProcessoDoDiploma").text = data["processo_diploma"]
    etree.SubElement(LivroRegistro, "DataColacaoGrau").text = data["data_colacao_grau"]
    etree.SubElement(LivroRegistro, "DataExpedicaoDiploma").text = data[
        "data_expedicao_diploma"
    ]
    etree.SubElement(LivroRegistro, "DataRegistroDiploma").text = data[
        "data_registro_diploma"
    ]
    ResponsavelRegistro = etree.SubElement(LivroRegistro, "ResponsavelRegistro")
    etree.SubElement(ResponsavelRegistro, "Nome").text = data[
        "responsavel_registro_nome"
    ]
    etree.SubElement(ResponsavelRegistro, "CPF").text = data["responsavel_registro_cpf"]
    etree.SubElement(ResponsavelRegistro, "IDouNumeroMatricula").text = data[
        "responsavel_registro_id_ou_matricula"
    ]

    etree.SubElement(DadosRegistro, "IdDocumentacaoAcademica").text = data[
        "id_documentacao_academica"
    ]

    Seguranca = etree.SubElement(DadosRegistro, "Seguranca")
    etree.SubElement(Seguranca, "CodigoValidacao").text = data["codigo_validacao"]

    etree.SubElement(DadosRegistro, "InformacoesAdicionais").text = data[
        "informacoes_adicionais"
    ]
    Assinantes = etree.SubElement(DadosRegistro, "Assinantes")
    Assinante3 = etree.SubElement(Assinantes, "Assinante")

    etree.SubElement(Assinante3, "CPF").text = data["assinante_3_cpf"]
    etree.SubElement(Assinante3, "Cargo").text = data["assinante_3_cargo"]
    # Assinante4 = etree.SubElement(Assinantes, "Assinante")
    # etree.SubElement(Assinante4, "CPF").text = data["assinante_4_cpf"]
    # etree.SubElement(Assinante4, "Cargo").text = data["assinante_4_cargo"]

    return etree.tostring(
        root, pretty_print=True, xml_declaration=True, encoding="UTF-8"
    )


def generate_xml2(data):
    pass


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
        root, pretty_print=True, xml_declaration=True, encoding="UTF-8", indent="    "
    )

    return xml_output


st.set_page_config(page_title="XML Generator", layout="wide")

tabs = st.tabs(["Diploma Digital", "Histórico Escolar"])

with tabs[0]:
    st.title("Gerador de XML de Diploma Digital")

    nome = st.text_input("Nome")
    nome_social = st.text_input("Nome Social")
    sexo = st.text_input("Sexo")
    nacionalidade = st.text_input("Nacionalidade")
    nome_municipio_estrangeiro = st.text_input("Nome Município Estrangeiro")
    cpf = st.text_input("CPF")
    rg_numero = st.text_input("Número RG")
    rg_orgao_expedidor = st.text_input("Órgão Expedidor RG")
    rg_uf = st.text_input("UF RG")
    data_nascimento = st.date_input("Data de Nascimento")
    data_conclusao = st.date_input("Data de Conclusão")

    nome_curso = st.text_input("Nome do Curso")
    codigo_curso_emec = st.text_input("Código do Curso no e-MEC")
    nome_habilitacao_1 = st.text_input("Nome da Habilitação 1")
    data_habilitacao_1 = st.date_input("Data da Habilitação 1")
    nome_habilitacao_2 = st.text_input("Nome da Habilitação 2")
    data_habilitacao_2 = st.date_input("Data da Habilitação 2")
    modalidade_curso = st.selectbox(
        "Modalidade do Curso", ["Presencial", "EaD", "Semipresencial"]
    )
    titulo_conferido = st.text_input("Título Conferido")
    grau_conferido = st.text_input("Grau Conferido")
    enfase_1 = st.text_input("Ênfase 1")
    enfase_2 = st.text_input("Ênfase 2")
    endereco_curso_logradouro = st.text_input("Logradouro do Endereço do Curso")
    endereco_curso_numero = st.text_input("Número do Endereço do Curso")
    endereco_curso_complemento = st.text_input("Complemento do Endereço do Curso")
    endereco_curso_bairro = st.text_input("Bairro do Endereço do Curso")
    endereco_curso_codigo_municipio = st.text_input(
        "Código do Município do Endereço do Curso"
    )
    endereco_curso_nome_municipio = st.text_input(
        "Nome do Município do Endereço do Curso"
    )
    endereco_curso_uf = st.text_input("UF do Endereço do Curso")
    endereco_curso_cep = st.text_input("CEP do Endereço do Curso")
    polo_nome = st.text_input("Nome do Polo")
    polo_endereco_logradouro = st.text_input("Logradouro do Endereço do Polo")
    polo_endereco_bairro = st.text_input("Bairro do Endereço do Polo")
    polo_endereco_nome_municipio_estrangeiro = st.text_input(
        "Nome do Município Estrangeiro do Endereço do Polo"
    )
    polo_endereco_cep = st.text_input("CEP do Endereço do Polo")
    polo_codigo_emec = st.text_input("Código e-MEC do Polo")
    autorizacao_numero_processo = st.text_input("Número do Processo de Autorização")
    autorizacao_tipo_processo = st.text_input("Tipo do Processo de Autorização")
    autorizacao_data_cadastro = st.date_input(
        "Data de Cadastro do Processo de Autorização"
    )
    autorizacao_data_protocolo = st.date_input(
        "Data de Protocolo do Processo de Autorização"
    )
    reconhecimento_tipo = st.text_input("Tipo de Reconhecimento")
    reconhecimento_numero = st.text_input("Número do Reconhecimento")
    reconhecimento_data = st.date_input("Data do Reconhecimento")
    reconhecimento_veiculo_publicacao = st.text_input(
        "Veículo de Publicação do Reconhecimento"
    )
    reconhecimento_data_publicacao = st.date_input(
        "Data de Publicação do Reconhecimento"
    )
    reconhecimento_secao_publicacao = st.text_input(
        "Seção de Publicação do Reconhecimento"
    )
    reconhecimento_pagina_publicacao = st.text_input(
        "Página de Publicação do Reconhecimento"
    )
    reconhecimento_numero_dou = st.text_input("Número do DOU do Reconhecimento")
    renovacao_reconhecimento_tipo = st.text_input("Tipo de Renovação de Reconhecimento")
    renovacao_reconhecimento_numero = st.text_input(
        "Número da Renovação de Reconhecimento"
    )
    renovacao_reconhecimento_data = st.date_input("Data da Renovação de Reconhecimento")
    renovacao_reconhecimento_veiculo_publicacao = st.text_input(
        "Veículo de Publicação da Renovação de Reconhecimento"
    )
    renovacao_reconhecimento_data_publicacao = st.date_input(
        "Data de Publicação da Renovação de Reconhecimento"
    )
    renovacao_reconhecimento_secao_publicacao = st.text_input(
        "Seção de Publicação da Renovação de Reconhecimento"
    )
    renovacao_reconhecimento_pagina_publicacao = st.text_input(
        "Página de Publicação da Renovação de Reconhecimento"
    )
    renovacao_reconhecimento_numero_dou = st.text_input(
        "Número do DOU da Renovação de Reconhecimento"
    )

    dados_ies_original_curso_pta_nome = st.text_input(
        "Nome da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_cnpj = st.text_input(
        "CNPJ da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_logradouro = st.text_input(
        "Logradouro do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_numero = st.text_input(
        "Número do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_complemento = st.text_input(
        "Complemento do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_bairro = st.text_input(
        "Bairro do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_codigo_municipio = st.text_input(
        "Código do Município do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_nome_municipio = st.text_input(
        "Nome do Município do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_uf = st.text_input(
        "UF do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_endereco_cep = st.text_input(
        "CEP do Endereço da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_tipo = st.text_input(
        "Tipo de Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_numero = st.text_input(
        "Número do Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_data = st.date_input(
        "Data do Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_veiculo_publicacao = st.text_input(
        "Veículo de Publicação do Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_data_publicacao = st.date_input(
        "Data de Publicação do Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_secao_publicacao = st.text_input(
        "Seção de Publicação do Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_pagina_publicacao = st.text_input(
        "Página de Publicação do Descredenciamento da IES Original do Curso PTA"
    )
    dados_ies_original_curso_pta_descredenciamento_numero_dou = st.text_input(
        "Número do DOU do Descredenciamento da IES Original do Curso PTA"
    )

    ies_emissora_nome = st.text_input("Nome da IES Emissora")
    ies_emissora_codigo_mec = st.text_input("Código MEC da IES Emissora")
    ies_emissora_cnpj = st.text_input("CNPJ da IES Emissora")
    ies_emissora_endereco_logradouro = st.text_input(
        "Logradouro do Endereço da IES Emissora"
    )
    ies_emissora_endereco_numero = st.text_input("Número do Endereço da IES Emissora")
    ies_emissora_endereco_complemento = st.text_input(
        "Complemento do Endereço da IES Emissora"
    )
    ies_emissora_endereco_bairro = st.text_input("Bairro do Endereço da IES Emissora")
    ies_emissora_endereco_nome_municipio_estrangeiro = st.text_input(
        "Nome do Município Estrangeiro do Endereço da IES Emissora"
    )
    ies_emissora_endereco_cep = st.text_input("CEP do Endereço da IES Emissora")
    ies_emissora_credenciamento_numero_processo = st.text_input(
        "Número do Processo de Credenciamento da IES Emissora"
    )
    ies_emissora_credenciamento_tipo_processo = st.text_input(
        "Tipo do Processo de Credenciamento da IES Emissora"
    )
    ies_emissora_credenciamento_data_cadastro = st.date_input(
        "Data de Cadastro do Processo de Credenciamento da IES Emissora"
    )
    ies_emissora_credenciamento_data_protocolo = st.date_input(
        "Data de Protocolo do Processo de Credenciamento da IES Emissora"
    )
    ies_emissora_recredenciamento_numero_processo = st.text_input(
        "Número do Processo de Recredenciamento da IES Emissora"
    )
    ies_emissora_recredenciamento_tipo_processo = st.text_input(
        "Tipo do Processo de Recredenciamento da IES Emissora"
    )
    ies_emissora_recredenciamento_data_cadastro = st.date_input(
        "Data de Cadastro do Processo de Recredenciamento da IES Emissora"
    )
    ies_emissora_recredenciamento_data_protocolo = st.date_input(
        "Data de Protocolo do Processo de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_tipo = st.text_input(
        "Tipo de Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_numero = st.text_input(
        "Número da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_data = st.date_input(
        "Data da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_veiculo_publicacao = st.text_input(
        "Veículo de Publicação da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_data_publicacao = st.date_input(
        "Data de Publicação da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_secao_publicacao = st.text_input(
        "Seção de Publicação da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_pagina_publicacao = st.text_input(
        "Página de Publicação da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_renovacao_recredenciamento_numero_dou = st.text_input(
        "Número do DOU da Renovação de Recredenciamento da IES Emissora"
    )
    ies_emissora_mantenedora_razao_social = st.text_input(
        "Razão Social da Mantenedora da IES Emissora"
    )
    ies_emissora_mantenedora_cnpj = st.text_input("CNPJ da Mantenedora da IES Emissora")
    ies_emissora_mantenedora_endereco_logradouro = st.text_input(
        "Logradouro do Endereço da Mantenedora da IES Emissora"
    )
    ies_emissora_mantenedora_endereco_bairro = st.text_input(
        "Bairro do Endereço da Mantenedora da IES Emissora"
    )
    ies_emissora_mantenedora_endereco_codigo_municipio = st.text_input(
        "Código do Município do Endereço da Mantenedora da IES Emissora"
    )
    ies_emissora_mantenedora_endereco_nome_municipio = st.text_input(
        "Nome do Município do Endereço da Mantenedora da IES Emissora"
    )
    ies_emissora_mantenedora_endereco_uf = st.text_input(
        "UF do Endereço da Mantenedora da IES Emissora"
    )
    ies_emissora_mantenedora_endereco_cep = st.text_input(
        "CEP do Endereço da Mantenedora da IES Emissora"
    )

    assinante_1_cpf = st.text_input("CPF do Assinante 1")
    assinante_1_cargo = st.text_input("Cargo do Assinante 1")
    assinante_2_cpf = st.text_input("CPF do Assinante 2")
    assinante_2_cargo = st.text_input("Cargo do Assinante 2")

    ies_registradora_nome = st.text_input("Nome da IES Registradora")
    ies_registradora_codigo_mec = st.text_input("Código MEC da IES Registradora")
    ies_registradora_cnpj = st.text_input("CNPJ da IES Registradora")
    ies_registradora_endereco_logradouro = st.text_input(
        "Logradouro do Endereço da IES Registradora"
    )
    ies_registradora_endereco_numero = st.text_input(
        "Número do Endereço da IES Registradora"
    )
    ies_registradora_endereco_complemento = st.text_input(
        "Complemento do Endereço da IES Registradora"
    )
    ies_registradora_endereco_bairro = st.text_input(
        "Bairro do Endereço da IES Registradora"
    )
    ies_registradora_endereco_codigo_municipio = st.text_input(
        "Código do Município do Endereço da IES Registradora"
    )
    ies_registradora_endereco_nome_municipio = st.text_input(
        "Nome do Município do Endereço da IES Registradora"
    )
    ies_registradora_endereco_uf = st.text_input("UF do Endereço da IES Registradora")
    ies_registradora_endereco_cep = st.text_input("CEP do Endereço da IES Registradora")
    ies_registradora_credenciamento_numero_processo = st.text_input(
        "Número do Processo de Credenciamento da IES Registradora"
    )
    ies_registradora_credenciamento_tipo_processo = st.text_input(
        "Tipo do Processo de Credenciamento da IES Registradora"
    )
    ies_registradora_credenciamento_data_cadastro = st.date_input(
        "Data de Cadastro do Processo de Credenciamento da IES Registradora"
    )
    ies_registradora_credenciamento_data_protocolo = st.date_input(
        "Data de Protocolo do Processo de Credenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_tipo = st.text_input(
        "Tipo de Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_numero = st.text_input(
        "Número do Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_data = st.date_input(
        "Data do Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_veiculo_publicacao = st.text_input(
        "Veículo de Publicação do Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_data_publicacao = st.date_input(
        "Data de Publicação do Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_secao_publicacao = st.text_input(
        "Seção de Publicação do Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_pagina_publicacao = st.text_input(
        "Página de Publicação do Recredenciamento da IES Registradora"
    )
    ies_registradora_recredenciamento_numero_dou = st.text_input(
        "Número do DOU do Recredenciamento da IES Registradora"
    )
    ies_registradora_renovacao_recredenciamento_numero_processo = st.text_input(
        "Número do Processo de Renovação de Recredenciamento da IES Registradora"
    )
    ies_registradora_renovacao_recredenciamento_tipo_processo = st.text_input(
        "Tipo do Processo de Renovação de Recredenciamento da IES Registradora"
    )
    ies_registradora_renovacao_recredenciamento_data_cadastro = st.date_input(
        "Data de Cadastro do Processo de Renovação de Recredenciamento da IES Registradora"
    )
    ies_registradora_renovacao_recredenciamento_data_protocolo = st.date_input(
        "Data de Protocolo do Processo de Renovação de Recredenciamento da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_tipo = st.text_input(
        "Tipo do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_numero = st.text_input(
        "Número do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_data = st.date_input(
        "Data do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_veiculo_publicacao = st.text_input(
        "Veículo de Publicação do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_data_publicacao = st.date_input(
        "Data de Publicação do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_secao_publicacao = st.text_input(
        "Seção de Publicação do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_pagina_publicacao = st.text_input(
        "Página de Publicação do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_ato_regulatorio_autorizacao_registro_numero_dou = st.text_input(
        "Número do DOU do Ato Regulatório de Autorização de Registro da IES Registradora"
    )
    ies_registradora_mantenedora_razao_social = st.text_input(
        "Razão Social da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_cnpj = st.text_input(
        "CNPJ da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_endereco_logradouro = st.text_input(
        "Logradouro do Endereço da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_endereco_bairro = st.text_input(
        "Bairro do Endereço da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_endereco_codigo_municipio = st.text_input(
        "Código do Município do Endereço da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_endereco_nome_municipio = st.text_input(
        "Nome do Município do Endereço da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_endereco_uf = st.text_input(
        "UF do Endereço da Mantenedora da IES Registradora"
    )
    ies_registradora_mantenedora_endereco_cep = st.text_input(
        "CEP do Endereço da Mantenedora da IES Registradora"
    )

    livro_registro = st.text_input("Livro de Registro")
    numero_folha_diploma = st.text_input("Número da Folha do Diploma")
    numero_sequencia_diploma = st.text_input("Número Sequencial do Diploma")
    processo_diploma = st.text_input("Processo do Diploma")
    data_colacao_grau = st.date_input("Data de Colação de Grau")
    data_expedicao_diploma = st.date_input("Data de Expedição do Diploma")
    data_registro_diploma = st.date_input("Data de Registro do Diploma")
    responsavel_registro_nome = st.text_input("Nome do Responsável pelo Registro")
    responsavel_registro_cpf = st.text_input("CPF do Responsável pelo Registro")
    responsavel_registro_id_ou_matricula = st.text_input(
        "ID ou Número de Matrícula do Responsável pelo Registro"
    )

    id_documentacao_academica = st.text_input("ID da Documentação Acadêmica")
    codigo_validacao = st.text_input("Código de Validação")
    informacoes_adicionais = st.text_input("Informações Adicionais")

    assinante_3_cpf = st.text_input("CPF do Assinante")
    assinante_3_cargo = st.text_input("Cargo do Assinante")
    # assinante_4_cpf = st.text_input("CPF do Assinante 4")
    # assinante_4_cargo = st.text_input("Cargo do Assinante 4")

    submitted = st.button("Gerar XML")

    if submitted:
        data = {
            "nome": nome,
            "nome_social": nome_social,
            "sexo": sexo,
            "nacionalidade": nacionalidade,
            "nome_municipio_estrangeiro": nome_municipio_estrangeiro,
            "cpf": cpf,
            "rg_numero": rg_numero,
            "rg_orgao_expedidor": rg_orgao_expedidor,
            "rg_uf": rg_uf,
            "data_nascimento": data_nascimento.strftime("%Y-%m-%d"),
            "data_conclusao": data_conclusao.strftime("%Y-%m-%d"),
            "nome_curso": nome_curso,
            "codigo_curso_emec": codigo_curso_emec,
            "nome_habilitacao_1": nome_habilitacao_1,
            "data_habilitacao_1": data_habilitacao_1.strftime("%Y-%m-%d"),
            "nome_habilitacao_2": nome_habilitacao_2,
            "data_habilitacao_2": data_habilitacao_2.strftime("%Y-%m-%d"),
            "modalidade_curso": modalidade_curso,
            "titulo_conferido": titulo_conferido,
            "grau_conferido": grau_conferido,
            "enfase_1": enfase_1,
            "enfase_2": enfase_2,
            "endereco_curso_logradouro": endereco_curso_logradouro,
            "endereco_curso_numero": endereco_curso_numero,
            "endereco_curso_complemento": endereco_curso_complemento,
            "endereco_curso_bairro": endereco_curso_bairro,
            "endereco_curso_codigo_municipio": endereco_curso_codigo_municipio,
            "endereco_curso_nome_municipio": endereco_curso_nome_municipio,
            "endereco_curso_uf": endereco_curso_uf,
            "endereco_curso_cep": endereco_curso_cep,
            "polo_nome": polo_nome,
            "polo_endereco_logradouro": polo_endereco_logradouro,
            "polo_endereco_bairro": polo_endereco_bairro,
            "polo_endereco_nome_municipio_estrangeiro": polo_endereco_nome_municipio_estrangeiro,
            "polo_endereco_cep": polo_endereco_cep,
            "polo_codigo_emec": polo_codigo_emec,
            "autorizacao_numero_processo": autorizacao_numero_processo,
            "autorizacao_tipo_processo": autorizacao_tipo_processo,
            "autorizacao_data_cadastro": autorizacao_data_cadastro.strftime("%Y-%m-%d"),
            "autorizacao_data_protocolo": autorizacao_data_protocolo.strftime(
                "%Y-%m-%d"
            ),
            "reconhecimento_tipo": reconhecimento_tipo,
            "reconhecimento_numero": reconhecimento_numero,
            "reconhecimento_data": reconhecimento_data.strftime("%Y-%m-%d"),
            "reconhecimento_veiculo_publicacao": reconhecimento_veiculo_publicacao,
            "reconhecimento_data_publicacao": reconhecimento_data_publicacao.strftime(
                "%Y-%m-%d"
            ),
            "reconhecimento_secao_publicacao": reconhecimento_secao_publicacao,
            "reconhecimento_pagina_publicacao": reconhecimento_pagina_publicacao,
            "reconhecimento_numero_dou": reconhecimento_numero_dou,
            "renovacao_reconhecimento_tipo": renovacao_reconhecimento_tipo,
            "renovacao_reconhecimento_numero": renovacao_reconhecimento_numero,
            "renovacao_reconhecimento_data": renovacao_reconhecimento_data.strftime(
                "%Y-%m-%d"
            ),
            "renovacao_reconhecimento_veiculo_publicacao": renovacao_reconhecimento_veiculo_publicacao,
            "renovacao_reconhecimento_data_publicacao": renovacao_reconhecimento_data_publicacao.strftime(
                "%Y-%m-%d"
            ),
            "renovacao_reconhecimento_secao_publicacao": renovacao_reconhecimento_secao_publicacao,
            "renovacao_reconhecimento_pagina_publicacao": renovacao_reconhecimento_pagina_publicacao,
            "renovacao_reconhecimento_numero_dou": renovacao_reconhecimento_numero_dou,
            "dados_ies_original_curso_pta_nome": dados_ies_original_curso_pta_nome,
            "dados_ies_original_curso_pta_cnpj": dados_ies_original_curso_pta_cnpj,
            "dados_ies_original_curso_pta_endereco_logradouro": dados_ies_original_curso_pta_endereco_logradouro,
            "dados_ies_original_curso_pta_endereco_numero": dados_ies_original_curso_pta_endereco_numero,
            "dados_ies_original_curso_pta_endereco_complemento": dados_ies_original_curso_pta_endereco_complemento,
            "dados_ies_original_curso_pta_endereco_bairro": dados_ies_original_curso_pta_endereco_bairro,
            "dados_ies_original_curso_pta_endereco_codigo_municipio": dados_ies_original_curso_pta_endereco_codigo_municipio,
            "dados_ies_original_curso_pta_endereco_nome_municipio": dados_ies_original_curso_pta_endereco_nome_municipio,
            "dados_ies_original_curso_pta_endereco_uf": dados_ies_original_curso_pta_endereco_uf,
            "dados_ies_original_curso_pta_endereco_cep": dados_ies_original_curso_pta_endereco_cep,
            "dados_ies_original_curso_pta_descredenciamento_tipo": dados_ies_original_curso_pta_descredenciamento_tipo,
            "dados_ies_original_curso_pta_descredenciamento_numero": dados_ies_original_curso_pta_descredenciamento_numero,
            "dados_ies_original_curso_pta_descredenciamento_data": dados_ies_original_curso_pta_descredenciamento_data.strftime(
                "%Y-%m-%d"
            ),
            "dados_ies_original_curso_pta_descredenciamento_veiculo_publicacao": dados_ies_original_curso_pta_descredenciamento_veiculo_publicacao,
            "dados_ies_original_curso_pta_descredenciamento_data_publicacao": dados_ies_original_curso_pta_descredenciamento_data_publicacao.strftime(
                "%Y-%m-%d"
            ),
            "dados_ies_original_curso_pta_descredenciamento_secao_publicacao": dados_ies_original_curso_pta_descredenciamento_secao_publicacao,
            "dados_ies_original_curso_pta_descredenciamento_pagina_publicacao": dados_ies_original_curso_pta_descredenciamento_pagina_publicacao,
            "dados_ies_original_curso_pta_descredenciamento_numero_dou": dados_ies_original_curso_pta_descredenciamento_numero_dou,
            "ies_emissora_nome": ies_emissora_nome,
            "ies_emissora_codigo_mec": ies_emissora_codigo_mec,
            "ies_emissora_cnpj": ies_emissora_cnpj,
            "ies_emissora_endereco_logradouro": ies_emissora_endereco_logradouro,
            "ies_emissora_endereco_numero": ies_emissora_endereco_numero,
            "ies_emissora_endereco_complemento": ies_emissora_endereco_complemento,
            "ies_emissora_endereco_bairro": ies_emissora_endereco_bairro,
            "ies_emissora_endereco_nome_municipio_estrangeiro": ies_emissora_endereco_nome_municipio_estrangeiro,
            "ies_emissora_endereco_cep": ies_emissora_endereco_cep,
            "ies_emissora_credenciamento_numero_processo": ies_emissora_credenciamento_numero_processo,
            "ies_emissora_credenciamento_tipo_processo": ies_emissora_credenciamento_tipo_processo,
            "ies_emissora_credenciamento_data_cadastro": ies_emissora_credenciamento_data_cadastro.strftime(
                "%Y-%m-%d"
            ),
            "ies_emissora_credenciamento_data_protocolo": ies_emissora_credenciamento_data_protocolo.strftime(
                "%Y-%m-%d"
            ),
            "ies_emissora_recredenciamento_numero_processo": ies_emissora_recredenciamento_numero_processo,
            "ies_emissora_recredenciamento_tipo_processo": ies_emissora_recredenciamento_tipo_processo,
            "ies_emissora_recredenciamento_data_cadastro": ies_emissora_recredenciamento_data_cadastro.strftime(
                "%Y-%m-%d"
            ),
            "ies_emissora_recredenciamento_data_protocolo": ies_emissora_recredenciamento_data_protocolo.strftime(
                "%Y-%m-%d"
            ),
            "ies_emissora_renovacao_recredenciamento_tipo": ies_emissora_renovacao_recredenciamento_tipo,
            "ies_emissora_renovacao_recredenciamento_numero": ies_emissora_renovacao_recredenciamento_numero,
            "ies_emissora_renovacao_recredenciamento_data": ies_emissora_renovacao_recredenciamento_data.strftime(
                "%Y-%m-%d"
            ),
            "ies_emissora_renovacao_recredenciamento_veiculo_publicacao": ies_emissora_renovacao_recredenciamento_veiculo_publicacao,
            "ies_emissora_renovacao_recredenciamento_data_publicacao": ies_emissora_renovacao_recredenciamento_data_publicacao.strftime(
                "%Y-%m-%d"
            ),
            "ies_emissora_renovacao_recredenciamento_secao_publicacao": ies_emissora_renovacao_recredenciamento_secao_publicacao,
            "ies_emissora_renovacao_recredenciamento_pagina_publicacao": ies_emissora_renovacao_recredenciamento_pagina_publicacao,
            "ies_emissora_renovacao_recredenciamento_numero_dou": ies_emissora_renovacao_recredenciamento_numero_dou,
            "ies_emissora_mantenedora_razao_social": ies_emissora_mantenedora_razao_social,
            "ies_emissora_mantenedora_cnpj": ies_emissora_mantenedora_cnpj,
            "ies_emissora_mantenedora_endereco_logradouro": ies_emissora_mantenedora_endereco_logradouro,
            "ies_emissora_mantenedora_endereco_bairro": ies_emissora_mantenedora_endereco_bairro,
            "ies_emissora_mantenedora_endereco_codigo_municipio": ies_emissora_mantenedora_endereco_codigo_municipio,
            "ies_emissora_mantenedora_endereco_nome_municipio": ies_emissora_mantenedora_endereco_nome_municipio,
            "ies_emissora_mantenedora_endereco_uf": ies_emissora_mantenedora_endereco_uf,
            "ies_emissora_mantenedora_endereco_cep": ies_emissora_mantenedora_endereco_cep,
            "assinante_1_cpf": assinante_1_cpf,
            "assinante_1_cargo": assinante_1_cargo,
            "assinante_2_cpf": assinante_2_cpf,
            "assinante_2_cargo": assinante_2_cargo,
            "ies_registradora_nome": ies_registradora_nome,
            "ies_registradora_codigo_mec": ies_registradora_codigo_mec,
            "ies_registradora_cnpj": ies_registradora_cnpj,
            "ies_registradora_endereco_logradouro": ies_registradora_endereco_logradouro,
            "ies_registradora_endereco_numero": ies_registradora_endereco_numero,
            "ies_registradora_endereco_complemento": ies_registradora_endereco_complemento,
            "ies_registradora_endereco_bairro": ies_registradora_endereco_bairro,
            "ies_registradora_endereco_codigo_municipio": ies_registradora_endereco_codigo_municipio,
            "ies_registradora_endereco_nome_municipio": ies_registradora_endereco_nome_municipio,
            "ies_registradora_endereco_uf": ies_registradora_endereco_uf,
            "ies_registradora_endereco_cep": ies_registradora_endereco_cep,
            "ies_registradora_credenciamento_numero_processo": ies_registradora_credenciamento_numero_processo,
            "ies_registradora_credenciamento_tipo_processo": ies_registradora_credenciamento_tipo_processo,
            "ies_registradora_credenciamento_data_cadastro": ies_registradora_credenciamento_data_cadastro.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_credenciamento_data_protocolo": ies_registradora_credenciamento_data_protocolo.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_recredenciamento_tipo": ies_registradora_recredenciamento_tipo,
            "ies_registradora_recredenciamento_numero": ies_registradora_recredenciamento_numero,
            "ies_registradora_recredenciamento_data": ies_registradora_recredenciamento_data.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_recredenciamento_veiculo_publicacao": ies_registradora_recredenciamento_veiculo_publicacao,
            "ies_registradora_recredenciamento_data_publicacao": ies_registradora_recredenciamento_data_publicacao.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_recredenciamento_secao_publicacao": ies_registradora_recredenciamento_secao_publicacao,
            "ies_registradora_recredenciamento_pagina_publicacao": ies_registradora_recredenciamento_pagina_publicacao,
            "ies_registradora_recredenciamento_numero_dou": ies_registradora_recredenciamento_numero_dou,
            "ies_registradora_renovacao_recredenciamento_numero_processo": ies_registradora_renovacao_recredenciamento_numero_processo,
            "ies_registradora_renovacao_recredenciamento_tipo_processo": ies_registradora_renovacao_recredenciamento_tipo_processo,
            "ies_registradora_renovacao_recredenciamento_data_cadastro": ies_registradora_renovacao_recredenciamento_data_cadastro.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_renovacao_recredenciamento_data_protocolo": ies_registradora_renovacao_recredenciamento_data_protocolo.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_ato_regulatorio_autorizacao_registro_tipo": ies_registradora_ato_regulatorio_autorizacao_registro_tipo,
            "ies_registradora_ato_regulatorio_autorizacao_registro_numero": ies_registradora_ato_regulatorio_autorizacao_registro_numero,
            "ies_registradora_ato_regulatorio_autorizacao_registro_data": ies_registradora_ato_regulatorio_autorizacao_registro_data.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_ato_regulatorio_autorizacao_registro_veiculo_publicacao": ies_registradora_ato_regulatorio_autorizacao_registro_veiculo_publicacao,
            "ies_registradora_ato_regulatorio_autorizacao_registro_data_publicacao": ies_registradora_ato_regulatorio_autorizacao_registro_data_publicacao.strftime(
                "%Y-%m-%d"
            ),
            "ies_registradora_ato_regulatorio_autorizacao_registro_secao_publicacao": ies_registradora_ato_regulatorio_autorizacao_registro_secao_publicacao,
            "ies_registradora_ato_regulatorio_autorizacao_registro_pagina_publicacao": ies_registradora_ato_regulatorio_autorizacao_registro_pagina_publicacao,
            "ies_registradora_ato_regulatorio_autorizacao_registro_numero_dou": ies_registradora_ato_regulatorio_autorizacao_registro_numero_dou,
            "ies_registradora_mantenedora_razao_social": ies_registradora_mantenedora_razao_social,
            "ies_registradora_mantenedora_cnpj": ies_registradora_mantenedora_cnpj,
            "ies_registradora_mantenedora_endereco_logradouro": ies_registradora_mantenedora_endereco_logradouro,
            "ies_registradora_mantenedora_endereco_bairro": ies_registradora_mantenedora_endereco_bairro,
            "ies_registradora_mantenedora_endereco_codigo_municipio": ies_registradora_mantenedora_endereco_codigo_municipio,
            "ies_registradora_mantenedora_endereco_nome_municipio": ies_registradora_mantenedora_endereco_nome_municipio,
            "ies_registradora_mantenedora_endereco_uf": ies_registradora_mantenedora_endereco_uf,
            "ies_registradora_mantenedora_endereco_cep": ies_registradora_mantenedora_endereco_cep,
            "livro_registro": livro_registro,
            "numero_folha_diploma": numero_folha_diploma,
            "numero_sequencia_diploma": numero_sequencia_diploma,
            "processo_diploma": processo_diploma,
            "data_colacao_grau": data_colacao_grau.strftime("%Y-%m-%d"),
            "data_expedicao_diploma": data_expedicao_diploma.strftime("%Y-%m-%d"),
            "data_registro_diploma": data_registro_diploma.strftime("%Y-%m-%d"),
            "responsavel_registro_nome": responsavel_registro_nome,
            "responsavel_registro_cpf": responsavel_registro_cpf,
            "responsavel_registro_id_ou_matricula": responsavel_registro_id_ou_matricula,
            "id_documentacao_academica": id_documentacao_academica,
            "codigo_validacao": codigo_validacao,
            "informacoes_adicionais": informacoes_adicionais,
            "assinante_3_cpf": assinante_3_cpf,
            "assinante_3_cargo": assinante_3_cargo,
            # "assinante_4_cpf": assinante_4_cpf,
            # "assinante_4_cargo": assinante_4_cargo,
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
    st.title("Gerador de XML de Histórico Escolar")

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
