# Roadmap — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026  
**Status:** Planejamento de execução

| Fase | Entrega | Situação |
|---|---|---|
| 1 | Protótipo Streamlit, leitura de arquivos, Gemini e validação local | Implementado parcialmente; conferir testes e execução no ambiente |
| 2 | Conectar aplicação ao Neon PostgreSQL e criar esquema | Pendente |
| 3 | CRUD de processos e análises com versionamento | Pendente |
| 4 | Histórico de eventos, status de melhorias e medições | Pendente |
| 5 | Reforçar validações, proveniência e revisão humana | Parcial no protótipo; evolução pendente |
| 6 | Relatórios DOCX, PDF, XLSX e CSV | Pendente; Markdown já disponível |
| 7 | Views/exportações e integração com Power BI | Pendente |
| 8 | Autenticação, autorização, backup e preparação para produção | Pendente |

## Critérios de passagem

Uma fase só será encerrada quando houver código publicado, testes executados, documentação atualizada e evidência da funcionalidade. A criação de um projeto no provedor não equivale à integração da aplicação.

## Prioridade imediata

1. Confirmar o estado local do projeto e sincronização com main.
2. Preparar configuração segura da conexão PostgreSQL.
3. Testar conectividade sem expor a URL de conexão.
4. Implementar e testar o esquema de dados.
5. Construir persistência antes de ampliar o dashboard.
