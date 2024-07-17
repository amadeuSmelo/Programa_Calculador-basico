# SOMA
# SUBTRAÇÃO
# MUTIPLICÇÃO
# DIVISÃO
# RESTO DA DIVISÃO
# POTÊNCIA

print('|---------------------------|'
      '\n|    {1} _SOMA              | '
      '\n|    {2} _SUBTRAÇÃO         |'
      '\n|    {3} _MULTIPLICÇÃO      |'
      '\n|    {4} _DIVISÃO           |'
      '\n|    {5} _RESTO DA DIVISÃO  |'
      '\n|    {6} _POTÊNCIA          |')
print('|---------------------------|')

S_N = str(input('\nVocê deseja realisa alguma operação? \n'))

if S_N == 'sim':
    operacao_desejada = int(input('De 1 a 6, qual operação você deseja realiza!: '))

    # _SOMA
    if operacao_desejada == 1:
        print('Certo, então você deseja {1} _soma. Vamos la!')

        soma1_desejada = int(input("Digite o primeiro valor: \n"))
        soma2_desejada = int(input("Digite o segunda valor: \n"))

        resultado = soma1_desejada + soma2_desejada

        print('------------------------------------------|')
        print('A soma entre ' + str(soma1_desejada) + ' e ' + str(soma2_desejada) + ' é igual a: ' + str(
            resultado))
        print('------------------------------------------|')

    # _SUBTRAÇÃO
    elif operacao_desejada == 2:
          print('Certo, então você deseja {2} _SUBTRAÇÃO. Vamos la!')

          subtracao1_desejada = int(input("Digite o primeiro valor: \n"))
          subtracao2_desejada = int(input("Digite o segunda valor: \n"))
  
          resultado = subtracao1_desejada - subtracao2_desejada
          print('------------------------------------------|')
          print('A subtração entre ' + str(subtracao1_desejada) + ' e ' + str(subtracao2_desejada) + ' é igual a: ' + str(
              resultado))
          print('------------------------------------------|')
    # _MULTIPLICÇÃO
    elif operacao_desejada == 3:
         print('Certo, então você deseja {3} _MULTIPLICÇÃO. Vamos la!')

         multiplicação1_desejada = int(input("Digite o primeiro valor: \n"))
         multiplicação2_desejada = int(input("Digite o segunda valor: \n"))
  
         resultado = multiplicação1_desejada * multiplicação2_desejada
         print('------------------------------------------|')
         print('A multiplicaçãoo entre ' + str(multiplicação1_desejada) + ' e ' + str(multiplicação2_desejada) + ' é igual a: ' + str(
             resultado))
         print('------------------------------------------|')

    # _DIVISÃO
    elif operacao_desejada == 4:
         print('Certo, então você deseja {4} _DIVISÃO. Vamos la!')

         divisao1_desejada = int(input("Digite o primeiro valor: \n"))
         divisao2_desejada = int(input("Digite o segunda valor: \n"))
  
         resultado = divisao1_desejada / divisao2_desejada
         print('------------------------------------------|')
         print('A divisao entre ' + str(divisao1_desejada) + ' e ' + str(divisao2_desejada) + ' é igual a: ' + str(
             resultado))
         print('------------------------------------------|')

    # _RESTO DA DIVISÃO
    elif operacao_desejada == 5:  
         print('Certo, então você deseja {4}RESTO_DA_DIVISÃO. Vamos la!')

         resto_divisao1_desejada = int(input("Digite o primeiro valor: \n"))
         resto_divisao2_desejada = int(input("Digite o segunda valor: \n"))
  
         resultado = resto_divisao1_desejada % resto_divisao2_desejada
         print('------------------------------------------|')
         print('A divisao entre ' + str(resto_divisao1_desejada) + ' e ' + str(resto_divisao2_desejada) + ' é igual a: ' + str(
             resultado))
         print('------------------------------------------|')        
         resto_desejada = int(input("Qual resto da divisão você deseje realiza: \n"))
   
    # _POTÊNCIA
    elif operacao_desejada == 6:
         print('Certo, então você deseja {6} _POTÊNCIA. Vamos la!')

         potencia1_desejada = int(input("Digite o primeiro valor: \n"))
         potencia2_desejada = int(input("Digite o segunda valor: \n"))
  
         resultado = potencia1_desejada ** potencia2_desejada
         print('------------------------------------------|')
         print(str(potencia1_desejada) + ' elevado a ' + str(potencia2_desejada) + ' é igual a: ' + str(
             resultado))
         print('------------------------------------------|')        

    # _POTÊNCIA
    else:
        
        print('TCHAU')

elif S_N == 'não':
        print("TCHAU E OBRIGADO! (*__*)")
