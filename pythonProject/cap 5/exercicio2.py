def apresentaçao(nome, nomeMae, nomePai):
    print(f"Nome: {nome}")
    print(f"Nome da mae: {nomeMae}")
    print(f"Nome do pai: {nomePai}")

nome = str(input("Digite seu nome completo"))
nomeMae = str(input("Digite o nome completo da sua mae"))
nomePai = str(input("Digite o nome completo do seu pai"))

apresentaçao(nome, nomeMae, nomePai)