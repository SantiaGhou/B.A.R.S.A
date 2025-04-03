import os
from dotenv import load_dotenv
from utils.audio_utils import transcribe_audio
from models.openai_model import OpenAIModel

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("A variável OPENAI_API_KEY não foi encontrada no .env")

openai_model = OpenAIModel(api_key=openai_api_key)

def main():
    print("Bem-vindo à Barsa!")
    print("Para sair, digite 'sair' ou pressione Ctrl+C.")
    
    while True:
        print("\nModos disponíveis:")
        print("1. Transcrever áudio do microfone")
        print("2. Fazer uma pergunta em texto")
        print("3. Sair")
        
        choice = input("Escolha um modo (1/2/3): ").strip()
        
        if choice == "1":
            print("Iniciando transcrição de áudio...")
            try:
                text = transcribe_audio()
                print(f"Você disse: {text}")
                response = openai_model.generate_response(text)
                print(f"Barsa: {response}")
            except Exception as e:
                print(f"Erro durante a transcrição: {e}")
        
        elif choice == "2":
            user_input = input("Faça sua pergunta: ").strip()
            if user_input.lower() in ["sair", "exit"]:
                break
            response = openai_model.generate_response(user_input)
            print(f"Barsa: {response}")
        
        elif choice == "3":
            print("Encerrando Barsa. Até mais!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()