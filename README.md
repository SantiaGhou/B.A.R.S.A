# Barsa - Assistente Inteligente Baseada em IA

Barsa é uma assistente inteligente desenvolvida em Python que utiliza os modelos da OpenAI para fornecer uma experiência interativa e multifuncional. O nome **Barsa** foi criado com base nas seguintes siglas:

- **B**: Brain (Cérebro) – Representa a inteligência artificial por trás do sistema.
- **A**: Assistant (Assistente) – Refere-se ao papel principal da aplicação, que é auxiliar o usuário.
- **R**: Recognizer (Reconhecedor) – Simboliza a capacidade de reconhecimento de texto, áudio, imagens e até rostos.
- **S**: Smart (Inteligente) – Indica a habilidade de processar informações complexas e tomar decisões baseadas em IA.
- **A**: Actionable (Executável) – Reflete a capacidade de realizar ações no computador, como abrir programas ou jogar jogos.

---

## Funcionalidades Principais

1. **Transcrição de Áudio para Texto**  
   A Barsa pode transcrever áudios capturados pelo microfone em tempo real e transformá-los em texto compreensível.

2. **Resposta a Mensagens de Texto**  
   Utilizando os modelos da OpenAI, a Barsa é capaz de entender e responder a perguntas ou comandos digitados pelo usuário.

3. **Reconhecimento de Imagens**  
   A assistente pode analisar e interpretar conteúdo visual, fornecendo descrições ou insights sobre as imagens fornecidas.

4. **Interação com Programas do Computador**  
   A Barsa pode ser configurada para abrir, fechar ou interagir com programas instalados no computador do usuário.

5. **Interface Gráfica Amigável**  
   Uma interface bonita e intuitiva será disponibilizada para facilitar a interação com o usuário.

6. **Opcional: Reconhecimento Facial**  
   Com acesso à webcam, a Barsa pode reconhecer rostos conhecidos e executar ações específicas com base nessa identificação.

7. **Jogos Interativos**  
   A Barsa inclui suporte para jogos simples, como xadrez e damas, permitindo que o usuário desafie a IA.

---
## Estrutura do Projeto

Aqui está a estrutura sugerida para o projeto Barsa:
profile
Qwen2.5-Plus
12:57 pm
Aqui está a estrutura do projeto formatada em Markdown, mantendo a clareza e organização visual:

markdown
Copiar
1
2
3
4
⌄
## Estrutura do Projeto

Aqui está a estrutura sugerida para o projeto Barsa:

B.A.R.S.A/<br>
│<br>
├── README.md # Documentação do projeto<br>
├── .env # Arquivo de variáveis de ambiente (chave da API da OpenAI)<br>
├── main.py # Ponto de entrada do programa<br>
├── utils/ # Diretório para funções utilitárias<br>
│ ├── audio_utils.py # Funções relacionadas à transcrição de áudio<br>
│ ├── image_utils.py # Funções relacionadas ao reconhecimento de imagens<br>
│ ├── program_utils.py # Funções para interação com programas do computador<br>
│ └── game_utils.py # Funções para jogos interativos<br>
│
├── interfaces/ # Diretório para interfaces gráficas<br>
│ └── gui.py # Interface gráfica principal<br>
│
├── models/ # Diretório para integração com modelos da OpenAI<br>
│ └── openai_model.py # Classe para comunicação com a API da OpenAI<br>
│<br>
└── tests/ # Diretório para testes automatizados<br>
├── test_audio.py # Testes para transcrição de áudio<br>
├── test_image.py # Testes para reconhecimento de imagens<br>
└── test_programs.py # Testes para interação com programas<br>

## Pré-Requisitos

Para rodar o projeto Barsa, você precisará instalar as seguintes dependências:

1. Python 3.8+
2. Bibliotecas Python:
   - `openai` (para integração com os modelos da OpenAI)
   - `speech_recognition` (para transcrição de áudio)
   - `pyttsx3` (para síntese de fala)
   - `Pillow` (para manipulação de imagens)
   - `pyautogui` (para interação com programas do computador)
   - `tkinter` (ou outra biblioteca de GUI, como PyQt ou Kivy)

Instale as dependências com o comando abaixo:

```bash
pip install -r requirements.txt
```
---
## Configuração inicial
```bash
git clone https://github.com/SantiaGhou/B.A.R.S.A.git
cd B.A.R.S.A
```
2. Crie um arquivo .env na raiz do projeto e adicione sua chave de API da OpenAI
3. ```pip install -r requirements.txt```

4.  Rode o comando ```python main.py```


## 📋 To-Do List

### ⚙️ Configuração Inicial
- [x] Definir arquitetura e estrutura do projeto
- [x] Criar README com informações detalhadas
- [x] Configurar variáveis de ambiente (.env) para armazenar a chave da API da OpenAI

---

### 🎤 Transcrição de Áudio para Texto
- [x] Implementar transcrição de áudio capturado pelo microfone
  - [x] Criar módulo `utils/audio_utils.py`
  - [x] Utilizar biblioteca `speech_recognition` para capturar e processar áudio
  - [ ] Testar funcionalidade em diferentes ambientes (ruído, volume baixo, etc.)
  - [x] Integrar transcrição com respostas da IA

---

### 💬 Resposta a Mensagens de Texto
- [x] Integrar modelo de linguagem da OpenAI para responder mensagens de texto
  - [x] Criar classe `OpenAIModel` em `models/openai_model.py`
  - [x] Garantir autenticação segura com a API da OpenAI
  - [ ] Testar integração com exemplos de perguntas/respostas
  - [ ] Otimizar latência das respostas

---

### 🖼️ Reconhecimento de Imagens
- [ ] Adicionar suporte para análise e interpretação de imagens
  - [ ] Criar módulo `utils/image_utils.py`
  - [ ] Utilizar bibliotecas como `Pillow` ou `OpenCV` para processamento básico
  - [ ] Integrar descrição de imagens com o modelo da OpenAI (DALL-E ou similares)
  - [ ] Testar reconhecimento de objetos e cenas comuns

---

### 💻 Interação com Programas do Computador
- [x] Desenvolver funcionalidade para abrir, fechar e interagir com programas locais
  - [x] Criar módulo `utils/program_utils.py`
  - [x] Utilizar biblioteca `pyautogui` ou similar para controle de janelas
  - [x] Implementar comandos de voz ou texto para gerenciar programas
  - [ ] Testar compatibilidade com diferentes sistemas operacionais

---

### 🎨 Interface Gráfica Amigável
- [ ] Criar interface gráfica bonita e intuitiva
  - [ ] Desenvolver GUI em `interfaces/gui.py`
  - [ ] Utilizar biblioteca `tkinter`, `PyQt` ou `Kivy` para design
  - [ ] Integrar todas as funcionalidades principais na interface
  - [ ] Testar usabilidade em diferentes dispositivos

---

### 🎮 Jogos Interativos (Opcional)
- [ ] Implementar jogos simples como xadrez, damas e outros
  - [ ] Criar módulo `utils/game_utils.py`
  - [ ] Desenvolver lógica básica dos jogos
  - [ ] Permitir que o usuário desafie a IA
  - [ ] Testar gameplay e ajustar dificuldade

---

### 👤 Reconhecimento Facial (Opcional)
- [ ] Adicionar suporte para reconhecimento facial via webcam
  - [ ] Integrar biblioteca de visão computacional como `dlib` ou `face_recognition`
  - [ ] Treinar modelos para reconhecer rostos conhecidos
  - [ ] Testar detecção em tempo real
  - [ ] Implementar ações específicas baseadas no reconhecimento facial

---

### 🛠️ Manutenção e Melhorias Contínuas
- [ ] Documentar cada módulo com comentários claros e exemplos de uso
- [ ] Escrever testes automatizados para garantir qualidade do código
- [ ] Otimizar desempenho geral da aplicação
- [ ] Coletar feedbacks dos usuários para implementar novas funcionalidades
