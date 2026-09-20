# Avaliação e Métricas

Para garantir que o assistente **Guia Dev Júnior** está funcionando corretamente e seguindo a persona, realizamos os seguintes testes de validação:

## Cenário 1: Pergunta sobre escopo esperado (Git)
- **Usuário:** "Como eu salvo meu código no github?"
- **Resposta Esperada:** O agente deve explicar o fluxo básico de `git add`, `git commit` e `git push` de forma simples, citando a base de conhecimento.
- **Status:** Aprovado ✅.

## Cenário 2: Pergunta fora do escopo (Avançado)
- **Usuário:** "Como eu configuro um cluster Kubernetes na AWS?"
- **Resposta Esperada:** O agente deve informar que esse assunto é avançado e está fora do seu escopo, pois ele é focado em ajudar iniciantes.
- **Status:** Aprovado ✅.

## Cenário 3: Pergunta abstrata/emocional
- **Usuário:** "Estou com medo de não conseguir aprender a programar."
- **Resposta Esperada:** O agente deve usar seu tom encorajador e amigável para motivar o usuário, lembrando que o aprendizado é um processo contínuo.
- **Status:** Aprovado ✅.
