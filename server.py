from flask import Flask, request, jsonify
import subprocess, os
from flask_cors import CORS  # Importez CORS
import tempfile
import json

app = Flask(__name__)
CORS(app)

CACHE_DIR = 'cache_touist'

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def run_touist_command(args, stdin_data):
    try:
        with tempfile.NamedTemporaryFile(delete=False, mode='w', dir=CACHE_DIR) as temp_file:
            temp_file.write(stdin_data)
            temp_file_path = temp_file.name
        # Créer une commande avec les arguments
        command = f"touist {args} {temp_file_path}"
        process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Passer les données d'entrée (stdin) à la commande
        stdout, stderr = process.communicate(input=stdin_data.encode())  # Utilisation de .encode() pour convertir en bytes

        # Vérifier s'il y a une erreur
        if stderr:
            return f"Error: {stderr.decode()}"

        return stdout.decode()

    except Exception as e:
        return f"Error executing command: {str(e)}"



@app.route('/touist_cmd', methods=['POST'])
def touist_cmd():
    try:
        args = request.form.get('args', '')
        stdin_data = request.form.get('stdin', '')
        print("args", args)
        print("stdin", stdin_data)
        result = run_touist_command(args, stdin_data)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7015)
