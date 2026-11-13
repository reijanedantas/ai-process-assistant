# Testes e evidências — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026

## 1. Testes existentes no repositório

- test_validacao.py: testes das checagens locais do relatório.
- test_arquivos.py: testes de leitura de arquivos e comportamento associado, conforme o conteúdo do arquivo de testes.
- A execução local é feita com:

```powershell
python -m unittest -v
```

## 2. O que os testes unitários não comprovam

Os testes que não chamam serviços externos não comprovam:
- disponibilidade ou autenticação da Gemini API;
- qualidade semântica de uma resposta real do modelo;
- conexão com Neon PostgreSQL;
- persistência e recuperação de registros;
- integração com Power BI;
- segurança de uma implantação pública.

## 3. Evidências necessárias para as próximas fases

| Área | Evidência necessária |
|---|---|
| Aplicação | Inicialização local sem erro |
| Arquivos | Testes para PDF, DOCX, TXT, arquivos inválidos e limites |
| Gemini | Teste controlado com chave protegida e modelo disponível |
| Banco | Teste de conexão e CRUD com dados fictícios |
| Versionamento | Teste que confirme preservação de análises anteriores |
| Melhorias | Teste de transição de status e histórico |
| Indicadores | Teste de múltiplas medições por período |
| Power BI | Validação de consultas/views ou exportação estruturada |

## 4. Estado desta revisão

Esta atualização foi feita por leitura do conteúdo publicado no GitHub. Não foi executada a suíte de testes no computador local da responsável. Portanto, nenhum novo teste está declarado como aprovado nesta alteração documental.
