# Arquitetura — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026  
**Status:** Arquitetura-alvo com separação entre componentes existentes e planejados

## 1. Arquitetura atualmente publicada

- **Interface:** Streamlit.
- **Linguagem:** Python.
- **Modelo de IA:** Gemini API, configurado em app.py.
- **Leitura de documentos:** pypdf e python-docx.
- **Validação local:** módulo validacao.py.
- **Demonstração:** exemplo fictício em exemplo.py.
- **Persistência:** ainda não implementada.
- **Relatórios:** exportação Markdown no protótipo.
- **BI:** integração Power BI ainda não implementada.

## 2. Arquitetura-alvo

1. Interface Streamlit recebe dados e arquivos.
2. Camada de entrada valida tipo, tamanho e conteúdo extraído.
3. Serviço de análise monta instruções e consulta o provedor de IA.
4. Camada de validação executa verificações locais e apresenta alertas.
5. Pessoa usuária revisa, corrige e decide o que será aceito.
6. Camada de aplicação grava processos, análises e eventos no PostgreSQL.
7. Consultas e views disponibilizam dados estruturados para relatórios e Power BI.

## 3. Tecnologias previstas

| Tecnologia | Responsabilidade | Situação |
|---|---|---|
| Python | Lógica da aplicação | Em uso |
| Streamlit | Interface web | Em uso |
| Google Gemini API | Geração de análises | Em uso no protótipo |
| pypdf | Extração de texto PDF | Em uso |
| python-docx | Extração de DOCX | Em uso |
| Neon PostgreSQL | Persistência | Projeto criado; conexão não implementada |
| SQLAlchemy e driver PostgreSQL | Acesso ao banco | A avaliar/implementar |
| GitHub | Código e documentação versionados | Em uso |
| Power BI Desktop | Visualização e indicadores | Protótipo separado com dados de demonstração |

## 4. Segurança de configuração

- A chave Gemini deve ser fornecida por variável de ambiente ou Streamlit Secrets.
- O arquivo .streamlit/secrets.toml não deve ser versionado.
- A URL de conexão PostgreSQL deve ficar em segredo local ou no gerenciador de segredos do ambiente de implantação.
- Nunca publicar senhas, tokens, chaves ou dados reais sensíveis.
- Utilizar dados fictícios ou anonimizados durante desenvolvimento.

## 5. Limites e decisões

A assinatura Google AI Plus é um benefício para uso das ferramentas Google conforme os termos do plano. Ela não deve ser tratada como crédito automático para chamadas da Gemini API. A API possui regras de cota e faturamento próprias.

O modelo configurado no protótipo é gemini-3.5-flash-lite. A documentação oficial consultada em 13/11/2026 lista esse endpoint como modelo estável. Alterações futuras devem ser precedidas por teste de compatibilidade, qualidade e custo.

## 6. Evolução arquitetural

A integração PostgreSQL deve ser implementada em uma etapa isolada, com teste de conexão, esquema versionado, migrações, repositórios e testes. Não se deve misturar credenciais de banco ao código-fonte.
