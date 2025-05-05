from flask import Flask, request, jsonify
import subprocess, os
from flask_cors import CORS  # Importez CORS
import tempfile
import json

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # e.g., 16 MB limit

CACHE_DIR = 'cache_touist'

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def run_touist_command(args, stdin_data):
    try:
        # Charger l'environnement OPAM
        opam_env = subprocess.check_output(['opam', 'env', '--shell', 'bash'], universal_newlines=True)
        env = os.environ.copy()
        for line in opam_env.splitlines():
            if line.startswith('export'):
                var, value = line.split()[1].split('=')
                env[var] = value.strip('"')

        with tempfile.NamedTemporaryFile(delete=False, mode='w', dir=CACHE_DIR) as temp_file:
            temp_file.write(stdin_data)
            temp_file_path = temp_file.name

        command = f"touist {args} {temp_file_path}"
        print(f"Running command: {command}")

        process = subprocess.Popen(
            command,
            shell=True,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        stdout_decoded = stdout.decode()
        stderr_decoded = stderr.decode()

        if stderr_decoded.strip():
            print(f"[WARNING] touist stderr output:\n{stderr_decoded}")

        return stdout_decoded

    except FileNotFoundError:
        error_message = "Command 'touist' not found. Is it installed and available in PATH?"
        print(f"[ERROR] {error_message}")
        raise RuntimeError(error_message)
    except subprocess.CalledProcessError as e:
        error_message = f"Subprocess error: {str(e)}"
        print(f"[ERROR] {error_message}")
        raise RuntimeError(error_message)
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(f"[ERROR] {error_message}")
        raise RuntimeError(error_message)


@app.route('/')
def hello():
    return "Bonjour ! Bienvenue sur le serveur Touist"

@app.route('/touist_cmd', methods=['POST'])
def touist_cmd():
    try:
        data = request.get_json()
        args = data.get('args', '')
        stdin_data = data.get('stdin', '')
        print("args : \n", args)
        print("stdin : \n", stdin_data)
        result = run_touist_command(args, stdin_data)
        return jsonify(result)

    except Exception as e:
        print(f"[ERROR in jsonify] : : {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7015)
