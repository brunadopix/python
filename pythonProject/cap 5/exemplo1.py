def validaLogin(nome, senha):
    if(nome == "Jose" and senha == "senha123"):
        return print("Seja bem vindo", nome, senha)
    else:
        return print("Senha ou login inválidos")


print("=== Digite seu nome ===")
nome = input()
print("=== Digite sua senha ===")
senha = input()

validaLogin(nome, senha)