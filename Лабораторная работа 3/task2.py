
def find_common_participants(a, b, c=","):
    ar_a = a.split(c)
    ar_b = b.split(c)
    d=[]
    for i in ar_a:
        for g in ar_b:
            if i == g and i not in d:
                d.append(i)
    return d

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

array = find_common_participants(participants_first_group, participants_second_group, "|")
array = sorted(array)