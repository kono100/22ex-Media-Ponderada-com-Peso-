
#22. Faça uma função que receba por parâmetro três notas de um aluno e três pesos. Calcule e
#retorne sua Média Ponderada. A média ponderada de n números é a soma dos produtos de
#cada um multiplicados por seus respectivos pesos, dividida pela soma dos pesos, isto é:


Nota1 = float(input("\nDigite a 1° Nota: "))
peso1 = float(input("Digite o 1° Peso: "))

Nota2 = float(input("\nDigite a 2° Nota: "))
peso2 = float(input("Digite o 2° Peso: "))

Nota3 = float(input("\nDigite a 3° Nota: "))
peso3 = float(input("Digite o 3° Peso: "))

mediaPonderada = ((Nota1*peso1)+(Nota2*peso2)+(Nota3*peso3))/(peso1+peso2+peso3)

print(f"\nMedia Ponderada = {mediaPonderada:,.1f}\n")