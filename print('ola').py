candidatos = [
    {'nome': 'João', 'resultado': 'e6_t8_p7_s9'},
    {'nome': 'Maria', 'resultado': 'e8_t7_p9_s8'},
    {'nome': 'José', 'resultado': 'e4_t6_p8_s7'},
    {'nome': 'Ana', 'resultado': 'e7_t9_p6_s9'},
    {'nome': 'Carlos', 'resultado': 'e6_t8_p8_s7'}
]




numeros = []

for candidato in candidatos:
    sublista = candidato['resultado'].split('_')  # separa a string em uma lista
    
    numeros_candidato = []
    for item in sublista:
        if item[1:].isdigit():  # verifica se o elemento é um número
            numeros_candidato.append(int(item[1:]))  # converte e adiciona o número à lista
    numeros.append(numeros_candidato) # criando uma lista somente com as notas de cada candidato



def buscarCandidato(nota1,nota2,nota3,nota4):
    listaResultado = [nota1,nota2,nota3,nota4]
    aprovados = []
    for i,numero in enumerate(numeros):
        if listaResultado >=  numeros[i]:
            aprovados.append(candidatos[i]['nome'])
        
    print(f'Candidatos Aprovados:{aprovados}')



buscarCandidato(4,10,8,8)    