import openai
from utils.program_utils import execute_program

class OpenAIModel:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_response(self, prompt):
        try:
            prompt_lower = prompt.lower()
            if "abrir" in prompt_lower or "fechar" in prompt_lower or "volume" in prompt_lower:
                return execute_program(prompt)
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é Barsa, um assistente de IA semelhante ao JARVIS do Homem de Ferro que ajuda os usuários a encontrar informações e responder perguntas."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": ""}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Erro ao gerar resposta: {str(e)}"