def spiski(f):
    opilased = []
    proguly = []
    for row in f:
        row=row.split()
        opilased.append(row[0]+' '+row[1])
        proguly.append(int(row[2]))
    return opilased, proguly
    
def sorteerimine(proguly,opilased,n): #Фукция, которая сортирует списки
    abi_p = 0
    abi_o = ""
    for i in range(0,n-1):
        for j in range(i+1,n):
            if proguly[i]>proguly[j]:
                abi_p=proguly[i]
                proguly[i]=proguly[j]
                proguly[j]=abi_p
                abi_o=opilased[i]
                opilased[i]=opilased[j]
                opilased[j]=abi_o
    return proguly,opilased

def komissija(proguly,opilased,n): # Выводит спсиок тех кто идёт на комисию
    komiss = []
    for i in range(n):
        if proguly[i] > 50 and proguly[i] < 100:
            komiss.append(opilased[i]+' прогулял '+ str(proguly[i]) + ' раз')
    return komiss

def delete(proguly,opilased,n): # Функция удаляет из списка  учеников, у которых прогулов больше чем 100
    new_proguly = []
    new_opilased = []
    for i in range(n):
        if proguly[i] < 100:
            new_proguly.append(proguly[i])
            new_opilased.append(opilased[i])
    return new_proguly,new_opilased

def my_choice(opilased,n,bukva): # Функция выводит фамилии начинающиеся на букву, который ввёл пользователь
    choice = []
    for i in range(n):
        space = opilased[i].find(' ')        ## находим номер места пробела между именем и фамилией
        if opilased[i][space+1] == bukva.capitalize(): ## если следующая после пробела буква равна введённой
            choice.append(opilased[i][space+1:] + ', ' + opilased[i][0:space])## добавляем в список фамилию и имя через запятую 
                          ## фамилия: от большой буквы после пробела и до конца [space+1:]
                          ## имя с первого символа до пробела [0:space]
    return choice


def glavnaja(): 
    f = open('opilased.txt','r')    ## открываем файл на чтение
    opilased, proguly = spiski(f)
    n = len(opilased)
    f.close()                       ## закрываем файл
    print("Лучшие ученики - введите b")
    print("Возрастание прогулов - введите s")
    print("Список на комиссию - введите k")
    print("Удалить прогульщиков ( > 100) - введите d")
    print("Выводятся ученики, фамилии которых начинаются на заданную букву - m")
    print("--------------------------------------------------------------------")
    menu = input("Сделайте свой выбор ")
    if menu == 'b':
        proguly, opilased = sorteerimine(proguly,opilased,n)
        how_many = int(input("Сколько лучших учеников вывести? "))
        for i in range(how_many):
            print(opilased[i],"прогулял", str(proguly[i])+' раз')
    elif menu == 's':
        proguly, opilased = sorteerimine(proguly,opilased,n)
        for i in range(n):
            print(opilased[i],"прогулял", str(proguly[i])+' раз')
    elif menu == 'k':
        print("Выводятся ученики, у которых количество прогулов > 50, но < 100")
        print("Этим ученикам даётся шанс исправиться")
        komiss = komissija(proguly,opilased,n)
        for i in range(len(komiss)):
            print(komiss[i])
    elif menu == 'd':
        proguly,opilased = delete(proguly,opilased,n)
        print("Выгнали всех прогульщиков. Остались:")
        for i in range(len(proguly)):
            print(opilased[i]+' прогулял всего '+ str(proguly[i])+' раз')
    elif menu == 'm':
        bukva = input("Введите первую букву фамилии ")
        print("Выводятся ученики, фамилии которых начинаются на букву",bukva.capitalize())
        choice = my_choice(opilased,n,bukva)
        if len(choice) == 0:
            print("Таких тут нет!")
        for i in range(len(choice)):
            print(choice[i])
    else:
        print("Ошибка! Вы сделали неверный выбор!")
        


glavnaja()
    

