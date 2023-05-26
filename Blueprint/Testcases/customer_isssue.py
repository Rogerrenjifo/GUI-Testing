def solution(lista):
    index = 0
    new_list = []
    count = 0

    for i in range(len(lista) - 1):
        if lista[i] + 1 != lista[i + 1]:
            if count >= 2:
                new_list.append(str(lista[index]) + "-" + str(lista[i]))
                new_list.append(",")
            else:
                if count == 1:
                    new_list.append(str(lista[i - 1]))
                    new_list.append(",")
                new_list.append(str(lista[i]))
                new_list.append(",")
            index = i + 1
            count = 0
        else:
            count += 1

    if count >= 2:
        new_list.append(str(lista[index]) + "-" + str(lista[-1]))
    else:
        if count == 1:
            new_list.append(str(lista[-2]))
            new_list.append(",")
        new_list.append(str(lista[-1]))

    result = "".join(new_list)
    return result
