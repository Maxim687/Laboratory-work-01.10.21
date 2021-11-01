cont = 'y'
while cont == 'y':
    print ("Виберіть групу з якою будете працювати: 1. Група Менеджменту. 2. Група Кіберпезпеки. 3. Група Журналістики")
    e = int(input())
    def studs():
        if e == 1:
            return 'students.txt'
        elif e == 2:
            return 'students2.txt'
        elif e == 3:
            return 'students3.txt'
    studs = studs()
    choice = int(input("Виберіть потрібну дію: 1. Читання, 2.Повний перезапис файла, 3.Дозапис у файл, 4. Пошук данних у файлі, 5.Сортування списка"))
    if choice == 1:
        f =open('students.txt','r', encoding = 'utf-8')
        reader = f.read()
        print (reader)
        f.close()
    elif choice == 2:
        f = open ('students.txt','w',encoding = 'utf-8')
        f.write ('Повний перезапис')
        f.close()
    elif choice == 3:
        fd = open ('students.txt','a',encoding = 'utf-8')
        newball = input ("Введіть бали ЗНО:")
        newstud = input ("Введіть ПІБ:")
        fd.write ('\n'+newball+" "+newstud)
        f.close()
    elif choice == 4:
        search = input("Введите что хотите найти: ")
        print (search)
        f = open ('students.txt', 'r', encoding = 'utf-8')
        reader = f.read()
        if search in reader:
         print ("Найден")
        else:
         print ("Не найден")
    elif choice == 5:
        f = open ('students.txt', 'r', encoding = 'utf-8')
        for l in sorted(f):
            print(l, end = ' ')