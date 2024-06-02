from gtts import gTTS
from playsound import playsound

def ler_texto_em_audio(arquivo_txt, lingua='pt'):
    try:
        # Lê o conteúdo do arquivo de texto
        with open(arquivo_txt, 'r', encoding='utf-8') as file:
            texto = file.read()
        
        # Converte o texto para áudio
        tts = gTTS(text=texto, lang=lingua)
        arquivo_audio = 'audio_output.mp3'
        tts.save(arquivo_audio)
        
        # Reproduz o áudio gerado
        playsound(arquivo_audio)
        print("Áudio reproduzido com sucesso!")
    
    except Exception as e:
        print(f"Erro ao ler o arquivo ou converter para áudio: {e}")

# Solicita o nome do arquivo de texto ao usuário
nome_arquivo = input("Digite o nome do arquivo de texto (com extensão .txt): ")

# Chama a função para ler o arquivo e converter para áudio
ler_texto_em_audio(nome_arquivo)
