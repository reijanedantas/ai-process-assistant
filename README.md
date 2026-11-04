# AI Process Assistant

Protótipo de assistente de IA para análise, diagnóstico e melhoria de processos.

## Funcionalidades atuais

- Entrada de descrição do processo por texto.
- Envio de arquivos PDF, DOCX e TXT.
- Análise com a API Gemini.
- Seleção do objetivo e do nível de detalhamento.
- Geração de relatório em Markdown.
- Checagens locais do relatório. Elas não garantem correção técnica.
- Limites de 20.000 caracteres no processo, 5.000 no contexto e 5 MB por arquivo.

## Requisitos

- Python 3.11 ou superior.
- Uma chave de API Gemini.
- Conexão com a internet para acessar a API.

## Instalação no Windows

1. Abra o Cursor e abra a pasta deste projeto.
2. Abra o terminal integrado do Cursor.
3. Crie um ambiente virtual:

   ```powershell
   python -m venv .venv
   ```

4. Ative o ambiente virtual:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   Se o PowerShell bloquear a ativação, use o Prompt de Comando:

   ```cmd
   .venv\Scripts\activate.bat
   ```

5. Instale as dependências:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Crie o arquivo de configuração local copiando `.streamlit/secrets.toml.example` para `.streamlit/secrets.toml`.
7. Abra `.streamlit/secrets.toml` e substitua o texto de exemplo pela sua chave Gemini. Esse arquivo fica fora do Git.
   Se preferir não criar o arquivo, defina a chave só na sessão do terminal, com um valor real no lugar do exemplo:

   ```powershell
   $env:GEMINI_API_KEY = "SUA_CHAVE_AQUI"
   ```

8. Execute:

   ```powershell
   streamlit run app.py
   ```

## Segurança: antes de publicar

- **Nunca publique** `.streamlit/secrets.toml`, chaves de API, senhas ou tokens.
- O arquivo `.gitignore` já exclui `.streamlit/secrets.toml` e arquivos `.env`.
- Não coloque chaves diretamente no código `app.py`.
- Não use `git add -f` no arquivo de segredos.
- Antes do primeiro commit, rode `git status` e confira que `.streamlit/secrets.toml` **não** aparece.
- Não use dados pessoais, funcionais, sigilosos ou de clientes nos testes.
- O texto enviado para análise é transmitido à API Gemini. Considere isso antes de inserir qualquer informação.
- O repositório não inclui licença. Escolha uma antes de tornar o projeto público, se quiser permitir reutilização.

## Publicação no GitHub

1. Crie um repositório novo no GitHub.
2. No Cursor, abra o terminal na pasta do projeto.
3. Confira os arquivos que serão enviados:

   ```powershell
   git status
   ```

4. Inicialize o Git, se ainda não existir:

   ```powershell
   git init
   ```

5. Adicione os arquivos:

   ```powershell
   git add .
   ```

6. Confira novamente o que será enviado:

   ```powershell
   git status
   ```

7. Crie o primeiro commit:

   ```powershell
   git commit -m "Versão inicial do AI Process Assistant"
   ```

8. Conecte o repositório remoto usando a URL do repositório criado no GitHub:

   ```powershell
   git remote add origin URL_DO_SEU_REPOSITORIO
   ```

9. Envie os arquivos:

   ```powershell
   git branch -M main
   git push -u origin main
   ```

Substitua `URL_DO_SEU_REPOSITORIO` pela URL real do seu repositório. Não execute esse comando com o texto de exemplo.

## Publicação no Streamlit Community Cloud

Depois de publicar o código no GitHub:

1. Acesse o Streamlit Community Cloud.
2. Conecte sua conta do GitHub.
3. Selecione o repositório e o arquivo `app.py`.
4. Nas configurações de Secrets do aplicativo, cadastre:

   ```toml
   GEMINI_API_KEY = "SUA_CHAVE_GEMINI"
   ```

5. Publique o aplicativo.

A chave deve ser cadastrada nas configurações de Secrets da plataforma, nunca em um arquivo versionado no GitHub.

## Verificação local

Na pasta do projeto, com o ambiente virtual ativo:

```powershell
python -m unittest -v
```

Os testes não chamam a API Gemini e não precisam de chave. Eles conferem a leitura dos arquivos e as checagens do relatório com textos fictícios.

## Limitações conhecidas

A checagem local procura seções, tópicos da minuta, termos das duas fórmulas, um bloco Mermaid e alguns indícios de extrapolação. Ela **não comprova** fidelidade ao processo, correção gramatical, fórmula aplicável aos dados reais nem fluxograma fiel.

Um aviso de indício não prova que a IA inventou um fato. A ausência de avisos também não autoriza usar o relatório. Não há segunda chamada à API para julgar o texto: isso aumentaria custo e latência e continuaria sendo uma estimativa.

A sintaxe Mermaid é conferida no próprio Python, sem Node.js e sem serviço externo. Essa conferência não substitui um compilador Mermaid.

Toda análise exige revisão humana.
