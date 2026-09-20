import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import get_system_prompt

# Carrega variáveis de ambiente do arquivo .env (como a GEMINI_API_KEY)
load_dotenv()

# Inicializa o cliente do Gemini
# Ele automaticamente pega a variável de ambiente GEMINI_API_KEY
client = genai.Client()

def carregar_base_conhecimento(caminho_arquivo: str) -> str:
    """Lê o arquivo de texto com a base de conhecimento."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
        return ""

def main():
    print("=" * 50)
    print("🤖 Bem-vindo ao Guia Dev Júnior!")
    print("Eu posso te ajudar com Git, Github e configuração de ambiente.")
    print("Digite 'sair' para encerrar a conversa.")
    print("=" * 50)

    # Carrega o conhecimento e o prompt
    caminho_base = os.path.join(os.path.dirname(__file__), "..", "data", "base_conhecimento.txt")
    base_conhecimento = carregar_base_conhecimento(caminho_base)
    system_instruction = get_system_prompt(base_conhecimento)

    # Configuração do Chat
    # Usando o modelo gemini-2.5-flash que é rápido e eficiente
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.3, # Temperatura baixa para focar na base de conhecimento e evitar alucinações
    )

    # Inicia o chat (mantém o histórico da conversa)
    chat = client.chats.create(model="gemini-2.5-flash", config=config)

    # Loop de interação com o usuário
    while True:
        try:
            mensagem = input("\nVocê: ")
            if mensagem.lower() in ['sair', 'exit', 'quit']:
                print("Guia Dev Júnior: Boa sorte nos seus estudos! Até a próxima! 🚀")
                break
            
            if not mensagem.strip():
                continue

            print("Guia Dev Júnior: Pensando...")
            
            # Envia a mensagem para o modelo e aguarda a resposta
            response = chat.send_message(mensagem)
            
            print(f"\nGuia Dev Júnior: {response.text}")

        except Exception as e:
            print(f"\nOcorreu um erro ao comunicar com a IA: {e}")

if __name__ == "__main__":
    main()
