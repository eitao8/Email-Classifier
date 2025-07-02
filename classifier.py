from transformers import pipeline

classificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
gerador = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def processar_email(texto):
    resultado = classificador(
        texto,
        candidate_labels=["Solicitacao de tarefa", "Saudacao ou agradecimento"],
        hypothesis_template="Este email é: {}."
    )
    label = resultado["labels"][0]
    categoria = "Produtivo" if "tarefa" in label.lower() else "Improdutivo"

    if categoria == "Produtivo":
        prompt = (
        "Você é um assistente virtual de uma empresa. "
        "Escreva uma resposta educada, objetiva e útil para o seguinte email recebido:\n\n"
        f"{texto}\n\n"
        "Resposta:"
        )

    else:
        prompt = (
        "Você é um assistente virtual de uma empresa. "
        "Escreva uma resposta educada, objetiva e útil para o seguinte email recebido:\n\n"
        f"{texto}\n\n"
        "Resposta:"
        )

    resposta = gerador(prompt, max_length=100, do_sample=True)[0]['generated_text']
    return categoria, resposta.split("Resposta:")[-1].strip()
