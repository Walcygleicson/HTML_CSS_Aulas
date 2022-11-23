x = input('Nome: ').split()
ex = ['da', 'de', 'do']

iniciais_list = list()
iniciais_str = str()
for i in x:
    cont = 0
    if i.lower() not in ex:
        for letra in i:
            if cont <= 0:
                iniciais_list.append(letra.upper()+". ")
                cont = 1

iniciais_str = iniciais_str.join(iniciais_list)
print(f'AS INICIAIS SÃO: {iniciais_str}')
