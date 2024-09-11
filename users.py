import boto3
from botocore.exceptions import *

# Cria uma sessão com o cliente IAM
client = boto3.client('iam')

def getUsersList():
    # Chama o método list_users
    try:
        response = client.list_users()

        # Itera sobre os usuários e imprime o nome de cada um
        for user in response['Users']:
            print(f"UserName: {user['UserName']}, UserId: {user['UserId']}")

        users = list()
        for user in response['Users']:
            users.append(user['UserName'])
        users.remove("admin")
        print(users)
        return users
    except:
        print(Exception)


def createUsersException(users):
    try:
        entrada = input("Enter the users to remove (separated by space): ")
        lista = entrada.split()
        print(f"Users to be removed: {lista}")
        for user in lista:
            if user in users:
                users.remove(user)
                print(f"Usuário {user} removed from list.")
            else:
                print(f"Usuário {user} not found.")
        
        print(f"Lista final de usuários: {users}")
    except:
        print("Error creating users exceptions")
