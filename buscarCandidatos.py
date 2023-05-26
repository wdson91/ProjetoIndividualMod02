lista_candidatos = [
    {'nome': 'João', 'resultado': 'e6_t8_p7_s9'},
    {'nome': 'Maria', 'resultado': 'e8_t7_p9_s8'},
    {'nome': 'José', 'resultado': 'e4_t6_p8_s7'},
    {'nome': 'Ana', 'resultado': 'e7_t9_p6_s9'},
    {'nome': 'Carlos', 'resultado': 'e6_t8_p8_s7'}
]

notas_candidatos = []

def validarEntrada(mensagem):
        
        while True:
            print('-'*60)
            try:
                entrada = int(input(mensagem))
                
                return entrada
            except ValueError:
                print("Por favor, insira um valor inteiro válido.")


nota1 = validarEntrada("Informe a nota mínima desejada para a entrevista: ")
nota2 = validarEntrada("Informe a nota mínima desejada para o teste teórico: ")
nota3 = validarEntrada("Informe a nota mínima desejada para o teste prático: ")
nota4 = validarEntrada("Informe a nota mínima desejada para as soft skills: ")



for candidato in lista_candidatos:
        resultado_split = candidato['resultado'].split('_')  # separa a string em uma lista
        
        numeros_candidato = []
        for item in resultado_split:
            if item[1:].isdigit():  # verifica se o elemento é um número
                numeros_candidato.append(int(item[1:]))  # converte e adiciona o número à lista
        notas_candidatos.append(numeros_candidato) # criando uma lista somente com as notas de cada candidato

def buscarCandidato(nota1,nota2,nota3,nota4):
    aprovados = []
    lista_resultado = [nota1,nota2,nota3,nota4]
    
    for i,lista in enumerate(notas_candidatos):
        
        if all(x <= y for x, y in zip(lista_resultado, lista)):
            aprovados.append({lista_candidatos[i]["nome"]:lista})
            
    if len(aprovados) <1 :
        print('-'*60)
        print("\n Nenhum candidato aprovado com essas notas")   
    print('-'*60)
    print("\nCandidatos aprovados com as respectivas notas informadas:\n")
    
    for i,candidato in enumerate(aprovados):
        nome = list(candidato.keys())[0]
        notas = candidato[nome]
        print(f'{i+1} - {nome}: {", ".join(str(nota) for nota in notas)}\n')
    print('-'*60)








buscarCandidato(nota1,nota2,nota3,nota4)



