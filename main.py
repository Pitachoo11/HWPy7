# autor Sergey Mitroshin

command=0
while 1==1:
    print ('*************************************')
    print (' Текстовая база телефонов')
    print (' Нажмите: ')
    print ('1 Для ввода данных в базу')
    print ('2 Для поиска записи по фамилии')
    print ('3 Для конвертации базы в формат 1')
    print ('0 Для завершения программы')
    print ('*************************************')
    try:
        command =int(input())
        if command==1:
            print('1')
        elif command == 0:
            break
    except:
        print ('Повторите ввод')

    
