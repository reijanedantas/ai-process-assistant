# Modelo de dados — AI Process Assistant

**Versão:** 1.0  
**Data:** 13/11/2026  
**Status:** Modelo lógico aprovado para orientar implementação; ainda não criado no banco

## 1. Objetivo

Manter histórico confiável dos processos, análises, riscos, melhorias, indicadores e decisões. O banco Neon foi criado, mas este modelo ainda não está implantado.

## 2. Entidades principais

| Tabela | Finalidade |
|---|---|
| processes | Cadastro persistente de cada processo |
| analyses | Versões das análises de um processo |
| stages | Etapas identificadas em uma versão de análise |
| risks | Riscos associados a uma versão de análise |
| improvements | Melhorias originadas em uma análise e acompanhadas ao longo do tempo |
| indicators | Definições dos indicadores |
| history_events | Eventos, decisões e mudanças de estado |
| indicator_measurements | Medições históricas de indicadores |

## 3. Relacionamentos

- Um processo pode possuir várias análises.
- Uma análise pertence a um processo e possui número de versão único dentro dele.
- Uma análise pode possuir várias etapas e vários riscos.
- Uma melhoria pertence ao processo e referencia a análise que a originou.
- Uma melhoria continua vinculada ao processo mesmo quando novas análises forem criadas.
- Um indicador pode possuir várias medições ao longo do tempo.
- Eventos registram ações e mudanças relacionadas ao processo ou aos seus objetos.

## 4. Status de melhoria

- Sugerida
- Em avaliação
- Aprovada
- Em implementação
- Implementada
- Rejeitada

A IA pode sugerir uma melhoria, mas não pode aprová-la nem alterar seu status sem ação humana autorizada.

## 5. Regras de integridade

- Identificadores UUID.
- Chaves estrangeiras e índices para consultas frequentes.
- Restrição única para (process_id, version) em analyses.
- Datas armazenadas em UTC.
- Medições históricas não devem sobrescrever medições anteriores.
- Não utilizar exclusão em cascata que apague inadvertidamente o histórico.
- Registrar origem e validação das informações.

## 6. Proveniência e validação

Os registros devem distinguir, conforme aplicável:

- Informação fornecida diretamente pela pessoa usuária.
- Informação extraída de documento.
- Hipótese gerada pela IA.
- Recomendação da IA.
- Informação validada por pessoa responsável.
- Informação ainda não confirmada.

A implementação deverá definir campos ou uma estrutura de evidências para guardar origem, referência, responsável pela validação, data e estado de validação.

## 7. Indicadores

A tabela indicators guarda definição, fórmula, unidade, periodicidade e critérios. A tabela indicator_measurements guarda cada valor medido, sua data de referência, origem e observações. Não substituir a série histórica pelo último valor.

## 8. Integração com Power BI

A camada de consulta deverá disponibilizar views ou exportações com estruturas compatíveis com:

- tb_Processos
- tb_Etapas
- tb_Riscos
- tb_Melhorias
- tb_Indicadores
- tb_Historico

O mapeamento definitivo será validado quando o esquema físico for implementado.
