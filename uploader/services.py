from django.contrib.auth import authenticate
from .repositories import createUserInDataBase
import requests
import pandas as pd

def verifyUsers(data):
    
    username = data['data']['username']
    password = data['data']['password']

    user = authenticate(username=username, password=password)

    return user if user else False
 
def createUsers(data):
    username = data['data']['username']
    password = data['data']['password']
    email = data['data']['email']

    user = createUserInDataBase(username, email, password)

    return True if user else False
    
def uploadFile(request):

    file = request.FILES.get('file')
    email = request.data.get('email')

    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    elif file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        raise ValueError("Formato de arquivo não suportado")
    
    print(file.name)

    files = {'file': (file.name, file)}
    data = {'email': email}

    response = requests.post('http://localhost:5000/upload/sendEmail', files=files, data=data)

    return True if response.status_code == 200 else False