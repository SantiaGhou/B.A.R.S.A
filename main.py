import os
from dotenv import load_dotenv
from utils.audio_utils import transcribe_audio
from models.openai_model import OpenAIModel
from interfaces.gui import main as gui_main

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
        print("3. Abrir interface gráfica")
        print("4. Sair")
        
        choice = input("Escolha um modo (1/2/3/4): ").strip()
        
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
            print("\nModo texto ativado! Converse comigo aqui.")
            print("Digite 'voltar' pra retornar ao menu ou 'sair' pra encerrar.")
            conversation_history = []
            while True:
                user_input = input("Você: ").strip()
                if user_input.lower() == "sair":
                    print("Encerrando Barsa. Até mais!")
                    return
                elif user_input.lower() == "voltar":
                    print("Voltando ao menu principal...")
                    break
                if user_input:
                    conversation_history.append({"role": "user", "content": user_input})
                    
                    response = openai_model.generate_response("\n".join([msg["content"] for msg in conversation_history]))
                    print(f"Barsa: {response}")
                    conversation_history.append({"role": "assistant", "content": response})
        
        elif choice == "3":
            print("Abrindo interface gráfica...")
            gui_main(openai_api_key)
        
        elif choice == "4":
            print("Encerrando Barsa. Até mais!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()