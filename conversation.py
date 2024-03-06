import openai

# Configure a sua chave da API GPT-3 aqui
openai = openai.OpenAI()

def chat(user_input):
    def obter_resposta(conversa):
        resposta = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use a engine adequada para GPT-3.5
            messages=conversa
        )
        return resposta.choices[0].message.content.strip()

    # Inicializar a conversa com uma mensagem de saudação
    conversa = [
        {"role": "system", "content": "Bien sûr ! Vous parlez à une personne en français, veuillez prendre en compte que votre interlocuteur est au début de son apprentissage. Répondez de manière claire et concise, et gardez la conversation intéressante. PARLEZ UNIQUEMENT EN FRANÇAIS."}
        ]

    # Obter input do usuário e adicionar à conversa

    conversa.append({"role": "user", "content": user_input})

    # Obter resposta do ChatGPT
    resposta_chatgpt = obter_resposta(conversa)

    # Adicionar a resposta do ChatGPT à conversa
    conversa.append({"role": "assistant", "content": resposta_chatgpt})

    # Imprimir a resposta
    print("ChatGPT:", resposta_chatgpt)
    return conversa[-1]['content']

