# Decisões técnicas — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026

## Registro de decisões

### DEC-001 — Manter Python e Streamlit no protótipo
**Decisão:** manter a base atual.  
**Motivo:** já existe aplicação funcional e testável.  
**Estado:** em uso.

### DEC-002 — Utilizar Gemini API para análise
**Decisão:** manter integração atual com a API Gemini.  
**Motivo:** atende à geração de análise textual no protótipo.  
**Estado:** implementado no protótipo; chave e disponibilidade externa são pré-requisitos.

### DEC-003 — Modelo gemini-3.5-flash-lite
**Decisão:** manter temporariamente o endpoint configurado.  
**Motivo:** a documentação oficial consultada em 13/11/2026 lista o modelo como estável e otimizado para tarefas de alto volume e custo/latência reduzidos.  
**Estado:** configurado; não equivale a teste de chamada bem-sucedida nesta revisão.  
**Revisão:** comparar qualidade, limites e preço antes de qualquer migração.

### DEC-004 — Neon PostgreSQL para persistência
**Decisão:** utilizar o projeto Neon já criado como banco planejado.  
**Motivo:** PostgreSQL gerenciado e região São Paulo escolhida.  
**Estado:** projeto criado; aplicação ainda não conectada.

### DEC-005 — Preservar versões de análise
**Decisão:** não sobrescrever análises anteriores.  
**Motivo:** permitir comparação e rastreabilidade.

### DEC-006 — Melhorias independentes da versão de análise
**Decisão:** cada melhoria referencia o processo e a análise de origem.  
**Motivo:** permitir que o acompanhamento continue após novas análises.

### DEC-007 — Medições históricas separadas
**Decisão:** armazenar cada medição em indicator_measurements.  
**Motivo:** preservar evolução temporal dos indicadores.

### DEC-008 — Decisão humana obrigatória
**Decisão:** sugestões da IA não aprovam processos, POPs ou melhorias.  
**Motivo:** responsabilidade e governança.

### DEC-009 — Assinatura Google AI Plus não é crédito de API
**Decisão:** usar a assinatura como apoio ao desenvolvimento, sem presumir cobertura de chamadas da Gemini API.  
**Motivo:** assinatura de produto e faturamento de API são mecanismos distintos.  
**Estado:** regra de custos aprovada.

### DEC-010 — Separação do produto de carreira
**Decisão:** Gestão de Carreira/Recolocação Profissional terá produto e repositório separados.  
**Motivo:** escopos, dados e jornadas diferentes.

## Processo para novas decisões

Toda decisão relevante deve registrar identificador, data, contexto, alternativas consideradas, decisão, justificativa, impacto e estado. Decisões substituídas não devem ser apagadas; devem ser marcadas como supersedidas.
