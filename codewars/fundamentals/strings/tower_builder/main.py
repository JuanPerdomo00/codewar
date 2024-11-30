def tower_builder(n_floors: int):
    # build here
    # lista_impares = []
    # lista_aux = [i for i in range(1, n_floors + 1)]
    # aux_n = n_floors

    # print(lista_aux)
    # for i in range(1, aux_n, 2):
    #     if len(lista_impares) <= len(lista_aux):
    #         lista_impares.append(i)
    #         aux_n += 1

    towr: list[str] = ["*" * i for i in range(1, n_floors * 2, 2)]
    new_towr = []

    for i, t in enumerate(towr):
        spaces = " " * (n_floors - i - 1)
        new_towr.append(spaces + t + spaces)

    return new_towr


print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(6))
