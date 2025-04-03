import os
import subprocess
import pyautogui

def execute_program(command):
    try:
        command = command.lower()
        
        # Abrir programas
        if "abrir" in command:
            if "bloco de notas" in command:
                subprocess.Popen("notepad.exe" if os.name == "nt" else "gedit")
                return "Abrindo o Bloco de Notas!"
            elif "navegador" in command or "chrome" in command:
                subprocess.Popen("chrome.exe" if os.name == "nt" else "google-chrome")
                return "Abrindo o Chrome!"
            elif "firefox" in command:
                subprocess.Popen("firefox.exe" if os.name == "nt" else "firefox")
                return "Abrindo o Firefox!"
            elif "opera" in command:
                subprocess.Popen("opera.exe" if os.name == "nt" else "opera")
                return "Abrindo o Opera!"
            elif "calculadora" in command:
                subprocess.Popen("calc.exe" if os.name == "nt" else "gnome-calculator")
                return "Abrindo a Calculadora!"
            elif "vscode" in command or "visual studio code" in command:
                subprocess.Popen("code" if os.name == "nt" else "code")
                return "Abrindo o Visual Studio Code!"
            elif "spotify" in command:
                subprocess.Popen("spotify.exe" if os.name == "nt" else "spotify")
                return "Abrindo o Spotify!"
            elif "explorador" in command or "arquivos" in command:
                subprocess.Popen("explorer.exe" if os.name == "nt" else "nautilus")
                return "Abrindo o Explorador de Arquivos!"
            else:
                return "Não sei abrir esse programa ainda. Tente algo como 'abrir chrome' ou 'abrir opera'."

        # Fechar programas
        elif "fechar" in command:
            if "bloco de notas" in command:
                pyautogui.hotkey("alt", "f4")
                return "Fechando o Bloco de Notas!"
            elif "navegador" in command or "chrome" in command:
                pyautogui.hotkey("ctrl", "shift", "w")
                return "Fechando o Chrome!"
            elif "firefox" in command:
                pyautogui.hotkey("ctrl", "shift", "w")
                return "Fechando o Firefox!"
            elif "opera" in command:
                pyautogui.hotkey("ctrl", "shift", "w")
                return "Fechando o Opera!"
            elif "calculadora" in command:
                pyautogui.hotkey("alt", "f4")
                return "Fechando a Calculadora!"
            elif "vscode" in command or "visual studio code" in command:
                pyautogui.hotkey("ctrl", "q")
                return "Fechando o Visual Studio Code!"
            elif "spotify" in command:
                pyautogui.hotkey("alt", "f4")
                return "Fechando o Spotify!"
            else:
                return "Qual programa você quer fechar? Tente 'fechar chrome' ou 'fechar opera'."

        # Controle de volume
        elif "volume" in command:
            if "aumentar" in command:
                pyautogui.hotkey("volumeup")
                return "Aumentando o volume!"
            elif "diminuir" in command:
                pyautogui.hotkey("volumedown")
                return "Diminuindo o volume!"
            elif "mutar" in command or "mudo" in command:
                pyautogui.hotkey("volumemute")
                return "Volume mutado!"
            else:
                return "O que você quer fazer com o volume? Tente 'aumentar volume' ou 'mutar volume'."

        else:
            return "Comando não reconhecido. Tente 'abrir chrome', 'fechar opera' ou 'aumentar volume'."
    except Exception as e:
        return f"Erro ao executar o comando: {str(e)}"