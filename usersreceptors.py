import boto3

# Cria uma sessão com o cliente IAM
client = boto3.client('iam')

# Chama o método list_users
response = client.list_users()

# Itera sobre os usuários e imprime o nome de cada um
for user in response['Users']:
    print(f"UserName: {user['UserName']}, UserId: {user['UserId']}")
