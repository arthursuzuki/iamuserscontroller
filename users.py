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
                    print(f"User {user} removed from list.")
                
            else:
                print(f"Usuário {user} not found.")
        
        print(f"Final users list: {users}")
    except:
        print("Error creating users exceptions")


def createUsersList():
    users = str(input("Place here the names of the users: "))
    users = users.split()
    return(users)


def readUsersFromCsv():
    import csv

    csv_file = 'data.csv'
    users = list()
    emails = list()

    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            users.append(row[0])  
            emails.append(row[1])

    return(users,emails)


def matchUsersWithEmail(users):
    import csv
    csv_file = 'data.csv'
    emails = []
    
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            usuario = row[0]  
            email = row[1]    
            
            if usuario in users:
                emails.append((usuario, email))
    
    return (emails)





