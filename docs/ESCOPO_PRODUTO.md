# Escopo do produto — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026  
**Status:** Base aprovada para orientar o desenvolvimento  
**Repositório:** https://github.com/reijanedantas/ai-process-assistant

## 1. Visão do produto

O AI Process Assistant é uma aplicação de apoio à análise, diagnóstico, documentação e melhoria de processos. A ferramenta recebe uma descrição e/ou documento de referência, utiliza IA para estruturar uma análise e apresenta um relatório que precisa ser revisado por uma pessoa.

O produto não substitui gestores, responsáveis pelo processo, especialistas, áreas jurídicas ou instâncias de aprovação.

## 2. Problema que pretende resolver

Processos frequentemente são descritos de forma dispersa, sem padronização suficiente para identificar etapas, responsabilidades, riscos, gargalos, oportunidades de melhoria e indicadores. A ferramenta busca organizar essas informações e facilitar sua análise.

## 3. Público e contexto de uso

Pessoas e equipes que precisam compreender, documentar, revisar ou melhorar processos administrativos e organizacionais. A aplicação deve ser validada com dados fictícios ou anonimizados antes de qualquer uso institucional.

## 4. Escopo funcional previsto

1. Receber descrição textual do processo.
2. Ler arquivos PDF, DOCX e TXT dentro dos limites definidos pela aplicação.
3. Gerar análise estruturada com resumo, objetivo, etapas e responsáveis identificados.
4. Separar fatos fornecidos de hipóteses e lacunas.
5. Identificar possíveis gargalos e riscos, sem tratar hipóteses como fatos.
6. Sugerir melhorias com impacto, esforço e justificativa.
7. Propor um fluxo melhorado e uma minuta de POP claramente não aprovada e não vigente.
8. Sugerir indicadores, fórmulas, dados necessários e critérios de contagem.
9. Gerar fluxograma em Mermaid.
10. Executar verificações locais de estrutura e alguns indícios de extrapolação.
11. Permitir revisão humana e exportação do relatório.
12. Em fases futuras, manter histórico, versões de análises, melhorias, eventos e medições de indicadores.
13. Em fases futuras, disponibilizar dados estruturados para Power BI.

## 5. Fora do escopo atual

- Aprovação automática de processos, POPs ou recomendações.
- Declaração automática de conformidade jurídica ou normativa.
- Substituição de sistemas oficiais de gestão.
- Tomada de decisão administrativa autônoma.
- Integração institucional sem autorização formal.
- Gestão de carreira e recolocação profissional: esse é um produto separado e não deve ser incorporado a este repositório.

## 6. Princípios do produto

- Preservar os fatos de origem.
- Identificar claramente hipóteses, recomendações e lacunas.
- Manter decisão humana em todas as aprovações.
- Priorizar soluções simples e de baixo custo.
- Proteger dados, credenciais e documentos.
- Preservar histórico e rastreabilidade quando a persistência for implementada.
- Não apresentar funcionalidade planejada como se estivesse pronta.

## 7. Critério de conclusão

Uma funcionalidade só será considerada concluída quando houver implementação no repositório, teste adequado e evidência verificável. Documentação aprovada não significa implementação concluída.
