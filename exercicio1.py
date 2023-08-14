# Maurício de Azevedo Neto


# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(frase):
    frase = frase.lower()
    palavras = frase.split()
    palavras_unicas = set(palavras)

    return len(palavras_unicas)


# Teste a sua função aqui (caso ache necessário)
