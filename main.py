people = int(input('количество человек:'))
c = int(input('число в считалке:'))
print(' каждый выбывает', c, 'человек')
a = [i for i in range(1, people+1)]
start = 0
while len (a)>1:
    print('людей:', a)
    print('начало счета', a[start])
    delete = (start+c-1)%len(a)
    if a[delete] == a[-1]:
        start = 0
    else: start = delete
    print('номер человека', a.pop(delete))
    print('остался', a[0])



