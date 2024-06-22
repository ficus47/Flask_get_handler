import requests

url = "https://172.16.5.4:5000/serv"
file_path = "image.jpg"

with open(file_path, 'rb') as f:
    files = {'image': f}
    data = {'mod': 'valid'}
    response = requests.post(url, files=files, data=data, verify=False)  # Désactiver la vérification SSL pour les certificats auto-signés
    print(response.text)
