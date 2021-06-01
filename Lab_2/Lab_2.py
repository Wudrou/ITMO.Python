# Работа со строками.
# 1, 2, 3
string1 = "This is a string."
string2 = " This is another string."
print(string1 + string2)
print(len(string1))
print(string1.title())
print(string1.lower())
print(string1.upper())
print(string1.rstrip())
print(string1.lstrip())
print(string1.strip)
print(string1.strip('.'))
# 4, 5, 6, 7
d = "qwerty"
ch = d[2]
print(ch)
chm = d[1:3]
chm1 = d[1:]
chm2 = d[:3]
chm3 = d[:]
chm4 = d[1:5:2]
print(chm, chm1, chm2, chm3, chm4)

# Работа с числами.
# 1, 2, 3
a = 10
b = 5
print(a / b, a % b, a ** 3)
param = "string" + str(15)
print(param)

# Преобразование данных
# 1
param = "string" + str(15)
print(param)
#2
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)

# Форматирование строк
# 1, 2, 3
a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

# Списки
# 1, 2, 3
list1 = [82,8,23,97,92,44,17,39,11,12]
dir(list1)
help(list1.insert)
help(list1.append)
help(list1.sort)
help(list1.remove)
help(list1.reverse)
# 4
list1[0] = 100
list1[3] = 98
print(list1)
# 5
list1.append(5)
print(list1)
# 6
list1.insert(5, 444)
print(list1)
# 7
del list1[0]
print(list1)
# 8
del list1[-1]
print(list1)

#Сортировка элементов списка
# 1, 2
list1.sort(reverse=True)
print(list1)
# 3, 4, 5
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(list2, lis)

# Кортежи
# 1, 2
print(dir(tuple))
help(lis.count)
help(lis.index)
# 3, 4
seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
# 5, 6, 7
listseq = list(seq)
print(type(listseq))

# Словари
# 1, 2
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D)
# 3
dp = {}
dp['name'] = input("Введите имя: ")
dp['age'] = input("Введите возраст: ")
print(dp)

# Вложенность хранения данных
# 1, 2
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
'job': ['dev', 'mgr'],
'age': 25}
print(rec['name']['firstname'] + ' ' + rec['name']['lastname'])
print(rec['name']['firstname'])
print(rec['job'])
# 3, 4
rec['job'].append('janitor')
print(rec)