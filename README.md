# 🕵️‍♂️ Super Agente "Olhos da Lei": Visão e Decisão Autônoma com Google ADK 🤖

Este repositório contém o código do projeto desenvolvido durante a Imersão IA com Google Gemini e Google ADK da Alura. O projeto implementa um protótipo de Agente de Inteligência Artificial focado em monitoramento de segurança e resposta a situações suspeitas.

## ✨ Sobre o Projeto

O "Super Agente Olhos da Lei" aborda o desafio da segurança urbana frente ao grande volume de dados gerados por sistemas de vigilância. A necessidade de identificar e reagir rapidamente a atividades suspeitas de forma autônoma é crucial.

Nosso projeto demonstra a construção de um Agente de IA modular, composto por múltiplos Agentes especializados que colaboram em um fluxo de processamento e decisão. Utilizando o Google Agent Development Kit (ADK) e modelos Gemini, criamos uma inteligência capaz de "observar" (via input simulado), avaliar riscos, sugerir investigações e recomendar ações.

## 🧠 Arquitetura do Super Agente

O Super Agente é estruturado em torno de Agentes colaborativos, cada um com uma função específica:

-   **Agente Visão:** Processa a descrição da cena e identifica elementos relevantes.
-   **Agente Risco:** Avalia o nível de perigo da situação (Baixo, Médio, Alto) com base na análise visual.
-   **Agente Investigação:** Analisa o relatório de visão e risco e sugere quais informações buscar para identificar suspeitos.
-   **Agente Ação:** Recomenda a ação mais adequada com base na situação, risco e informações adicionais (como resultado de busca simulada em banco de dados).

O fluxo de informação básico segue a cadeia: **Visão → Risco → Ação**. O Agente Investigação atua de forma complementar, fornecendo dados que podem influenciar a decisão do Agente Ação.

## 🚀 Funcionalidades Implementadas

-   Configuração e uso da API do Google Gemini.
-   Instalação e utilização do Google Agent Development Kit (ADK).
-   Definição de múltiplos Agentes de IA com instruções específicas.
-   Implementação de uma função auxiliar (`call_agent`) para rodar os Agentes.
-   Demonstração do fluxo **Visão → Risco → Ação** com inputs textuais simulados.
-   Definição de um Agente Investigação para sugerir buscas.
-   Simulação de uma ferramenta de busca em banco de dados de procurados (`mock_database_lookup`) e sua utilização direta no fluxo.
-   Demonstração do Agente Ação tomando decisões influenciadas pelo resultado da busca simulada.

*(Nota: Devido a uma limitação na versão atual do ADK utilizada, a integração da ferramenta de busca com o Agente Investigação foi simulada chamando a função diretamente após a sugestão do agente, em vez de usar a funcionalidade `Tool` nativa do ADK.)*

## 💻 Como Rodar o Projeto

O projeto está implementado em um notebook Google Colab (`Projeto__Olhos_da_Lei__de_Imersão_IA_Alura_+_Google_Gemini_Aula_05_Agentes.ipynb`).

1.  **Abra o notebook no Google Colab:** Clique no arquivo `.ipynb` neste repositório do GitHub. O GitHub tem um botão "Open in Colab" que facilita isso.
2.  **Configure sua API Key do Google Gemini:** Siga as instruções no notebook para configurar a sua `GOOGLE_API_KEY` nos Segredos do Colab.
3.  **Execute as Células em Ordem:** Rode cada célula do notebook sequencialmente, da primeira até a última. Isso instalará as bibliotecas, configurará o ambiente, definirá os Agentes e executará o fluxo de demonstração.

Certifique-se de ter uma conexão ativa e que sua API Key está configurada corretamente nos Segredos do Colab.

## 🌐 Link para o Vídeo de Demonstração

[**Assista à apresentação e demonstração do Super Agente "Olhos da Lei" aqui!**](LINK_DO_SEU_VIDEO_AQUI)

*(Lembre-se de substituir `LINK_DO_SEU_VIDEO_AQUI` pelo link real do seu vídeo no YouTube ou outra plataforma)*

## ⏭️ Próximos Passos (Potencial Futuro)

-   Integrar com um sistema real de **Visão Computacional** para processar imagens/vídeos de câmeras.
-   Conectar a um **Banco de Dados** real de informações de segurança ou criminais.
-   Implementar ações reais, como **alertas automáticos** para autoridades ou sistemas de resposta.
-   Adicionar Agentes para reconhecimento facial, análise de comportamento, etc.
-   Desenvolver uma interface de usuário para monitoramento.

## 👨‍💻 Autor

-   [Yaakov Israel][(https://github.com/Yaakov-Israel)

---
