import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate-video", methods=["POST"])
def generate_video():
    # Ici tu peux récupérer le prompt envoyé dans le JSON
    data = request.get_json()
    prompt = data.get("prompt", "Un coucher de soleil magnifique")

    # Pour l'exemple on renvoie un message simple
    return jsonify({"message": f"Reçu prompt : {prompt}"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # PORT fourni par Render
    app.run(host="0.0.0.0", port=port)
