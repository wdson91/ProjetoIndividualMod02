# Projeto Individual Mod02
**Como rodar o código:**

 - Faça um fork do repositório e depois um git clone em:  https://github.com/wdson91/ProjetoIndividualMod02.git 
 - Em seguida rode no vscode em uma máquina que tenha o python instalado

**Descrição do código:**

O código apresentado é uma implementação que busca candidatos aprovados com base em notas mínimas fornecidas para a entrevista, teste teórico, teste prático e soft skills. O código é dividido em três partes principais:

1. **Preparação dos dados:**
   - A lista `candidatos` contém informações dos candidatos, como nome e resultado em formato de string.
   - A variável `numeros` é uma lista que armazena apenas as notas de cada candidato, extraídas da string de resultados.

2. **Validação das entradas:**
   - A função `validarEntrada` é usada para solicitar ao usuário as notas mínimas desejadas e validar se os valores inseridos são inteiros válidos.

3. **Busca dos candidatos aprovados:**
   - A função `buscarCandidato` recebe as notas mínimas fornecidas como parâmetros.
   - Para cada candidato e suas notas na lista `numeros`, verifica-se se todas as notas mínimas fornecidas são maiores ou iguais às notas do candidato.
   - Se um candidato atender aos requisitos mínimos, ele é adicionado à lista de aprovados `aprovados`.
   - Por fim, os candidatos aprovados são impressos na tela, ou uma mensagem de nenhum candidato aprovado é exibida se a lista `aprovados` estiver vazia.

**Exemplo de uso:**

Ao executar o código, o usuário será solicitado a fornecer as notas mínimas desejadas para cada etapa (entrevista, teste teórico, teste prático e soft skills). Após a entrada de valores válidos, o código buscará os candidatos aprovados com base nessas notas mínimas e exibirá uma lista com os nomes dos candidatos aprovados e suas respectivas notas.

É importante lembrar que a função `buscarCandidato` é chamada no final do código, passando as notas mínimas fornecidas pelo usuário como argumentos. Para testar o código com outras notas, é possível modificar as chamadas dessa função com diferentes valores de notas mínimas.
