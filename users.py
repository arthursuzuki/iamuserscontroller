import boto3

# Cria uma sessão com o cliente IAM
client = boto3.client('iam')

def getUsersList():
    # Chama o método list_users
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

def createUsersException(users):
    entrada = input("Enter the users to remove (separated by space): ")
    lista = entrada.split()
    print(f"Usuários a serem removidos: {lista}")
    for user in lista:
        if user in users:
            users.remove(user)
            print(f"Usuário {user} removido da lista.")
        else:
            print(f"Usuário {user} não encontrado na lista.")
    
    print(f"Lista final de usuários: {users}")

