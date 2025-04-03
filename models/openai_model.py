import openai
from utils.program_utils import execute_program

class OpenAIModel:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_response(self, prompt):
        try:
            prompt_lower = prompt.lower()
            if any(keyword in prompt_lower for keyword in ["abrir", "fechar", "volume", "capturar", "print", "screenshot", "desligar", "reiniciar", "esvaziar"]):
                return execute_program(prompt)
           
            messages = [{"role": "system", "content": "Você é Barsa, um assistente de IA semelhante ao JARVIS do Homem de Ferro que ajuda os usuários a encontrar informações e responder perguntas."}]
            for line in prompt.split("\n"):
                if line.strip():
                    messages.append({"role": "user" if "Barsa:" not in line else "assistant", "content": line.replace("Barsa: ", "")})
            messages.append({"role": "assistant", "content": ""})
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Erro ao gerar resposta: {str(e)}"