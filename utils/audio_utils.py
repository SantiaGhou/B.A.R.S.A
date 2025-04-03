import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        print("Ajustando para ruído ambiente... Aguarde.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Fale algo!")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        return text
    except sr.UnknownValueError:
        return "Não consegui entender o que você disse."
    except sr.RequestError as e:
        return f"Erro ao conectar ao serviço de reconhecimento: {str(e)}"