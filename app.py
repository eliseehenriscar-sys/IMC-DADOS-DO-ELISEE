def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 24.9:
        classificacao = "Peso normal"
    elif imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    return imc, classificacao

if __name__ == "__main__":
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc, classificacao = calcular_imc(peso, altura)
    print(f"Seu IMC é {imc:.2f} ({classificacao})")
