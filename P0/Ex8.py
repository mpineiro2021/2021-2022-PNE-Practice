import Seq0
dict_list, list_genes = Seq0.seq_count()
value_list = []
i = 0
while i < len(dict_list):
    for d in dict_list[i]:
        max_key = max(d, key=d.get)
    value_list.append(max_key)
    i += 1
print(value_list)

