#!/user/bin/python3

def uniq_add(my_list=[]):
    uniq_list = list()
    sum = 0
    for i in my_list:
        for x in uniq_list:
            if i == x:
                break
        uniq_list.append(i)
        sum += i

    return sum
