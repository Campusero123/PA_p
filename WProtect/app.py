import os
import base64
import requests
from datetime import datetime
from tkinter import Tk, filedialog

# Configuração do servidor da AI. Exemplo: "http://localhost:8000"
AI_SERVER_URL = "http://localhost:11434/api/generate"

# Função para selecionar uma imagem
def select_image():
    Tk().withdraw()  # Ocultar a janela principal do Tkinter
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    return file_path

# Função para transformar a imagem em uma string codificada em base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Função para enviar a imagem em base64 para o servidor do modelo llava
def send_image_to_llava(image_base64, prompt, model="llava"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "images": [image_base64]
    }
    response = requests.post(AI_SERVER_URL, json=payload)
    return response.json()

# Função para salvar o alerta
def save_alert(image_path, alert_message):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_dir = "./alerts"
    os.makedirs(save_dir, exist_ok=True)

    # Copiar a imagem
    image_name = os.path.basename(image_path)
    alert_image_path = os.path.join(save_dir, f"{timestamp}_{image_name}")
    with open(image_path, 'rb') as src, open(alert_image_path, 'wb') as dest:
        dest.write(src.read())

    # Salvar informações do alerta
    with open(os.path.join(save_dir, f"{timestamp}_alert.txt"), 'w') as alert_file:
        alert_file.write(f"Horário: {timestamp}\n")
        alert_file.write(f"Mensagem de Alerta: {alert_message}\n")
        alert_file.write(f"Caminho da Imagem: {alert_image_path}\n")
        # Simulação de localização
        alert_file.write(f"Localização: Latitude: -23.5505, Longitude: -46.6333\n")


# Fluxo principal
def main():
    if not AI_SERVER_URL:
        print("⚠️ Por favor, configure a URL do servidor da AI em 'AI_SERVER_URL'.")
        return

    print("Selecione uma imagem para análise...")
    image_path = select_image()

    if not image_path:
        print("Nenhuma imagem selecionada. Saindo...")
        return

    image_base64 = encode_image_to_base64(image_path)
    prompt = "Avalie se há uma mulher potencialmente em perigo nesta imagem. Responda com 'Risco Detectado' ou 'Risco Não Detectado'."

    print(f"Analisando a imagem: {image_path}")
    try:
        ai_response = send_image_to_llava(image_base64, prompt)
        response_text = ai_response.get("response", "")
    except requests.RequestException as e:
        print(f"Erro ao se comunicar com o servidor da AI: {e}")
        return

    if "Risco Detectado" in response_text:
        print("⚠️ Situação de risco detectada! Alertando autoridades...")
        save_alert(image_path, response_text)
    else:
        print("✅ Nenhuma situação de risco detectada.")

if __name__ == "__main__":
    main()
