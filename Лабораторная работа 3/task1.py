
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def function(a):
    for i in range(0, len(items_list)):
        if a == items_list[i]:
            return i

for find_item in ['банан', 'груша', 'персик']:
    index_item = function(find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
