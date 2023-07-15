
#declaração das variáveis
maiorMaxTemp=-100
menorMaxTemp =100
somaMaxTemp=0
qteMesEscald=0
mesEcald=0
mesMenosQuente=0


#contador:
for count in range (12): 
    #Entradas:
    mes=int(input("Informe o mês,utilizando um número inteiro de 1 a 12  para o mês correspondente: "))
    tempMax=float(input("Informe a termperatura em graus Celsius, num intervalo de -90 a 60 °C: "))
    #Validação das entradas:
    if mes<1 or mes>12:print("Erro: mês no intervalo errado")
    elif tempMax<-90 or tempMax>60:print("Erro: temperatura no intervalo errado")
    #Meses por extenso:
    if mes==1: mes="Janeiro"
    elif mes==2: mes="Fevereiro"
    elif mes==3: mes="Março"
    elif mes==4: mes="Abril"
    elif mes==5: mes="Maio"
    elif mes==6: mes="Junho"
    elif mes==7: mes="Julho"
    elif mes==8: mes="Agosto"
    elif mes==9: mes="Setembro"
    elif mes==10: mes="Outubro"
    elif mes==11: mes="Novembro"
    else: mes="Dezembro"
    #Quantidade de  meses escaldantes:
    if tempMax>40:
        qteMesEscald+=1
    #Mês que apresentou maior temperatura máxima:
    if tempMax>maiorMaxTemp:
        maiorMaxTemp=tempMax
        mesEcald=mes
    #Mês que apresentou menor temperatura máxima:
    if tempMax<menorMaxTemp:
           menorMaxTemp=tempMax
           mesMenosQuente=mes
    #Média:
    somaMaxTemp+=tempMax
    tempMaxMedia = somaMaxTemp/12

print(f"Temperatura média máxima anual: {tempMaxMedia:.3f}")
print(f"Quantidade de meses escaldantes, ou seja, com temperatura maior que 40°C: {qteMesEscald}")
print(f"Mês mais escaldante do ano, ou seja, mês que apresentou maior temperatura máxima do ano: {mesEcald}")
print(f"Mês menos quente do ano: {mesMenosQuente}")


    