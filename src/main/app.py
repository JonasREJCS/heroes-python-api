from flask import Flask
app = Flask(__name__)
from Hero import Hero

@app.route('/')
def index():
    return 'O servidor tá funfando!'

@app.route('/heroes')
def heroes():
    lista = {}

    lista[11] = 'Bebe Rexha'
    lista[12] = 'Alok'
    lista[13] = 'Glória Groove'
    lista[14] = 'Drake'
    lista[15] = 'The Black Eyed Peas'
    lista[16] = 'Lady Gaga'
    lista[17] = 'Rihanna'
    lista[18] = 'P!nk'
    lista[19] = 'Anitta'
    lista[20] = 'Katy Perry'
    lista[21] =  'Pablo Vittar'

    return lista