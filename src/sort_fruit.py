with open("py3basics_2.1/py3basics/DATA/fruit.txt") as f:
    fruit_list = []
    read_fruits = f.readlines()
    for r in read_fruits:
        r = r.rstrip('\n')
        fruit_list.append(r)
    sorted_case_sense = sorted(fruit_list)
    print(sorted_case_sense)
    sorted_case_insens = sorted(fruit_list, key=str.casefold)
    print(sorted_case_insens)
    sorted_by_len_name = sorted(fruit_list, k)