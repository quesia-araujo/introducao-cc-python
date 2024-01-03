def remove_repetidos(lista):
    lista_sem_repeticao = []

    for elemento in lista:
        if elemento not in lista_sem_repeticao:
            lista_sem_repeticao.append(elemento)
            
    list.sort(lista_sem_repeticao)

    return lista_sem_repeticao