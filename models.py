from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

try:
    models = client.models.list()

    print("Models available with your Groq API key:\n")

    for model in sorted(models.data, key=lambda m: m.id):
        print(model.id)

except Exception as e:
    print(f"Error: {e}")
