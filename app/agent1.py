import openai

# Configurazione di OpenAI
#openai.api_key = "your-openai-api-key"
client = openai.OpenAI(api_key="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")

def agent1_task(data):
    # Usa OpenAI per generare una risposta
    response = openai.Completion.create(
        model="text-davinci-003",  # Usa il modello appropriato
        prompt=data,  # Invia i dati (prompt) per la risposta
        max_tokens=150
    )
    result = response.choices[0].text.strip()
    return result
