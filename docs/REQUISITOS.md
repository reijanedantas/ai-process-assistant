# Requisitos — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026  
**Status:** Requisitos de referência; implementação parcial

## 1. Requisitos funcionais

| ID | Requisito | Situação verificada |
|---|---|---|
| RF-01 | Receber descrição textual de processo | Implementado no protótipo |
| RF-02 | Receber PDF, DOCX e TXT | Implementado no protótipo, sujeito aos limites documentados |
| RF-03 | Consultar Gemini para gerar análise | Implementado no protótipo; depende de chave e disponibilidade da API |
| RF-04 | Gerar relatório estruturado em português | Implementado no protótipo |
| RF-05 | Separar fatos, hipóteses e lacunas | Previsto no prompt; exige revisão humana |
| RF-06 | Sugerir riscos, melhorias, POP, indicadores e fluxograma | Implementado no protótipo como geração por IA |
| RF-07 | Executar validações locais | Implementado em validacao.py |
| RF-08 | Exportar relatório | Implementado para Markdown |
| RF-09 | Cadastrar e recuperar processos de forma persistente | Planejado; banco ainda não integrado |
| RF-10 | Versionar análises sem sobrescrever versões anteriores | Planejado |
| RF-11 | Acompanhar status de melhorias ao longo do tempo | Planejado |
| RF-12 | Registrar eventos e decisões | Planejado |
| RF-13 | Registrar medições históricas de indicadores | Planejado |
| RF-14 | Disponibilizar dados para Power BI | Planejado |
| RF-15 | Autenticação e controle de acesso | Planejado; não implementado |

## 2. Requisitos não funcionais

- **Segurança:** chaves fora do código e do Git; não enviar dados sensíveis sem autorização.
- **Privacidade:** informar que o conteúdo submetido à análise é transmitido ao provedor da API.
- **Confiabilidade:** tratar falhas de leitura e de API sem expor segredos.
- **Transparência:** mostrar limites das validações automáticas e identificar propostas como propostas.
- **Manutenibilidade:** separar interface, validações, dados e integrações.
- **Rastreabilidade:** preservar versões e eventos quando a persistência for implementada.
- **Custo:** priorizar planos e recursos gratuitos; não ativar cobrança sem aprovação.
- **Usabilidade:** apresentar mensagens claras e orientações compreensíveis.

## 3. Limites conhecidos do protótipo

- Limites de texto, contexto e tamanho de arquivo são definidos em app.py.
- A leitura de PDF pode ser limitada a um número máximo de páginas.
- PDF digitalizado sem camada de texto pode não fornecer conteúdo extraível.
- As validações locais verificam estrutura e padrões; não comprovam correção semântica, legal ou operacional.
- Os testes locais não comprovam disponibilidade da API Gemini nem integração com banco de dados.

## 4. Critérios de aceite

Cada requisito deve ter evidência de código, teste ou demonstração. Itens planejados não podem ser marcados como implementados apenas por constarem neste documento.
