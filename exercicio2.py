# Maurício de Azevedo Neto


# Crie a função que será avaliada no exercício aqui

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    count1 = {}
    count2 = {}

    for caractere in str1:
        if caractere in count1:
            count1[caractere] += 1
        else:
            count1[caractere] = 1

    for caractere in str2:
        if caractere in count2:
            count2[caractere] += 1
        else:
            count2[caractere] = 1

    return count1 == count2


# Teste a sua função aqui (caso ache necessário)
