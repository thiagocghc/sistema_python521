print("POMPEU MAROMBA")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso, ",imc)

elif imc > 18.5 and imc <= 25:
    print("Peso normal: ",imc)

if imc > 25 and imc < 29.99: 
    print("Obesidade")

