# Write a function that takes an iterable (something you can loop through, ie: string, list, or tuple) and produces a dictionary with all distinct elements as the keys, and the number of each element as the value
def count_unique(some_iterable):
    d = {}

    while some_iterable != []:
        key = some_iterable.pop()
        d[key] = d.get(key, 0) + 1

    print d


# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists
def common_items(list1, list2):
    list_mash = []

    temp1 = list1[:]
    while temp1 != []:
        i = temp1.pop()
        temp2 = list2[:]
        while temp2 != []:
            j = temp2.pop()
            if i == j:
                list_mash.append(i)

    print list_mash


# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists. This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    d = {}
    list_mash = []
    temp1 = list1[:]
    temp2 = list2[:]

    while temp1 != []:
        i = temp1.pop()
        d[i] = d.get(i, True)
    while temp2 != []:
        j = temp2.pop()
        d[j] = d.get(j)
        if d[j] == True:
            list_mash.append(j)
    print list_mash

first_list = ["hug", 'bug', 'tug', 'glug', 'a', 'e', 'f']
second_list = ['a', 'b', 'c', 'd', 'tug', 'glug', 'e', 'f']

count_unique(["dog", "dog", "cat", "rat", "Pat", "dog"])

common_items2(first_list, second_list)