# Email-Classifier

# 📧 Classificador de Emails com IA (Desafio AutoU)

Essa aplicação web classifica emails em **Produtivo** ou **Improdutivo** e gera uma **resposta automática sugerida**, usando modelos de IA do Hugging Face.

## ✅ Funcionalidades

- Upload de arquivos `.txt` ou `.pdf`
- Colagem de texto direto no navegador
- Classificação usando zero-shot (BART)
- Geração de resposta automática com GPT-Neo

## 🚀 Como executar localmente

```bash
git clone https://github.com/seu-usuario/email-classifier-autou.git
cd email-classifier-autou

#Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

#Instale as dependências
pip install -r requirements.txt

#Rode o app
python app.py
