# Checagens locais do relatório.
# Elas apontam ausências e indícios. Não provam fidelidade, gramática, fórmula correta nem fluxograma fiel.

import re
import unicodedata


# Títulos usados para localizar cada seção sem cortar listas numeradas internas.
TITULOS_SECOES = {
    1: "RESUMO DO PROCESSO",
    2: "OBJETIVO E RESULTADO ESPERADO",
    3: "ETAPAS IDENTIFICADAS",
    4: "GARGALOS E RISCOS",
    5: "MELHORIAS PROPOSTAS",
    6: "PROPOSTA DE PROCESSO MELHORADO",
    7: "MINUTA DE PROCEDIMENTO OPERACIONAL PADRÃO",
    8: "INDICADORES DE DESEMPENHO",
    9: "PERGUNTAS PARA VALIDAÇÃO",
    10: "FLUXOGRAMA MERMAID",
}

# Seções em que uma afirmação tende a ser apresentada como fato ou como regra da minuta.
SECOES_AFIRMACAO = (1, 3, 5, 6, 7)


def sem_acento(texto):
    # Compara títulos e fórmulas mesmo quando a acentuação varia.
    base = unicodedata.normalize("NFD", texto or "")
    sem_marcas = "".join(caractere for caractere in base if unicodedata.category(caractere) != "Mn")
    return sem_marcas.lower()


def extrair_secao(resposta, numero):
    # Recorta uma seção pelo título oficial, e não por qualquer número solto no texto.
    titulo = TITULOS_SECOES[numero]
    resposta = resposta or ""
    inicio = re.search(
        rf"(?i)(?:^|\n)\s*{numero}\s*[\.\)\-:]*\s*{re.escape(titulo)}",
        resposta,
    )
    if inicio is None:
        return ""

    fim = len(resposta)
    for outro, nome in TITULOS_SECOES.items():
        if outro == numero:
            continue
        # Procura o próximo título oficial depois do início desta seção.
        seguinte = re.search(
            rf"(?i)(?:^|\n)\s*{outro}\s*[\.\)\-:]*\s*{re.escape(nome)}",
            resposta[inicio.end() :],
        )
        if seguinte is not None:
            fim = min(fim, inicio.end() + seguinte.start())
    return resposta[inicio.start() : fim]


def _juntar_secoes(resposta, numeros):
    # Junta só as seções pedidas. Se nenhuma existir, não varre o relatório inteiro.
    partes = [extrair_secao(resposta, numero) for numero in numeros]
    return "\n".join(parte for parte in partes if parte)


def validar_secoes(resposta):
    # Confere a presença dos títulos. Presença não significa que o conteúdo esteja certo.
    avisos = []
    if not (resposta or "").strip():
        return ["A IA não retornou conteúdo."]

    for numero, titulo in TITULOS_SECOES.items():
        secao = f"{numero}. {titulo}"
        if secao.lower() not in resposta.lower():
            avisos.append(f"Seção ausente ou com título diferente: {secao}")
    return avisos


def validar_mermaid(resposta):
    # Confere o bloco Mermaid com regras locais. Não executa o compilador Mermaid.
    avisos = []
    blocos = re.findall(r"```mermaid\s*(.*?)```", resposta or "", flags=re.IGNORECASE | re.DOTALL)
    if not blocos:
        if "```mermaid" in (resposta or "").lower():
            avisos.append("O bloco Mermaid foi aberto e não foi fechado.")
        elif "mermaid" in sem_acento(resposta):
            avisos.append("Há menção a Mermaid, mas não um bloco ```mermaid fechado.")
        else:
            avisos.append("Não foi encontrado um bloco de código Mermaid.")
        return avisos

    if len(blocos) > 1:
        avisos.append("Há mais de um bloco Mermaid. Entregue um único fluxograma.")

    codigo = blocos[0].strip()
    if not codigo or sem_acento(codigo) in {"mermaid flowchart", "flowchart"}:
        avisos.append("O bloco Mermaid está vazio ou contém apenas um título.")
        return avisos

    linhas = [linha.strip() for linha in codigo.splitlines() if linha.strip() and not linha.strip().startswith("%%")]
    primeira = linhas[0] if linhas else ""
    if re.match(r"(?i)flowchart\s+(td|lr)\b", primeira) is None:
        avisos.append("O bloco Mermaid não começa com flowchart TD ou flowchart LR.")

    if re.search(r"-->|==>|-+\.?\s*-+>|---", codigo) is None:
        avisos.append("O bloco Mermaid não contém ligações entre as etapas.")

    for abre, fecha, nome in (("[", "]", "colchetes"), ("(", ")", "parênteses"), ("{", "}", "chaves")):
        if codigo.count(abre) != codigo.count(fecha):
            avisos.append(f"O bloco Mermaid tem {nome} desbalanceados. A sintaxe pode estar inválida.")

    # Losango é decisão. Os caminhos precisam estar nomeados, não apenas desenhados.
    if "{" in codigo and "}" in codigo:
        normalizado = sem_acento(codigo)
        tem_sim = re.search(r"\bsim\b", normalizado) is not None
        tem_nao = re.search(r"\bnao\b", normalizado) is not None
        if not tem_sim or not tem_nao:
            avisos.append("Há decisão no Mermaid sem os caminhos Sim e Não identificados.")
    return avisos


def validar_indicadores(resposta):
    # Procura os termos obrigatórios das duas fórmulas. Não recalcula indicador nenhum.
    secao = extrair_secao(resposta, 8)
    if not secao:
        return ["Indicadores: a seção não foi encontrada, então as fórmulas não foram conferidas."]

    texto = sem_acento(secao)
    avisos = []

    if "tempo medio" not in texto:
        avisos.append("Indicadores: não foi encontrado o tempo médio de atendimento.")
    else:
        if "soma dos tempos" not in texto or "solicitacoes concluidas" not in texto:
            avisos.append(
                "Indicadores: a fórmula do tempo médio não deixa claros a soma dos tempos e a quantidade de solicitações concluídas."
            )
        if re.search(r"\b(horas|dias)\b", texto) is None:
            avisos.append("Indicadores: informe se a unidade do tempo médio será horas ou dias.")

    if "taxa de retrabalho" not in texto:
        avisos.append("Indicadores: não foi encontrada a taxa de retrabalho.")
    else:
        if "solicitacoes devolvidas" not in texto:
            avisos.append(
                "Indicadores: o numerador deve ser a quantidade de solicitações devolvidas, não o total de devoluções."
            )
        if re.search(r"(?:x|\*|×)\s*100", texto) is None:
            avisos.append("Indicadores: a taxa de retrabalho não mostra a multiplicação por 100.")
        if re.search(r"quantidade de devolucoes\s*/", texto) is not None:
            avisos.append(
                "Indicadores: a fórmula parece dividir pela quantidade de devoluções. Isso não é o mesmo que solicitações devolvidas."
            )
        if "mesmo periodo" not in texto and "periodo de referencia" not in texto:
            avisos.append("Indicadores: não ficou explícito que numerador e denominador usam o mesmo período.")

    if "dados necessarios" not in texto and "coleta" not in texto:
        avisos.append("Indicadores: não há explicação dos dados que ainda precisam ser coletados.")
    return avisos


def validar_pop(resposta):
    # A minuta precisa ser reconhecível como proposta e trazer os tópicos pedidos.
    secao = extrair_secao(resposta, 7)
    if not secao:
        return ["POP: a seção da minuta não foi encontrada."]

    # O título já contém "minuta" e "procedimento". A checagem olha o texto depois dele.
    corpo = "\n".join(secao.splitlines()[1:])
    texto = sem_acento(corpo)
    avisos = []
    topicos = (
        ("Objetivo", "objetivo"),
        ("Escopo", "escopo"),
        ("Responsáveis", "responsav"),
        ("Procedimento", "procedimento"),
        ("Registros e controles", "registro"),
        ("Pontos pendentes de validação", "validacao"),
    )
    for rotulo, chave in topicos:
        if chave not in texto:
            avisos.append(f"POP: tópico não encontrado na minuta: {rotulo}.")

    # A palavra "minuta" no título não basta. A frase precisa dizer que ainda não foi aprovada.
    if "nao aprovad" not in texto and "nao vigente" not in texto:
        avisos.append("POP: a minuta não está identificada como proposta não aprovada.")

    parece_vigente = re.search(r"\b(pop|procedimento|minuta)\s+aprovad|\bvigente\b", texto) is not None
    nega_vigencia = "nao vigente" in texto or "nao aprovad" in texto
    if parece_vigente and not nega_vigencia:
        avisos.append("POP: o texto pode apresentar a minuta como aprovada ou vigente.")
    return avisos


def validar_separacao(resposta):
    # Só verifica se os rótulos fatos e hipóteses aparecem. Não julga se a classificação está correta.
    secao = sem_acento(extrair_secao(resposta, 4))
    if not secao:
        return []
    if "fato" not in secao or "hipotese" not in secao:
        return ["Gargalos: a seção não separa, pelos rótulos, fatos e hipóteses."]
    return []


def _termo_afirmado(texto, padrao):
    # Ignora o termo quando a frase próxima só diz que a informação não existe ou não foi descrita.
    for encontrado in re.finditer(padrao, texto or ""):
        inicio = max(0, encontrado.start() - 90)
        janela = texto[inicio : encontrado.end()]
        if re.search(r"nao\s+(foram|ha|existe|possui|descreve)|sem\s+informac|nao\s+disponibil|nao\s+presum", janela):
            continue
        return True
    return False


def indicios_fidelidade(origem, contexto, resposta):
    # Compara expressões de risco com o material. Um indício não comprova que houve invenção.
    avisos = []
    material = sem_acento(f"{origem or ''}\n{contexto or ''}")
    trecho = sem_acento(_juntar_secoes(resposta, SECOES_AFIRMACAO))
    if not trecho:
        return ["Não foi possível isolar as seções para procurar indícios de extrapolação."]

    # Procura "a chefia aprova", e não uma frase que apenas nega a aprovação.
    for encontrado in re.finditer(
        r"chefia(?:\s+\w+){0,4}\s+aprov\w*|aprovad[oa]\s+pel[oa]\s+chefia",
        trecho,
    ):
        frase = encontrado.group(0)
        if re.search(r"\bnao\b|\bsem\b", frase):
            continue
        if "aprov" not in material:
            avisos.append(
                "Indício, não prova: a chefia aparece como quem aprova, e o material não fala em aprovação."
            )
            break

    if re.search(r"\d+\s*(dias|horas)\b", trecho) and re.search(r"\d+\s*(dias|horas)\b", material) is None:
        avisos.append("Indício, não prova: há prazo numérico que não aparece no material de origem.")

    # "Não são controles oficiais" é uma negação. Só a afirmação sem essa ressalva gera indício.
    for encontrado in re.finditer(r"controles?\s+oficiais?", trecho):
        inicio = max(0, encontrado.start() - 24)
        janela = trecho[inicio : encontrado.end()]
        if re.search(r"nao\s+(sao|e|foram|sera|serao)\s+controles?\s+oficiais?", janela):
            continue
        if "oficial" not in material:
            avisos.append(
                "Indício, não prova: um controle foi chamado de oficial sem essa qualificação no material."
            )
            break

    periodo_alterado = re.search(r"periodo\s+.{0,50}(reduzid|alterad|encurtad)", trecho) is not None
    periodo_no_material = re.search(r"periodo\s+.{0,50}(reduzid|alterad|encurtad)", material) is not None
    if periodo_alterado and not periodo_no_material:
        avisos.append("Indício, não prova: o período pretendido aparece como reduzido ou alterado.")

    # O material pode citar automação só para dizer que ela não foi descrita. Isso não é uma funcionalidade.
    if _termo_afirmado(trecho, r"\bautomacao\b|\bautomatiz\w*|\bworkflow automatico\b|\bnotificacao automatica\b"):
        if not _termo_afirmado(material, r"\bautomacao\b|\bautomatiz\w*|\bworkflow\b|\bnotificacao automatica\b"):
            avisos.append("Indício, não prova: há funcionalidade sistêmica que o material não descreve.")

    cita_norma = re.search(r"\bart\.?\s*\d+|\blei\s+n|\bdecreto\s+n", trecho) is not None
    norma_no_material = re.search(r"\bart\.?\s*\d+|\blei\s+n|\bdecreto\s+n", material) is not None
    if cita_norma and not norma_no_material:
        avisos.append("Indício, não prova: há norma, artigo ou decreto que não consta no material.")

    nega_formulario = "nao existe um formulario" in material or "nao ha formulario" in material
    afirma_formulario = re.search(r"formulario padronizado", trecho) is not None
    nega_no_relatorio = re.search(r"nao existe|nao ha formulario|sem formulario", trecho) is not None
    if nega_formulario and afirma_formulario and not nega_no_relatorio:
        avisos.append(
            "Indício, não prova: o material diz que não há formulário padronizado, mas o relatório pode tratá-lo como existente."
        )
    return avisos


def validar_resposta(resposta, origem="", contexto=""):
    # Reúne as checagens. A lista vazia não autoriza usar o relatório sem revisão humana.
    if not (resposta or "").strip():
        return ["A IA não retornou conteúdo."]

    avisos = []
    avisos.extend(validar_secoes(resposta))
    avisos.extend(validar_mermaid(resposta))
    avisos.extend(validar_indicadores(resposta))
    avisos.extend(validar_pop(resposta))
    avisos.extend(validar_separacao(resposta))
    avisos.extend(indicios_fidelidade(origem, contexto, resposta))

    unicos = []
    for aviso in avisos:
        if aviso not in unicos:
            unicos.append(aviso)
    return unicos
