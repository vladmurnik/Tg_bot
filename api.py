import requests

def api_joke(text):
    res = requests.get(f'http://rzhunemogu.ru/RandJSON.aspx?CType={text[6::]}')
    return(res.text[12:len(res.text) - 2])


def api_cat(message):
    base = ''
    if (message.text[5::]).isdigit():
        for i in range(int(message.text[5::])):
            response = requests.get(f'https://api.thecatapi.com/v1/images/search')
            if response.status_code == 200:
                data = response.json()
                image_url = data[0]['url']
                base = base + image_url + ' '
        return(base)
    else:
        response = requests.get(f'https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            data = response.json()
            image_url = data[0]['url']
            return(image_url)

def api_dog(message):
    base = ''
    if (message.text[5::]).isdigit():
        for i in range(int(message.text[5::])):
            response = requests.get(f'https://api.thedogapi.com/v1/images/search')
            if response.status_code == 200:
                data = response.json()
                image_url = data[0]['url']
                base = base + image_url + ' '
        return(base)
    else:
        response = requests.get(f'https://api.thedogapi.com/v1/images/search')
        if response.status_code == 200:
            data = response.json()
            image_url = data[0]['url']
            return(image_url)