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


def validarEntrada(mensagem):
        while True:
            try:
                entrada = int(input(mensagem))
                print('-'*60)
                return entrada
            except ValueError:
                print("Por favor, insira um valor inteiro válido.")
    
    
nota1 = validarEntrada("Informe a nota mínima desejada para a entrevista: ")
nota2 = validarEntrada("Informe a nota mínima desejada para o teste teórico: ")
nota3 = validarEntrada("Informe a nota mínima desejada para o teste prático: ")
nota4 = validarEntrada("Informe a nota mínima desejada para as soft skills: ")

def buscarCandidato(nota1,nota2,nota3,nota4):
    aprovados = []
    listaResultado = [nota1,nota2,nota3,nota4]
    
    for i,lista in enumerate(numeros):
        if all(x <= y for x, y in zip(listaResultado, lista)):
            aprovados.append({candidatos[i]['nome']:lista})

    print('Nenhum candidato aprovado com essas notas') if len(aprovados) <1 else print(f'Candidatos Aprovados:{aprovados}')


buscarCandidato(nota1,nota2,nota3,nota4)



# buscarCandidato(4,10,8,8)    