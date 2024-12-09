"""
@author: Mykaelle
"""
from flask import Flask  

app_Mykaelle = Flask (__name__)

@app_Mykaelle.route('/')    
@app_Mykaelle.route('/rota1') 
def rota1(): 
    return 'Olá, turma!'

@app_Mykaelle.route('/rota2')
def rota2():
    resposta = "<H3> Essa é outra página da rota 2 <H3>"
    return resposta

def saudacoes (nome): 
    return f'Olá, {nome}'

if __name__ == "__main__" :
    app_Mykaelle.run(port = 8000)  #executa aplicação

