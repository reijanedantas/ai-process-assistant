# AI Process Assistant

Assistente de IA para análise, diagnóstico, documentação e melhoria de processos. O protótipo recebe uma descrição ou arquivo PDF, DOCX ou TXT, consulta a Gemini API e apresenta um relatório em Markdown para revisão humana.

> **Estado do produto:** protótipo funcional publicado. Persistência PostgreSQL, histórico de análises, relatórios avançados, integração automática com Power BI e autenticação ainda são evoluções planejadas.

## O que o protótipo faz

- Recebe descrição textual de um processo.
- Lê arquivos PDF, DOCX e TXT, com limites de tamanho e páginas.
- Consulta a Gemini API.
- Gera relatório com resumo, objetivo, etapas, fatos, hipóteses, riscos, melhorias, proposta de processo, minuta de POP, indicadores, perguntas de validação e fluxograma Mermaid.
- Executa checagens locais de estrutura e indícios sem nova chamada à IA.
- Disponibiliza um exemplo fictício de solicitação de férias.
- Permite baixar o relatório em Markdown.

A checagem local não comprova fidelidade semântica, correção jurídica, gramatical ou técnica. Toda análise exige revisão humana antes de ser usada como procedimento, controle ou decisão.

## Documentação oficial do projeto

A pasta docs/ contém a documentação versionada:

| Documento | Conteúdo |
|---|---|
| [Escopo do produto](docs/ESCOPO_PRODUTO.md) | Objetivo, dores, público, limites e funcionalidades |
| [Requisitos](docs/REQUISITOS.md) | Requisitos funcionais, não funcionais e regras de negócio |
| [Arquitetura](docs/ARQUITETURA.md) | Arquitetura publicada e arquitetura-alvo |
| [Modelo de dados](docs/MODELO_DADOS.md) | Entidades e relacionamentos planejados |
| [Decisões técnicas](docs/DECISOES_TECNICAS.md) | Decisões e justificativas |
| [Ferramentas Google e custos](docs/FERRAMENTAS_GOOGLE_E_CUSTOS.md) | Uso do Google AI Plus, API e controle de custos |
| [Roadmap](docs/ROADMAP.md) | Fases e situação das entregas |
| [Changelog](docs/CHANGELOG.md) | Histórico de mudanças |
| [Testes](docs/TESTES.md) | Estratégia, comandos e limitações |

## Situação técnica atual

| Componente | Situação |
|---|---|
| Python + Streamlit | Implementado no protótipo |
| Gemini API | Chamada implementada; depende de chave, disponibilidade e condições da API |
| Leitura PDF/DOCX/TXT | Implementada no protótipo |
| Validação local | Implementada; não é prova de correção |
| Testes automatizados | Arquivos de teste presentes; execute localmente para confirmar o estado atual |
| Neon PostgreSQL | Projeto criado; conexão e persistência ainda não implementadas |
| Power BI | PBIX demonstrativo separado; integração automática ainda não implementada |
| Autenticação e autorização | Planejadas |

## Organização dos arquivos

| Arquivo | Função |
|---|---|
| app.py | Interface Streamlit, leitura de arquivos e chamada ao Gemini |
| validacao.py | Checagens locais do relatório |
| exemplo.py | Caso fictício usado na demonstração |
| test_arquivos.py | Testes de leitura de arquivos e chamada |
| test_validacao.py | Testes das checagens do relatório |
| requirements.txt | Dependências Python |
| docs/ | Documentação oficial versionada |

## Requisitos

- Python 3.11 ou superior.
- Chave de API Gemini.
- Internet para consultar a API.

## Instalação

Na pasta do projeto, execute no PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se o PowerShell bloquear a ativação:

```cmd
.venv\Scripts\activate.bat
```

Copie .streamlit/secrets.toml.example para .streamlit/secrets.toml e substitua o valor de exemplo pela chave. O arquivo de segredos não deve ser enviado ao Git.

Também é possível informar a chave somente na sessão do terminal:

```powershell
$env:GEMINI_API_KEY = "SUA_CHAVE_AQUI"
streamlit run app.py
```

## Demonstração

1. Execute a instalação e configure a chave Gemini.
2. Inicie o aplicativo com streamlit run app.py.
3. Clique em **Carregar exemplo fictício de férias**.
4. Clique em **Analisar processo com IA**.
5. Revise o relatório e os alertas antes de baixar ou reutilizar o conteúdo.

## Testes

Execute:

```powershell
python -m unittest -v
```

Os testes locais não chamam a Gemini API e não precisam de chave. Eles verificam funções locais com dados fictícios. Consulte docs/TESTES.md para limitações e próximos testes.

## Segurança e privacidade

- Não publique .streamlit/secrets.toml, chaves, senhas, tokens ou strings de conexão.
- Não coloque credenciais no código.
- Não use git add -f em arquivos de segredos.
- Não utilize dados pessoais, funcionais, sigilosos ou de clientes sem autorização e avaliação adequada.
- O texto enviado para análise é transmitido à Gemini API; avalie os termos e a política aplicável antes de enviar qualquer informação.
- Durante o desenvolvimento, prefira dados fictícios ou anonimizados.

## Google AI Plus e custos da API

A assinatura Google AI Plus pode apoiar o desenvolvimento por meio dos recursos incluídos no plano, como Gemini e NotebookLM. Ela **não deve ser considerada crédito automático para chamadas da Gemini API**. A API possui cotas e regras de faturamento próprias. Consulte docs/FERRAMENTAS_GOOGLE_E_CUSTOS.md antes de habilitar qualquer recurso pago.

## Publicação online

Para publicar no Streamlit Community Cloud, conecte o repositório, selecione app.py e cadastre a chave em Secrets da plataforma:

```toml
GEMINI_API_KEY = "SUA_CHAVE_GEMINI"
```

A chave deve permanecer nas configurações de segredos da plataforma, nunca em arquivo versionado.

## Limitações e responsabilidade

O protótipo não possui persistência de processos em banco, histórico de análises, autenticação, autorização nem integração automática com Power BI. A checagem local procura seções, tópicos, termos e indícios; não julga integralmente o conteúdo. A sintaxe Mermaid é verificada por regras locais, sem substituir um compilador Mermaid.

Toda sugestão, indicador, minuta, risco ou fluxograma precisa ser revisado por pessoa responsável. O produto não aprova automaticamente procedimentos nem declara conformidade legal.

O repositório não inclui licença. Reutilização por terceiros depende de uma decisão explícita sobre licenciamento.
