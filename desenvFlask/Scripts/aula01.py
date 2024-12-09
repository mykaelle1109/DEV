from flask import Flask

app_Mykaelle = Flask (__name__)

@app_Mykaelle.route('/')
def raiz():
    return 'Olá, Mykaelle Araujo!'

app_Mykaelle.run()