# AI Process Assistant

Protótipo para analisar um processo e devolver um relatório que uma pessoa consegue revisar.

A pessoa descreve a rotina ou envia um PDF, DOCX ou TXT. O programa consulta o Gemini e monta um relatório em Markdown. Uma checagem local, feita no próprio Python e sem nova chamada à IA, aponta lacunas de estrutura e alguns indícios de extrapolação. Essa checagem não comprova que o relatório está fiel ou tecnicamente correto.

## O que o relatório contém

- Resumo do processo e objetivo da análise
- Etapas, com atividade, responsável e complemento
- Fatos separados de hipóteses
- Melhorias, com problema, impacto, esforço e justificativa
- Proposta de processo, com ponto de decisão quando o material tiver um
- Minuta de procedimento, sempre identificada como não aprovada e não vigente
- Dois indicadores, com fórmula, unidade, dados necessários e critério de contagem
- Perguntas para validar o que o material não informou
- Fluxograma em Mermaid, com o código visível para revisão

Há um exemplo fictício de solicitação de férias. Ele não usa dados de pessoas, órgãos ou clientes.

## Como demonstrar

1. Siga a instalação abaixo e execute o aplicativo.
2. Clique em **Carregar exemplo fictício de férias**.
3. Clique em **Analisar processo com IA**.

A análise só é gerada depois que a chave Gemini estiver configurada. O relatório pode ser baixado em Markdown.

## Organização

| Arquivo | Função |
| --- | --- |
| `app.py` | Interface Streamlit, leitura de arquivos e chamada ao Gemini |
| `validacao.py` | Checagens locais do relatório |
| `exemplo.py` | Caso fictício usado no botão de demonstração |
| `test_arquivos.py` | Testes da leitura de arquivos e da chamada |
| `test_validacao.py` | Testes das checagens do relatório |
| `requirements.txt` | Dependências |

## Requisitos

- Python 3.11 ou superior
- Chave de API Gemini
- Internet para consultar a API

## Instalação

Na pasta do projeto:

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

Copie `.streamlit/secrets.toml.example` para `.streamlit/secrets.toml` e substitua o texto de exemplo pela chave. O arquivo de segredos fica fora do Git.

Também é possível informar a chave só na sessão do terminal:

```powershell
$env:GEMINI_API_KEY = "SUA_CHAVE_AQUI"
streamlit run app.py
```

## Verificação

```powershell
python -m unittest -v
```

Os testes não chamam a API Gemini e não precisam de chave. Eles conferem a leitura dos arquivos e as checagens do relatório com textos fictícios.

## Segurança

- Não publique `.streamlit/secrets.toml`, chaves, senhas ou tokens.
- O `.gitignore` exclui `.streamlit/secrets.toml` e arquivos `.env`.
- Não coloque a chave no código.
- Não use `git add -f` no arquivo de segredos.
- Não use dados pessoais, funcionais, sigilosos ou de clientes na demonstração.
- O texto enviado para análise é transmitido à API Gemini.

O repositório não inclui licença. Quem quiser permitir reutilização precisa escolher uma.

## Publicar uma demonstração online

No Streamlit Community Cloud, conecte este repositório, selecione `app.py` e cadastre a chave nas Secrets da plataforma:

```toml
GEMINI_API_KEY = "SUA_CHAVE_GEMINI"
```

A chave fica nas configurações da plataforma, não em um arquivo versionado.

## Limitações

A checagem local procura seções, tópicos da minuta, termos das duas fórmulas, um bloco Mermaid e alguns indícios de extrapolação. Ela não comprova fidelidade ao processo, correção gramatical, fórmula aplicável aos dados reais nem fluxograma fiel.

Um aviso de indício não prova que a IA inventou um fato. A ausência de avisos também não autoriza usar o relatório. Não há segunda chamada à API para julgar o texto.

A sintaxe Mermaid é conferida no próprio Python, sem Node.js e sem serviço externo. Essa conferência não substitui um compilador Mermaid.

Toda análise exige revisão humana antes de virar procedimento, controle ou decisão.
