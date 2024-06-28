"""
Escreva um programa que solicite uma senha ao
usuário e verifique se ela corresponde a uma 
senha pré-definida 
"""

senha = input('Digite sua senha de acesso: ')
senha_pre_definida = '856479'

if senha == senha_pre_definida:
    print('Sua senha estar correta! ')
else:
    print('Senha incorreta, tente novamente.')