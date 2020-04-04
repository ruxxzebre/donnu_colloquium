
with open("conditions.txt", "r") as f:
    temp_list = f.readlines()
    conditions_list = []
    j = -1
    for i in temp_list:
        if i[0].isdigit():
            conditions_list.append([i])
            j += 1
        else:
            conditions_list[j].append(i)

conditions_list = [("".join(i)).replace('\n', '') for i in conditions_list]

import pickle

with open('conditions.bin', 'wb') as f:
    pickle.dump(conditions_list, f, protocol=4)

with open('conditions.bin', 'rb') as f:
    a = pickle.load(f, encoding="utf8")

