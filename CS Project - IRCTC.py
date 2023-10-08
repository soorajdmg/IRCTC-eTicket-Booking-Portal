import pickle, mysql.connector as msc, os, random
import time, string, tabulate, datetime as dt, csv


def trains():
    ans1 = 'y'
    while ans1 in ['y', 'Y']:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'ab')
        trains = {}
        trains['tname'] = input('Enter train name: ')
        trains['tno'] = int(input('Enter train no: '))
        trains['stations'] = []
        nos = int(input('Enter the number of stations: '))
        for i in range(1, nos + 1):
            n = input('Enter the station code: ')
            n = n.upper()
            (trains['stations']).append(n)
        t = {}
        for i in range(1, nos + 1):
            c = input('Enter the station timing: ')
            t.update({trains['stations'][i - 1]: c})
        trains['time'] = t
        pickle.dump(trains, fh)
        print('Record successfully created!')
        fh.close()
        ans1 = input('Do you want to add more trains? [Y/N]: ')


def traindisp():
    print('[1] DISPLAY ALL RECORDS\n[2] DISPLAY BY TRAIN NO\n[3] DISPLAY BY STATION')
    ch3 = int(input('Enter your choice: '))
    if ch3 == 1:
        print()
        f3 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
        found = 0
        try:
            while True:
                s2 = pickle.load(f3)
                print(s2)
                found = 1
        except EOFError:
            if found == 0:
                print('No records to display')
            f3.close()
    elif ch3 == 2:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
        no = int(input('Enter train no: '))
        print()
        try:
            while True:
                st = pickle.load(fh)
                if st['tno'] == no:
                    print(st)
                    fh.close()
                    break
        except EOFError:
            print('No such train found')
            fh.close()
    elif ch3 == 3:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
        scode = input('Enter the station code: ')
        scode = scode.upper()
        print()
        found = 0
        try:
            while True:
                st = pickle.load(fh)
                if scode in st['stations']:
                    print(st)
                    found = 1
        except EOFError:
            if found == 0:
                print('No such train found')
            fh.close()
    else:
        print('Invalid input (Type either)')


def tedit():
    ans2 = 'y'
    while ans2 in ['y', 'Y']:
        no = int(input('Enter the train no to edit: '))
        print()
        print('[1] Train name\n[2] Station code & timing')
        ch1 = int(input('Enter your choice: '))
        if ch1 == 1:
            fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
            f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat', 'wb')
            found = 0
            try:
                while True:
                    det = pickle.load(fh)
                    if det['tno'] != no:
                        pickle.dump(det, f1)
                    else:
                        det['tname'] = input('Enter the new train name: ')
                        found = 1
                        pickle.dump(det, f1)
                        print('Edited successfully')
            except EOFError:
                if found == 0:
                    print('No such train found')
                fh.close()
            f1.close()
            os.remove('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat')
            os.rename('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat',
                      'trains.dat')

        elif ch1 == 2:
            fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
            f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat', 'wb')
            nos = int(input('Enter the number of stations: '))
            found = 0
            try:
                while True:
                    st = pickle.load(fh)
                    if st['tno'] != no:
                        pickle.dump(st, f1)
                    else:
                        l = []
                        for i in range(1, nos + 1):
                            n = input('Enter the station code: ')
                            n = n.upper()
                            l.append(n)
                            st['stations'] = l
                        t = {}
                        for i in range(1, nos + 1):
                            found = 1
                            c = input('Enter the station timing: ')
                            t.update({st['stations'][i - 1]: c})
                        st['time'] = t
                        pickle.dump(st, f1)
                        print('Edited successfully!')
            except EOFError:
                if found == 0:
                    print('No such train found!')
                fh.close()
                f1.close()
                os.remove('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat')
                os.rename('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat',
                          'D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat')
        ans2 = input('Do you want to edit more trains? [Y/N]: ')


def tdelete():
    ans2 = 'y'
    while ans2 in ['y', 'Y']:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
        f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat', 'ab')
        no = int(input('Enter the train no to delete: '))
        found = 0
        try:
            while True:
                det = pickle.load(fh)
                if det['tno'] != no:
                    pickle.dump(det, f1)
                else:
                    found = 1
                    fh.close()
                    f1.close()
                    os.remove('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat')
                    os.rename('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat',
                              'trains.dat')
                    print('Deleted successfully')
                    break
        except EOFError:
            if found == 0:
                print('No such train found')
        ans2 = input('Do you want to delete more trains? [Y/N]: ')


station = {}


def stations():
    global stations
    f2 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'ab')
    nos = int(input('Enter the number of stations to add: '))
    print()
    for i in range(1, nos + 1):
        n = input('Enter the station name: ')
        n = n.lower()
        n = n.capitalize()
        station['sname'] = n
        c = input('Enter the station code: ')
        c = c.upper()
        station['scode'] = c
        print('[1] TOWARDS NORTH\n[2] TOWARDS SOUTH')
        dir = int(input('Choose the direction: '))
        if dir == 1:
            station['direction'] = 'North'
        elif dir == 2:
            station['direction'] = 'South'
        else:
            print('Invalid input (Type either 1 or 2)')
        pickle.dump(station, f2)
    f2.close()
    return station


def stationdisp():
    print('[1] DISPLAY ALL STATIONS\n[2] DISPLAY BY CODE\n[3] DISPLAY BY DIRECTION')
    ch3 = int(input('Enter your choice: '))
    print()
    if ch3 == 1:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
        found = 0
        try:
            while True:
                st = pickle.load(fh)
                print(st)
                found = 1
        except EOFError:
            if found == 0:
                print('No records found')
            fh.close()
    elif ch3 == 2:
        print()
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
        no = input('Enter the station code: ')
        print()
        no = no.upper()
        found = 0
        try:
            while True:
                st = pickle.load(fh)
                if st['scode'] == no:
                    print(st)
                    found = 1
        except EOFError:
            if found == 0:
                print('No such stations found')
            fh.close()
    elif ch3 == 3:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
        dir = int(input('[1] South\n[2] North\nEnter your choice: '))
        print()
        found = 0
        if dir not in [1, 2]:
            print('Invalid input (Type either 1 or 2)')
        try:
            while True:
                st = pickle.load(fh)
                if st['direction'] == 'South' and dir == 1:
                    print(st)
                    found = 1
                elif st['direction'] == 'North' and dir == 2:
                    print(st)
                    found = 1
                else:
                    pass
        except EOFError:
            if found == 0:
                print('No such stations found')
            fh.close()
    else:
        print('Invalid input (Type either 1, 2 or 3)')


def sedit():
    ans3 = 'y'
    while ans3 in ['y', 'Y']:
        no = input('Enter the station code to edit: ')
        no = no.upper()
        print()
        print('[1] Station name\n[2] Station direction')
        ch1 = int(input('Enter your choice: '))
        if ch1 == 1:
            fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
            f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat', 'wb')
            found = 0
            try:
                while True:
                    det = pickle.load(fh)
                    if det['scode'] != no:
                        pickle.dump(det, f1)
                    else:
                        a = input('Enter the new station name: ')
                        a = a.lower()
                        a = a.capitalize()
                        det['sname'] = a
                        found = 1
                        pickle.dump(det, f1)
                        print('Edited successfully')
            except EOFError:
                if found == 0:
                    print('No such station found')
                fh.close()
            f1.close()
            os.remove('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat')
            os.rename('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat',
                      'stations.dat')

        elif ch1 == 2:
            fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
            f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat', 'wb')
            print('[1] TOWARDS NORTH\n[2] TOWARDS SOUTH')
            ch = int(input('Enter your journey direction: '))
            found = 0
            try:
                while True:
                    st = pickle.load(fh)
                    if st['scode'] != no:
                        pickle.dump(st, f1)
                    else:
                        if ch == 1:
                            st['direction'] = 'North'
                        elif ch == 2:
                            st['direction'] = 'South'
                        else:
                            print('Invalid input (Type either 1 or 2)')
                        pickle.dump(st, f1)
                        print('Edited successfully!')
            except EOFError:
                if found == 0:
                    print('No such station found!')
            fh.close()
            f1.close()
            os.remove('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat')
            os.rename('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat',
                      'D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat')
        ans3 = input('Do you want to edit more stations? [Y/N]: ')


def sdelete():
    ans2 = 'y'
    while ans2 in ['y', 'Y']:
        fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
        f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat', 'ab')
        no = input('Enter the station code to delete: ')
        no = no.upper()
        found = 0
        try:
            while True:
                det = pickle.load(fh)
                if det['scode'] != no:
                    pickle.dump(det, f1)
                else:
                    found = 1
                    fh.close()
                    f1.close()
                    os.remove('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat')
                    os.rename('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\temp.dat',
                              'stations.dat')
                    print('Station deleted successfully')
                    break
        except EOFError:
            if found == 0:
                print('No such station found')
        ans2 = input('Do you want to delete more stations? [Y/N]: ')


def ftm(pos, lst):
    if pos == 1:
        FHT = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ftime.dat', 'rb')
        temp = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\temp.dat', 'ab')
        global FTime
        try:
            FTime = pickle.load(FHT)
        except EOFError:
            pass
        if lst[1] == 1:
            FTime[lst[0]] = [0, 24]
        elif lst[1] == 2:
            FTime[lst[0]] = [6, 7, 8, 9, 10, 11]
        elif lst[1] == 3:
            FTime[lst[0]] = [13, 14, 15]
        elif lst[1] == 4:
            FTime[lst[0]] = [16, 17, 18, 19, 20]
        else:
            FTime[lst[0]] = [20, 21, 22, 23]
        pickle.dump(FTime, temp)
        FHT.close()
        temp.close()
        os.remove(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ftime.dat')
        os.rename(r'D:\Users\Sooraj\PycharmProjects\CS Project\temp.dat',
                  r'D:\Users\Sooraj\PycharmProjects\CS Project\Ftime.dat')
    else:
        FHT = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ftime.dat', 'rb')
        global Fime
        l = []
        try:
            Fime = pickle.load(FHT)
        except EOFError:
            pass
        for i in Fime:
            if (int(lst) in Fime[i]) or 0 in Fime[i]:
                l.append(i)
        return l


def catering():
    ans = 'y'
    while ans in ['y', "Y", 'Yes']:
        print('[1] Show food menu\n[2] Edit')
        print()
        f = input('Select any one of the above choices: ')
        print()
        if f == '1':
            FI = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
            rdr = csv.reader(FI)
            print(tabulate.tabulate(rdr, headers='firstrow', tablefmt='github'))
            print('' * 2, sep='\n')
            FI.close()
        elif f == '2':
            ans1 = 'y'
            while ans1 in ['y', "Y", 'Yes']:
                print('[1] Add food\n[2] Change cost\n[3] Change time\n[4] Stock food supplies')
                print()
                f1 = input('Select any one of the above choices')
                print()
                if f1 == '1':
                    Add = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'a', newline='')
                    ct = csv.writer(Add)
                    vrf = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r', )
                    r = csv.reader(vrf)
                    lst = []
                    for i in r:
                        lst.append(i)
                    ind = int((lst[-1][0])) + 1
                    name = input('Enter name of the food')
                    cost = eval(input('Enter cost of the food'))
                    print('Enter time for this item')
                    print()
                    print('[Available hours are]:\n', '=' * 21,
                          '\n|1. All working hours.|\n|2.  06-11 AM         |\n|3.  01-03 PM         |\n|4.  04-08 PM         |\n|5.  08-11 PM         |\n',
                          '=' * 21)
                    n = 1
                    while n == 1:
                        n = 0
                        t = input('Select any one of the above')
                    if t == 1:
                        tim = 'All working hours.'
                    elif t == '2':
                        tim = '6-11 PM'
                    elif t == '3':
                        tim = '1-3 PM'
                    elif t == '4':
                        tim = '4-8 PM'
                    elif t == '5':
                        tim = '8-11 PM'
                    else:
                        print('Please enter a valid choice')
                        n = 1
                    qnty = int(input('Enter available quantity of the item'))
                    row = [ind, name, cost, tim, qnty]
                    ct.writerow(row)
                    ftm(1, [ind, t])
                    print()
                    print(name, 'has been added to the menu successfully\n')
                    Add.close()
                    vrf.close()
                elif f1 == '2':
                    vrf = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
                    tmp = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv', 'w', newline='')
                    r = csv.reader(vrf)
                    w = csv.writer(tmp)
                    ind = int(input("Enter index number of the food you'd like to change the cost of: "))
                    cst = int(input('Enter new cost of the food'))
                    lst = []
                    t = 0
                    for i in r:
                        lst.append(i)
                    for i in lst:
                        if i[0] == str(ind):
                            i[2] = cst
                            t = 1
                    if t == 1:
                        w.writerows(lst)
                        vrf.close()
                        tmp.close()
                        os.remove(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                        os.rename(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv',
                                  r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                    else:
                        print('No such food exist in the menu\n')
                    vrf.close()
                    tmp.close()

                elif f1 == '3':
                    ind = int(input("Enter index number of the food you'd like to change the time of: "))
                    trf = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
                    tmp = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv', 'w', newline='')
                    r = csv.reader(trf)
                    w = csv.writer(tmp)
                    print()
                    print('[Available hours are]:\n', '=' * 21,
                          '\n|1. All working hours.|\n|2.  06-11 AM         |\n|3.  01-03 PM         |\n|4.  04-08 PM         |\n|5.  08-11 PM         |\n',
                          '=' * 21)
                    print()
                    n = 1
                    tim = ''
                    while n == 1:
                        n = 0
                        t = input('Select any one of the above')
                    if t == '1':
                        tim = 'All working hours.'
                    elif t == '2':
                        tim = '6-11 PM'
                    elif t == '3':
                        tim = '1-3 PM'
                    elif t == '4':
                        tim = '4-8 PM'
                    elif t == '5':
                        tim = '8-11 PM'
                    else:
                        print('Please enter a valid choice')
                        n = 1
                    lst = []
                    t1 = 0
                    for i in r:
                        lst.append(i)
                    for i in lst:
                        if i[0] == str(ind):
                            i[3] = tim
                            t1 = 1
                    if t1 == 1:
                        ftm(1, [ind, int(t)])
                        w.writerows(lst)
                        trf.close()
                        tmp.close()
                        os.remove(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                        os.rename(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv',
                                  r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                        print('Updated\n')
                    else:
                        print('No such food exist in the menu\n')
                    trf.close()
                    tmp.close()
                elif f1 == '4':
                    vrf = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
                    tmp = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv', 'w', newline='')
                    r = csv.reader(vrf)
                    w = csv.writer(tmp)
                    ind = int(input("Enter index number of the food you'd like to stock up: "))
                    st = int(input('Enter amount of item to restock'))
                    lst = []
                    t = 0
                    for i in r:
                        lst.append(i)
                    for i in lst:
                        if i[0] == str(ind):
                            ad = int(i[4]) + st
                            i[4] = ad
                            t = 1
                    if t == 1:
                        w.writerows(lst)
                        vrf.close()
                        tmp.close()
                        os.remove(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                        os.rename(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv',
                                  r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                        print('Updated\n')
                    else:
                        print('No such food exist in the menu\n')
                    vrf.close()
                    tmp.close()
                else:
                    print("Invalid input, Try again.")
                ans1 = input('Edit again?[Y/N]\n')
        else:
            print('Invalid input,please try again')
        print()
        ans = input('Do you want to continue in food menu? [Y/N]:')


def order():
    print('+', '_' * 100, '+', sep='')
    print('' * 2, sep='\n')
    print('+', '*' * 49, '+', sep='')
    print("|\t\t|||TODAY'S MENU|||", '\t          |')
    print('+', '*' * 49, '+', sep='')
    ans = 'y'
    while ans in ['y', "Y", 'Yes']:
        print("\n[1] ORDER\n[2] DISPLAY THE WHOLE MENU\n[3] FOODS AVAILABLE AT THIS HOUR")
        F = input('Select one: ')
        if F == '1':
            t = 0
            rst = []
            ast = []
            ans = 'y'
            p = 0
            Ctime = time.strftime("%H")
            ind = ftm(2, Ctime)
            while ans in ['y', "Y"]:
                RED = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
                tmp = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv', 'w', newline='')
                r = csv.reader(RED)
                w = csv.writer(tmp)
                lst = []
                for i in r:
                    lst.append(i)
                Ord = int(input("Enter index number of the food you'd like to order: "))
                for i in lst:
                    if i[0] == str(Ord):
                        p = 1
                        if Ord in ind:
                            am = int(input('Enter amount of item to buy: '))
                            if am <= int(i[4]):
                                rst.append(Ord)
                                ast.append(am)
                                r = int(i[4]) - am
                                i[4] = r
                                t = 1
                            else:
                                print('\nSorry, amount of item defficient\n')
                            if t == 1:
                                w.writerows(lst)
                                RED.close()
                                tmp.close()
                                os.remove(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                                os.rename(r'D:\Users\Sooraj\PycharmProjects\CS Project\Ctemp.csv',
                                          r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv')
                        else:
                            print('\nFood not available at this hour\n')
                if p == 0:
                    print('\nNo such food exist in the menu\n')
                ans = input('Would you like to order another item? [Y/N]:')
            if t == 1:
                print('\nProcessing food', end='')
                for i in range(3):
                    print('.', end='')
                    time.sleep(0.5)
                    print(end='')
                print()
                print('Ordered successfully\n')
                rec = input('Would you like the receipt of the item? [Y/N]:')
                sm = 0
                qn = 0
                if rec in ['y', 'Y']:
                    fd = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
                    r = csv.reader(fd)
                    rpt = []
                    hd = ['Item', 'Qty', 'Price']
                    for i in r:
                        for j in rst:
                            if i[0] == str(j):
                                am = ast[rst.index(j)]
                                cst = am * int(i[2])
                                qn += am
                                sm += cst
                                rpt.append([i[1], am, cst])
                    print()
                    print('_' * 30)
                    print()
                    print('Thanks for ordering our food!')
                    print('_' * 30)
                    print('Bill no:', ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                    e = dt.datetime.now()
                    print('Date:', e.strftime("%Y-%m-%d %H:%M:%S"))
                    print('-' * 30)
                    print(tabulate.tabulate(rpt, headers=hd, stralign='right'))
                    print('-' * 30)
                    print('Total:', ' ' * 11, sm)
                    print('-' * 30)
                    print('\nWe wish you a safe journey!')
                    print('_' * 30)

            RED.close()
            tmp.close()

        elif F == '2':
            FI = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
            rdr = csv.reader(FI)
            print(tabulate.tabulate(rdr, headers='firstrow', tablefmt='fancy_grid'))
            print('' * 2, sep='\n')
            FI.close()
        elif F == '3':
            FI = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\FoodInfo.csv', 'r')
            Ctime = time.strftime("%H")
            rdr = csv.reader(FI)
            ind = ftm(2, Ctime)
            av = []
            pr = ['Index', '', '------', ]
            ind += pr
            nl = ['', '', '', '', '']
            for i in rdr:
                if i[0] in ind or int(i[0]) in ind:
                    av.append(i)
            # av=['-'*6,'-'*15,'-'*6,'Not Available At This Hour','-'*13]
            print(tabulate.tabulate(av, headers='firstrow', tablefmt='fancy_grid'))
            FI.close()
        else:
            print('Invalid input,Try again\n')
        ans = input('Want to select again?[Y/N]')
    print()


def tickets():
    print('[1] TOWARDS NORTH\n[2] TOWARDS SOUTH')
    ch = int(input('Enter your journey direction: '))
    print()
    f1 = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\trains.dat', 'rb')
    fh = open(r'D:\Users\Sooraj\PycharmProjects\CS Project\stations.dat', 'rb')
    print('STATION CODE            STATION NAME ')
    print('-' * 102)
    if ch == 1:
        found = 0
        try:
            while True:
                s = pickle.load(fh)
                n1 = 20 - len(s['scode'])
                if s['direction'] == 'North':
                    print('[', s['scode'], ']' + (' ' * n1) + s['sname'])
                    print('-' * 102)
                    found = 1

        except EOFError:
            if found == 0:
                print('No stations towards the North direction')
    elif ch == 2:
        found = 0
        try:
            while True:
                s = pickle.load(fh)
                n1 = 20 - len(s['scode'])
                if s['direction'] == 'South':
                    print('[', s['scode'], ']' + (' ' * n1) + s['sname'])
                    print('-' * 102)
                    found = 1

        except EOFError:
            if found == 0:
                print('No stations towards the South direction')
    fh.close()

    dest = input('Enter the station code: ')
    dest = dest.upper()
    found = 0
    print()
    print('TRAIN NO' + ' ' * 6 + 'AVAILABLE TRAINS' + ' ' * 24 + 'ARRIVAL')
    print('-' * 102)
    try:
        while True:
            s = pickle.load(f1)
            a = s['tno']
            n1 = 10 - len(str(s['tno']))
            n2 = 40 - len(s['tname'])
            if dest in s['stations']:
                print('[', a, ']' + ' ' * n1 + s['tname'] + ' ' * n2 + s['time'][dest])
                print('-' * 102)
                found = 1
    except EOFError:
        if found == 0:
            print('No trains to the specified station')
        print()
        f1.close()

    pnr = random.randrange(1, 10)
    pnr = str(pnr)
    for i in range(9):
        p = str(random.randrange(10))
        pnr += p
    pnr = int(pnr)
    tno = int(input('Enter the train no to book: '))
    f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
    f2 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
    try:
        while True:
            st = pickle.load(f1)
            if st['tno'] == tno:
                tname = st['tname']
                for i in st['stations']:
                    if i == dest:
                        dtime = st['time'][i]
                        pass
                break
    except EOFError:
        pass
    try:
        while True:
            st = pickle.load(f2)
            if st['scode'] == dest:
                dname = st['sname']
                break
    except EOFError:
        f1.close()
        f2.close()

    pnr = random.randrange(1, 10)
    pnr = str(pnr)
    for i in range(9):
        p = str(random.randrange(10))
        pnr += p
    pnr = int(pnr)
    f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
    f2 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
    try:
        while True:
            st = pickle.load(f1)
            if st['tno'] == tno:
                tname = st['tname']
                for i in st['stations']:
                    if i == dest:
                        dtime = st['time'][i]
                        pass
                break
    except EOFError:
        pass
    try:
        while True:
            st = pickle.load(f2)
            if st['scode'] == dest:
                dname = st['sname']
                break
    except EOFError:
        pass
    name = input('Enter your name: ')
    seats = int(input('Enter the no of seats: '))
    f = msc.connect(host='localhost', user='root', passwd='lekk', database='sooraj')
    cx = input('Do you want to order food? [Y/N]: ')
    if cx in ['y', 'Y']:
        order()
        insquery = "insert into tickets values(%s,%s,'%s','%s',%s,'%s','%s','%s')" % (
            pnr, tno, tname, name, seats, dest, dtime, 'YES')

    else:
        insquery = "insert into tickets values(%s,%s,'%s','%s',%s,'%s','%s','%s')" % (
            pnr, tno, tname, name, seats, dest, dtime, 'NO')
    cu = f.cursor()
    cu.execute(insquery)
    f.commit()
    print('Processing ticket', end='')
    for i in range(5):
        print('.', end='')
        time.sleep(0.5)
        print(end='')
    print()
    print()
    print('-' * 48 + 'TICKET' + '-' * 48)
    n1 = 67 - len(name)
    n2 = 55 - (len(tname) + len(str(tno)))
    n3 = 61 - len(dname)
    if cx in ['y', 'Y']:
        print('Name:', name, ' ' * n1 + 'No of seats:', seats,
              '\nTrain details:', tno, '-', tname, ' ' * n2 + 'PNR No:', pnr,
              '\nDestination:', dname + ' ' * n3 + 'Reach by:', dtime,
              '\nCatering status: YES')
    else:
        print('Name:', name, ' ' * n1 + 'No of seats:', seats,
              '\nTrain details:', tno, '-', tname, ' ' * n2 + 'PNR No:', pnr,
              '\nDestination:', dname + ' ' * n3 + 'Reach by:', dtime,
              '\nCatering status: NO')
    print('-' * 102)
    print()


def ticketdatadisp():
    print('[1] DISPLAY ALL RECORDS\n[2] DISPLAY BY PNR NO.')
    ch2 = int(input('Enter your choice: '))
    if ch2 == 1:
        fh = msc.connect(host='localhost', user='root', passwd='lekk', database='sooraj')
        cu = fh.cursor()
        cu.execute('select * from tickets')
        tu = cu.fetchall()
        print('\n(PNR, TRAIN NO, TRAIN NAME, PASSENGER NAME, NO. OF SEATS, DEST, DEST. TIME)')
        for i in tu:
            print(i)
        fh.close()
    elif ch2 == 2:
        no = int(input('Enter the PNR no: '))
        fh = msc.connect(host='localhost', user='root', passwd='lekk', database='sooraj')
        cu = fh.cursor()
        cu.execute('select * from tickets where pnr=%s' % (no,))
        tu = cu.fetchall()
        print()
        if tu == []:
            print('Invalid PNR entered')
        else:
            print('(PNR, TRAIN NO, TRAIN NAME, PASSENGER NAME, NO. OF SEATS, DEST, DEST. TIME)')
            for i in tu:
                print(i)
    else:
        print('Invalid input (Type either 1 or 2)')


print('SOUTHERN RAILWAY WELCOMES YOU!')
ans = 'y'
while ans == 'y' or ans == 'Y':
    print()
    print('[1] USER\n[2] DEVELOPER')
    log = int(input('Enter your choice: '))
    print()

    # user mode
    if log == 1:
        print('[1] BOOK TICKETS\n[2] CANCEL TICKET\n[3] PNR ENQUIRY\n[4] LOCATE A TRAIN')
        c = int(input('Enter your objective: '))
        print()
        if c == 1:
            tickets()

        elif c == 2:
            no = int(input('Enter the PNR to cancel ticket: '))
            fh = msc.connect(host='localhost', user='root', passwd='lekk', database='sooraj')
            cu = fh.cursor()
            cu.execute('select * from tickets')
            tu = cu.fetchall()
            found = 0
            for i in tu:
                if i[0] == no:
                    cu.execute('Delete from tickets where pnr=%s' % (no,))
                    print()
                    print('-' * 48 + 'TICKET' + '-' * 48)
                    n1 = 67 - len(i[3])
                    n2 = 55 - (len(i[2]) + len(str(i[1])))
                    n3 = 61 - len(i[-2])
                    print('Name:', i[3], ' ' * n1 + 'No of seats:', i[4],
                          '\nTrain details:', i[1], '-', i[2], ' ' * n2 + 'PNR No:', i[0],
                          '\nDestination:', i[-2] + ' ' * n3 + 'Reach by:', i[-1])
                    print('-' * 102)
                    print()
                    cross_check = input('Do you want to cancel this ticket? [Y/N]: ')
                    if cross_check == 'y' or cross_check == 'Y':
                        fh.commit()
                        print('\nTicket cancelled successfully')
                    found = 1
                    break
            else:
                print('\nInvalid PNR entered')
            fh.close()
            print()

        elif c == 3:
            no = int(input('Enter your PNR: '))
            fh = msc.connect(host='localhost', user='root', passwd='lekk', database='sooraj')
            cu = fh.cursor()
            cu.execute('select * from tickets')
            tu = cu.fetchall()
            found = 0
            for i in tu:
                if i[0] == no:
                    print()
                    print('-' * 46 + 'PNR STATUS' + '-' * 46)
                    n1 = 67 - len(i[3])
                    n2 = 55 - (len(i[2]) + len(str(i[1])))
                    n3 = 27 - len(i[-2])
                    print('Name:', i[3], ' ' * n1 + 'No of seats:', i[4],
                          '\nTrain details:', i[1], '-', i[2], ' ' * n2 + 'PNR No:', i[0],
                          '\nDestination:', i[-3] + ' ' * n3 + 'Reach by:', i[-2] + ' ' * (n3 - 1) + 'Catering status:',
                          i[-1])
                    print('-' * 102)
                    print()
                    found = 1
            if found == 0:
                print('Invalid PNR entered')

        elif c == 4:
            no = int(input('Enter the train no: '))
            fh = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\trains.dat', 'rb')
            f1 = open('D:\\Users\\Sooraj\\PycharmProjects\\CS Project\\stations.dat', 'rb')
            try:
                while True:
                    st = pickle.load(fh)
                    s1 = pickle.load(f1)
                    if st['tno'] == no:
                        cdt = dt.datetime.now()
                        ct = cdt.strftime('%H:%M')
                        found = 0
                        index = 0
                        k = 10000
                        for i in st['stations']:
                            try:
                                if st['time'][i] == ct:
                                    print()
                                    n1 = 54 - (len(str(st['tno'])) + len(st['tname']))
                                    n2 = 59 - len((st['stations'][index + 1]))
                                    n3 = 60 - len(st['stations'][-1])
                                    print('Train details:', st['tno'], '/', st['tname'],
                                          ' ' * n1 + 'Current status: ' + 'Reached the station ' + i +
                                          '\nNext station:', (st['stations'][index + 1]) + ' ' * n2 + 'Reach by:',
                                          st['time'][st['stations'][index + 1]] +
                                          '\nDestination:', st['stations'][-1] + ' ' * n3 + 'Reach by:',
                                          st['time'][st['stations'][-1]])
                                    print()
                                    found = 1
                                    break

                                elif st['time'][i] < ct and st['time'][st['stations'][index + 1]] > ct:
                                    print()
                                    n1 = 54 - (len(str(st['tno'])) + len(st['tname']))
                                    n2 = 59 - len((st['stations'][index + 1]))
                                    n3 = 60 - len(st['stations'][-1])
                                    print('Train details:', st['tno'], '/', st['tname'],
                                          ' ' * n1 + 'Current status: ' + 'Left the station ' + i +
                                          '\nNext station:', (st['stations'][index + 1]) + ' ' * n2 + 'Reach by:',
                                          st['time'][st['stations'][index + 1]] +
                                          '\nDestination:', st['stations'][-1] + ' ' * n3 + 'Reach by:',
                                          st['time'][st['stations'][-1]])
                                    print()
                                    found = 1
                                    break

                                elif st['time'][st['stations'][0]] > ct:
                                    print()
                                    n1 = 54 - (len(str(st['tno'])) + len(st['tname']))
                                    n2 = 59 - len((st['stations'][index + 1]))
                                    n3 = 60 - len(st['stations'][-1])
                                    print('Train details:', st['tno'], '/', st['tname'],
                                          ' ' * n1 + 'Current status: ' + 'Yet to depart from its origin station ' +
                                          st['stations'][0] +
                                          '\nNext station:', (st['stations'][1]) + ' ' * n2 + 'Reach by:',
                                          st['time'][st['stations'][1]] +
                                          '\nDestination:', st['stations'][-1] + ' ' * n3 + 'Reach by:',
                                          st['time'][st['stations'][-1]])
                                    print()
                                    found = 1
                                    break

                                elif st['time'][st['stations'][-1]] <= ct:
                                    print()
                                    n1 = 54 - (len(str(st['tno'])) + len(st['tname']))
                                    n2 = 54 - len((st['stations'][index + 1]))
                                    n3 = 60 - len(st['stations'][-1])
                                    print('Train details:', st['tno'], '/', st['tname'],
                                          ' ' * n1 + 'Current status: ' + 'Reached its destination ' + st['stations'][
                                              -1] +
                                          '\nNext station:', '---------' + ' ' * n2 + 'Reach by:',
                                          '--:--' +
                                          '\nDestination:', st['stations'][-1] + ' ' * n3 + 'Reach by:',
                                          st['time'][st['stations'][-1]])
                                    print()
                                    found = 1
                                    break

                                elif st['time'][st['stations'][index + 1]] > ct:
                                    ind = 0
                                    ct1 = ct.replace(':', '')
                                    t = st['time'][st['stations'][index]]
                                    t = t.replace(':', '')
                                    k1 = int(t) - int(ct1)
                                    for i in st['stations']:
                                        if k1 < k:
                                            k = k1
                                            ps = i
                                            ind += 1
                                    found = 2
                                if found == 2:
                                    print()
                                    n1 = 54 - (len(str(st['tno'])) + len(st['tname']))
                                    n2 = 59 - len((st['stations'][ind + 1]))
                                    n3 = 60 - len(st['stations'][-1])
                                    print('Train details:', st['tno'], '/', st['tname'],
                                          ' ' * n1 + 'Current status: ' + 'Left the station ' + i +
                                          '\nNext station:', (st['stations'][ind + 1]) + ' ' * n2 + 'Reach by:',
                                          st['time'][st['stations'][ind + 1]] +
                                          '\nDestination:', st['stations'][-1] + ' ' * n3 + 'Reach by:',
                                          st['time'][st['stations'][-1]])
                                    print()
                                    break
                                index += 1


                            except IndexError:
                                pass
                        if found == 0:
                            print('Data is being updated\n')

                        break
            except EOFError:
                print('No such train found')

        else:
            print('Invalid input (Type either 1, 2, 3 or 4)')


    # developer mode / pass=1000
    elif log == 2:
        password = int(input('Enter password: '))
        if password == 1000:
            ans1 = 'y'
            while ans1 in ['y', 'Y']:
                print()
                print('[1] TRAINS\n[2] STATIONS\n[3] TICKET DATA\n[4] FOOD ITEMS')
                ch1 = int(input('Enter your choice: '))
                print()
                if ch1 == 1:
                    print('[1] ADD TRAINS\n[2] EDIT TRAINS\n[3] DISPLAY RECORDS\n[4] DELETE TRAINS')
                    ch2 = int(input('Enter your choice: '))
                    print()
                    if ch2 == 1:
                        trains()
                    elif ch2 == 2:
                        tedit()
                    elif ch2 == 3:
                        traindisp()
                    elif ch2 == 4:
                        tdelete()
                    else:
                        print('Invalid input (Type either 1, 2, 3 or 4)')
                elif ch1 == 2:
                    print('[1] ADD STATIONS\n[2] EDIT STATIONS\n[3] DISPLAY RECORDS\n[4] DELETE STATIONS')
                    ch4 = int(input('Enter your choice: '))
                    print()
                    if ch4 == 1:
                        stations()
                    elif ch4 == 2:
                        sedit()
                    elif ch4 == 3:
                        stationdisp()
                    elif ch4 == 4:
                        sdelete()
                    else:
                        print('Invalid input (Type either 1, 2, 3 or 4)')

                elif ch1 == 3:
                    ticketdatadisp()
                elif ch1 == 4:
                    catering()
                else:
                    print('Invalid input (Type either 1, 2, 3 or 4)')
                print()
                ans1 = input('Do you want to continue in DEV mode [Y/N]: ')
        else:
            print('Incorrect password')

    else:
        print('Invalid input (Type either 1 or 2)')

    ans = input('Do you want to continue in menu? [Y/N]: ')
    print()

print('Thankyou for using this eTicket Booking Portal!')
