def maior_valor(lista):
    try:
        first_length = len(lista[0])
        last_length = len(lista[-1])

        if first_length >= last_length:
            return first_length
        else:
            return last_length
    except IndexError:
        return 0
    
class Error(Exception):
    pass

def arithmetic_arranger(numeros,teste=False):
    conjunto1 = ''
    conjunto2 = ''
    conjunto3 = ''
    conjunto4 = ''
    espaco = ' '
    barra = '-'

    for item in numeros:
 
        if item != numeros[-1]:

            item = item.split(' ')

            if len(item[0]) > 4:
                raise Error("Numbers cannot be more than four digits.")

            if item[0].isdigit() and item[-1].isdigit():
                valor1 = int(item[0])
                valor2 = int(item[-1])
            else:
                raise Error("Numbers must only contain digits.")
            
            
            sinal = item[1]
            if sinal == '+' or sinal == '-':
                maior = maior_valor(item)

                conjunto1 += (str(f'{espaco * (maior + 2 - len(item[0]))}{(item[0])}{espaco * 4}'))
                conjunto2 += (str(f'{item[1]}{espaco * (maior + 1 - len(item[-1]))}{(item[2])}{espaco * 4}'))
                conjunto3 += f'{barra * (maior + 2)}{espaco * 4}'
                if teste == True:
                    valor1 = int(item[0])
                    valor2 = int(item[-1])
                    if sinal == '+':
                        total = valor1 + valor2 
                        conjunto4 += f'{espaco * ((maior + 2)-len(str(total)))}{total}{espaco * 4}' 
                    elif sinal == '-':
                        total = valor1 - valor2 
                        conjunto4 += f'{espaco * ((maior + 2)-len(str(total)))}{total}{espaco * 4}'
            else:
                raise Error("Operator must be '+' or '-'.")        
        else:
            
            item = item.split(' ')
            
            if item[0].isdigit() and item[-1].isdigit():
                valor1 = int(item[0])
                valor2 = int(item[-1])
            else:
                raise Error("Numbers cannot be more than four digits.")
                
            sinal = item[1]
            if sinal == '+' or sinal == '-':
                maior = maior_valor(item)
                
                conjunto1 += (str(f'{espaco * (maior + 2 - len(item[0]))}{(item[0])}'))
                conjunto2 += (str(f'{item[1]}{espaco * (maior + 1 - len(item[-1]))}{(item[2])}'))
                conjunto3 += f'{barra * (maior + 2)}'
                if teste == True:
                    if sinal == '+':
                        total = valor1 + valor2 
                        conjunto4 += f'{espaco * ((maior + 2)-len(str(total)))}{total}' 
                    elif sinal == '-':
                        total = valor1 - valor2 
                        conjunto4 += f'{espaco * ((maior + 2)-len(str(total)))}{total}'                    
            else:
                raise Error("Operator must be '+' or '-'.") 
        
    print(f'{conjunto1}\n{conjunto2}\n{conjunto3}\n{conjunto4}')