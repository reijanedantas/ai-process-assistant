# Testes locais das checagens. Não chamam a API Gemini e não usam chave.
import unittest

from exemplo import CONTEXTO_FERIAS, DESCRICAO_FERIAS
from validacao import validar_resposta


def _relatorio_fiel():
    # Relatório fictício, escrito para o teste. Não é resposta do modelo.
    return """
1. RESUMO DO PROCESSO
O servidor encaminha o pedido por e-mail à chefia imediata e indica o período pretendido.
A chefia imediata analisa a compatibilidade com o planejamento e encaminha o pedido ao RH.
O RH consulta o saldo no sistema de gestão de pessoas. Se há inconsistência, devolve o pedido à chefia.
Se não há inconsistência, registra a programação e confirma o registro ao servidor.
Não existe formulário padronizado. Não há prazos formalmente definidos. Parte dos controles usa planilhas.
Responsável por várias etapas: Não informado.

2. OBJETIVO E RESULTADO ESPERADO
Objetivo da análise: diagnosticar e melhorar o processo.
Situação atual: pedidos por e-mail, sem formulário padronizado.
Resultado esperado com as melhorias: Necessita de validação. Não é situação já existente.

3. ETAPAS IDENTIFICADAS
| Número | Atividade | Responsável | Informação complementar |
| --- | --- | --- | --- |
| 1 | Encaminhar o pedido por e-mail, com o período pretendido | Servidor | Não informado |
| 2 | Analisar a compatibilidade com o planejamento | Chefia imediata | Não é registro de aprovação |
| 3 | Encaminhar o pedido ao RH | Chefia imediata | Não informado |
| 4 | Consultar o saldo e verificar a consistência | RH | Sistema de gestão de pessoas |
| 5 | Devolver a solicitação à chefia quando há inconsistência | RH | Correção ou esclarecimento |
| 6 | Registrar a programação e confirmar o registro | RH | Quando não há inconsistência |

4. GARGALOS E RISCOS
A. Fatos identificados no material.
Não existe formulário padronizado. Não há prazos definidos. Parte dos controles está em planilhas.
B. Hipóteses que precisam de validação.
A falta de prazo pode dificultar o acompanhamento. Isso não está comprovado no material.

5. MELHORIAS PROPOSTAS
| Melhoria proposta | Problema relacionado | Impacto | Esforço | Justificativa |
| --- | --- | --- | --- | --- |
| Definir um formulário ainda inexistente | Não existe formulário padronizado | Médio | Baixo | Proposta, não fato atual |
Use [prazo a definir]. Não elimine a planilha antes de verificar o sistema.

6. PROPOSTA DE PROCESSO MELHORADO
Proposta, ainda não implantada. Preservar a sequência atual e marcar etapas novas como proposta.
Não criar aprovação da chefia. Responsável de etapa nova: [responsável a confirmar].

7. MINUTA DE PROCEDIMENTO OPERACIONAL PADRÃO (POP)
Minuta não aprovada e não vigente.
Objetivo: orientar o registro do pedido já descrito.
Escopo: solicitação de férias informada no material.
Responsáveis: servidor, chefia imediata e RH. Demais responsáveis: [responsável a confirmar].
Procedimento passo a passo: repetir somente as etapas identificadas.
Registros e controles: e-mail, planilhas e registro no sistema. Não são controles oficiais.
Pontos pendentes de validação: normas aplicáveis, prazos e funcionalidades do sistema.

8. INDICADORES DE DESEMPENHO
Tempo médio de atendimento.
Finalidade: acompanhar a duração das solicitações concluídas.
Fórmula: Tempo médio = soma dos tempos individuais das solicitações concluídas / quantidade de solicitações concluídas.
Unidade de medida: dias. Não misturar horas corridas com horas úteis.
Dados necessários: data e hora de recebimento e de confirmação da conclusão. Sem essas datas, o cálculo depende da coleta.
Periodicidade sugerida: Necessita de validação.
Critério de contagem: somente solicitações concluídas.
Cuidados de interpretação: não calcular sem os registros.

Taxa de retrabalho.
Finalidade: acompanhar solicitações devolvidas.
Fórmula: Taxa de retrabalho (%) = (quantidade de solicitações devolvidas pelo menos uma vez / quantidade total de solicitações recebidas no período) x 100.
Cada solicitação devolvida conta uma vez no numerador. Não usar a quantidade de devoluções como numerador.
Numerador e denominador usam o mesmo período de referência.
Dados necessários: registro das devoluções e o total recebido no período. Se faltarem, informar a necessidade de coleta.

9. PERGUNTAS PARA VALIDAÇÃO
Quais normas se aplicam? Quais permissões o sistema possui? Onde os registros devem ser guardados?

10. FLUXOGRAMA MERMAID
O desenho cobre somente as etapas descritas. A decisão abaixo é a inconsistência já informada.

```mermaid
flowchart TD
    A[Encaminhar pedido por e-mail] --> B[Analisar compatibilidade]
    B --> C[Encaminhar ao RH]
    C --> D{Ha inconsistencia?}
    D -->|Sim| E[Devolver a chefia]
    D -->|Não| F[Registrar programacao]
    E --> B
```
"""


def _relatorio_infiel():
    # Relatório fictício que viola os critérios do caso de férias.
    return """
1. RESUMO DO PROCESSO
A chefia imediata aprova formalmente o pedido. O período pretendido foi reduzido.
O formulário padronizado é utilizado. Os controles oficiais estão em planilhas.
O prazo de cada etapa é de 5 dias. A automação do sistema envia a decisão.
Conforme a Lei nº 8112, o registro é automático.

2. OBJETIVO E RESULTADO ESPERADO
Situação atual já com o processo melhorado em vigor.

3. ETAPAS IDENTIFICADAS
| Número | Atividade | Responsável | Informação complementar |
| --- | --- | --- | --- |
| 1 | Aprovar o pedido | Chefia | Aprovação formal |

4. GARGALOS E RISCOS
Há demora. Sem separar fatos e hipóteses.

5. MELHORIAS PROPOSTAS
Eliminar as planilhas porque o sistema já automatiza tudo.

6. PROPOSTA DE PROCESSO MELHORADO
A chefia aprova e o sistema conclui sozinho.

7. MINUTA DE PROCEDIMENTO OPERACIONAL PADRÃO (POP)
POP aprovado e vigente.

8. INDICADORES DE DESEMPENHO
Taxa de retrabalho = quantidade de devoluções / quantidade de solicitações.

9. PERGUNTAS PARA VALIDAÇÃO
Nenhuma.

10. FLUXOGRAMA MERMAID
Mermaid flowchart
"""


class ValidacaoRelatorioTeste(unittest.TestCase):
    def test_relatorio_fiel_nao_dispara_avisos(self):
        # O texto fiel é um fixture. Passar aqui não significa que o modelo produzirá o mesmo texto.
        avisos = validar_resposta(_relatorio_fiel(), DESCRICAO_FERIAS, CONTEXTO_FERIAS)
        self.assertEqual(avisos, [])

    def test_relatorio_infiel_aponta_indicios_e_falhas(self):
        avisos = validar_resposta(_relatorio_infiel(), DESCRICAO_FERIAS, CONTEXTO_FERIAS)
        texto = " ".join(avisos).lower()
        self.assertIn("chefia", texto)
        self.assertIn("prazo numérico", texto)
        self.assertIn("oficial", texto)
        self.assertIn("reduzido ou alterado", texto)
        self.assertIn("funcionalidade", texto)
        self.assertIn("norma", texto)
        self.assertIn("formulário", texto)
        self.assertIn("mermaid", texto)
        self.assertIn("devoluções", texto)
        self.assertIn("não aprovada", texto)

    def test_bloco_mermaid_sem_caminhos_gera_aviso(self):
        resposta = _relatorio_fiel().replace(
            "```mermaid\nflowchart TD\n    A[Encaminhar pedido por e-mail] --> B[Analisar compatibilidade]\n"
            "    B --> C[Encaminhar ao RH]\n    C --> D{Ha inconsistencia?}\n"
            "    D -->|Sim| E[Devolver a chefia]\n    D -->|Não| F[Registrar programacao]\n    E --> B\n```",
            "```mermaid\nflowchart TD\n    A[Encaminhar pedido] --> B{Segue?}\n```",
        )
        avisos = validar_resposta(resposta, DESCRICAO_FERIAS, CONTEXTO_FERIAS)
        self.assertTrue(any("Sim e Não" in aviso for aviso in avisos))

    def test_extrapolacoes_do_caso_de_ferias_geram_indicio(self):
        # Reproduz o tipo de frase que passou na checagem antiga e não está no material.
        resposta = _relatorio_fiel().replace(
            "Não criar aprovação da chefia.",
            "Parecer da chefia sobre o pedido validado. Devolver ao servidor para ajuste do período. "
            "Consultar dentro do prazo normativo. Rastreabilidade garantida.",
        ).replace(
            "Minuta não aprovada e não vigente.",
            "Minuta não aprovada e não vigente.\nObjetivo: normatizar o procedimento.",
        ).replace(
            "Parte dos controles está em planilhas.",
            "Parte dos controles está em planilhas, podendo causar atraso.",
        )
        texto = " ".join(validar_resposta(resposta, DESCRICAO_FERIAS, CONTEXTO_FERIAS)).lower()
        self.assertIn("parecer", texto)
        self.assertIn("validado", texto)
        self.assertIn("servidor", texto)
        self.assertIn("normativo", texto)
        self.assertIn("normatiz", texto)
        self.assertIn("garantida", texto)
        self.assertIn("pode ou podendo", texto)

    def test_automacao_citada_como_pendencia_nao_e_indicio(self):
        # Perguntar ou listar automação como ponto pendente não é dizer que o sistema já faz isso.
        resposta = _relatorio_fiel().replace(
            "Pontos pendentes de validação: normas aplicáveis, prazos e funcionalidades do sistema.",
            "Pontos pendentes de validação: funcionalidades de automação do sistema.",
        )
        texto = " ".join(validar_resposta(resposta, DESCRICAO_FERIAS, CONTEXTO_FERIAS)).lower()
        self.assertNotIn("funcionalidade sistêmica", texto)

    def test_resposta_vazia(self):
        self.assertEqual(validar_resposta("  "), ["A IA não retornou conteúdo."])


if __name__ == "__main__":
    unittest.main()
