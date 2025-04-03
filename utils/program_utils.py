import os
import subprocess
import pyautogui
import time
import shutil

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
            elif "documentos" in command:
                path = os.path.expanduser("~/Documents")
                subprocess.Popen(f'explorer "{path}"' if os.name == "nt" else f"nautilus '{path}'")
                return "Abrindo a pasta Documentos!"
            elif "downloads" in command:
                path = os.path.expanduser("~/Downloads")
                subprocess.Popen(f'explorer "{path}"' if os.name == "nt" else f"nautilus '{path}'")
                return "Abrindo a pasta Downloads!"
            elif "arquivo" in command:
                # Extrair nome do arquivo (simples, assume que vem depois de "abrir arquivo")
                parts = command.split("arquivo")
                if len(parts) > 1 and parts[1].strip():
                    file_name = parts[1].strip()
                    file_path = os.path.expanduser(f"~/Desktop/{file_name}")
                    if os.path.exists(file_path):
                        os.startfile(file_path) if os.name == "nt" else subprocess.Popen(["xdg-open", file_path])
                        return f"Abrindo o arquivo {file_name}!"
                    else:
                        return f"Arquivo {file_name} não encontrado na Área de Trabalho!"

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

        # Ações de sistema
        elif "capturar tela" in command or "print" in command or "screenshot" in command:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            screenshot_path = os.path.join(desktop, f"screenshot_{int(time.time())}.png")  # Nome único com timestamp
            os.makedirs(desktop, exist_ok=True)  # Garante que o diretório existe
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            return f"Captura de tela salva em {screenshot_path}!"
        elif "desligar" in command:
            if os.name == "nt":
                subprocess.Popen("shutdown /s /t 5")
                return "Desligando o computador em 5 segundos! (Cancele com 'shutdown /a' se precisar)"
            else:
                subprocess.Popen("shutdown -h now")
                return "Desligando o computador agora!"
        elif "reiniciar" in command:
            if os.name == "nt":
                subprocess.Popen("shutdown /r /t 5")
                return "Reiniciando o computador em 5 segundos! (Cancele com 'shutdown /a' se precisar)"
            else:
                subprocess.Popen("reboot")
                return "Reiniciando o computador agora!"
        elif "esvaziar lixeira" in command:
            if os.name == "nt":
                from winshell import recycle_bin
                recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                return "Lixeira esvaziada!"
            else:
                return "Esvaziar lixeira ainda não suportado no Linux."

        else:
            return "Comando não reconhecido. Tente 'abrir documentos', 'capturar tela' ou 'desligar'."
    except Exception as e:
        return f"Erro ao executar o comando: {str(e)}"