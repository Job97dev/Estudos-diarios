"""
A sintaxe geral segue esta ordem mental:

nova_lista = [expressao for item in iteravel if condicao]
"""


numeros = [10,20,30,40,50]

numeros_dobros = [num - 5 for num in numeros]


nomes = ['joabe', 'carol', 'jairo']

maiusculos = [nome.upper() for nome in nomes]



concentracao = [59,55,53,55,61,62,52,52,63,54,21,58,]

num_par = [num for num in concentracao if num % 2 == 0]
num_impar = [num for num in concentracao if num % 2 != 0]

print(f'concentraçoes pares: {num_par}')
print(f'concentraçoes inpares: {num_impar}')
