def calculaDiametro(raio):
    return 2 * raio
def calculaCircunferencia(pi, raio):
    return pi * raio * 2
def calculaAreaCircunferencia(pi, raio):
    return pi * (raio ** 2)
#main
raio = float(input("Digite o valor do raio:"))
pi = 3.14159

diametro = calculaDiametro(raio)
Circunferencia = calculaCircunferencia(pi, raio)
area = calculaAreaCircunferencia(pi, raio)

print("calcula diametro", diametro)
print("calcula circunferencia", Circunferencia)
print("calcula area circunferencia", area)
