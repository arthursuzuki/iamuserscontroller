import os
from generatepassword import generate_password
import subprocess

password = generate_password()
print(password)

command = [
    "aws", "iam", "update-login-profile",
    "--user-name", f"iuctester",
    "--password", f"{password}"
]

# Executa o comando no CMD usando subprocess
try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print("Comando executado com sucesso:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar o comando: {e}")
    print(e.stderr)