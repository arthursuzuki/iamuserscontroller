import subprocess
from generatepassword import generate_password
from users import getUsersList,createUsersException
from login import loginAws

#NAO RODAR
#se for rodar tirar esse exit()

loginAws()


print("passo")
exit(1)
users = list(getUsersList())
i = int(input("You have any users exeptions? (1 for yes, other number to continue )"))
if(i==1):
    users = createUsersException(users)

i = users.count()

for i in users:
    newPassword = generate_password()
    print(newPassword)
    command = [
        "aws", "iam", "update-login-profile",
        "--user-name", f"{users[i]}",
        "--password", f"{newPassword}"
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Comando executado com sucesso:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
        print(e.stderr)

    i = i-1
