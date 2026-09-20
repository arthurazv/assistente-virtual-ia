# Guia Dev Júnior: Assistente Virtual IA 🚀

**Projeto Final do Lab: Construa Seu Assistente Virtual Com Inteligência Artificial da DIO.**

## O Problema
Muitas pessoas que estão iniciando na programação se sentem perdidas com o excesso de informações, configurações de ambiente de desenvolvimento e comandos de terminal. Termos como "Git", "Commit", "Variáveis de Ambiente" costumam causar confusão inicial.

## A Solução
O **Guia Dev Júnior** é um assistente virtual com inteligência artificial focado em ajudar pessoas desenvolvedoras iniciantes. Ele fornece respostas claras, simples e diretas sobre comandos de versionamento, configuração de ferramentas (como VS Code, Node e Python) e boas práticas.

## Valor do Projeto (Pitch)
Este projeto mostra como uma IA, guiada por uma base de conhecimento bem definida e instruções de sistema (prompts) claras, pode atuar como um mentor paciente, reduzindo a barreira de entrada na tecnologia para novos profissionais, otimizando o tempo de aprendizado.

## Estrutura do Repositório
- `docs/`: Contém a documentação de persona do agente e as métricas de avaliação.
- `data/`: Contém a base de conhecimento (arquivos de texto com dados para a IA).
- `src/`: Contém o código-fonte da aplicação (Python).

## Como rodar localmente
1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv venv` e ative-o.
3. Instale as dependências: `pip install -r requirements.txt`
4. Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API: `GEMINI_API_KEY=sua_chave_aqui`
5. Execute a aplicação: `python src/app.py`
