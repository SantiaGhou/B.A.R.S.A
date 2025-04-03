import tkinter as tk
from models.openai_model import OpenAIModel
from utils.audio_utils import transcribe_audio

class BarsaGUI:
    def __init__(self, root, api_key):
        self.root = root
        self.model = OpenAIModel(api_key)
        self.root.title("Barsa")
        self.root.geometry("400x500")

        self.label = tk.Label(root, text="Bem-vindo à Barsa!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.text_input = tk.Entry(root, width=40)
        self.text_input.pack(pady=5)

        self.text_button = tk.Button(root, text="Enviar Texto", command=self.send_text)
        self.text_button.pack(pady=5)

        self.audio_button = tk.Button(root, text="Gravar Áudio", command=self.record_audio)
        self.audio_button.pack(pady=5)

        self.response_label = tk.Label(root, text="", wraplength=350, justify="left")
        self.response_label.pack(pady=10)

    def send_text(self):
        prompt = self.text_input.get()
        if prompt:
            response = self.model.generate_response(prompt)
            self.response_label.config(text=f"Barsa: {response}")
            self.text_input.delete(0, tk.END)

    def record_audio(self):
        self.response_label.config(text="Gravando... Fale algo!")
        self.root.update()
        try:
            text = transcribe_audio()
            response = self.model.generate_response(text)
            self.response_label.config(text=f"Você disse: {text}\nBarsa: {response}")
        except Exception as e:
            self.response_label.config(text=f"Erro: {str(e)}")

def main(api_key):
    root = tk.Tk()
    app = BarsaGUI(root, api_key)
    root.mainloop()

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    main(api_key)