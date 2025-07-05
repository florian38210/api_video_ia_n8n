import os
import uuid
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
OUTPUT_FOLDER = "output"
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def generate_dummy_video(output_path):
    # Simule la génération vidéo, crée un fichier vide ou avec un contenu simple
    with open(output_path, "wb") as f:
        f.write(b"\x00" * 1024 * 1024)  # 1 Mo de zeros juste pour test

@app.route("/generate-video", methods=["POST"])
def generate_video():
    data = request.json
    prompt = data.get("prompt", "Pas de prompt fourni")

    # Ici tu mettra ta vraie génération vidéo IA
    video_id = str(uuid.uuid4())
    video_filename = f"{video_id}.mp4"
    video_path = os.path.join(OUTPUT_FOLDER, video_filename)

    generate_dummy_video(video_path)

    return jsonify({
        "video_url": f"/videos/{video_filename}",
        "prompt": prompt
    })

@app.route("/videos/<filename>")
def serve_video(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

