import random
def zp(cash1,vid_raboty1,all_works):   #zp = зп = зарплата
    if vid_raboty1 in works:
        if vid_raboty1=='курьер': #зарабатываем деньги, увеличиваем переменную фкц cash1/cash 
            cash1+=1000
            zarplata=1000
        elif vid_raboty1=='репетитор':
            cash1+=2000
            zarplata=2000
        elif vid_raboty1=='администратор в клубе':
            cash1+=1500
            zarplata=1500

        if vid_raboty1 in all_works: #добавляем в словарь все виды работ и кол-во смен
            all_works[vid_raboty1][0]+=1
            all_works[vid_raboty1][1]+=zarplata
        else:
            all_works[vid_raboty1]=[1,zarplata]
        return cash1
    else:
        print('Такого вида работы не существует, поробуйте ещё раз')
        return cash1
def ploschadki_s_tovarami(ploschadki):#каталог товаров на разных площадках
    for ploschadka in ploschadki:
        print(f'\n~~~~~~~~~~~~~~~{ploschadka}~~~~~~~~~~~~~~~')
        for item in ploschadki[ploschadka]:
            print(f'Цена товара {item}: {ploschadki[ploschadka][item]} руб.')
def otrabotannye_smeny(all_works):#вывод отработанных смен и заработанных денег
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Давайте посмотрим, как вы зарабатывали:')
    for work in all_works:
        print(f'На работе "{work}" Вы отработали {all_works[work][0]} смен и заработали {all_works[work][1]} руб.')
def bought(wanted,pokupki): #желанные и полученные покупки
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Далее Ваши пожелания в начале заработка:')
    for tovar in wanted:
        print(tovar)
    print('И то, что Вы смогли купить:')
    for tovar in pokupki:
        print(tovar)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
all_works=dict() #словарь всех видов работ и кол-во смен
works=('курьер','репетитор','администратор в клубе')
ploschadki={
    'WB':{'coat':5000,
          'palazzo':3500,
          'bodysuit':900,
          'chelsea':3000,
          'sweater':2500
        },
    'OZON':{'coat':5800,
          'palazzo':3000,
          'bodysuit':500,
          'chelsea':4000,
          'sweater':2000
        },
    'AliExpress':{'coat':1000,
          'palazzo':1000,
          'bodysuit':3000,
          'chelsea':10000,
          'sweater':1000
        },
    'GIRLIE ROOM':{'coat':6000,
          'palazzo':4000,
          'bodysuit':2000,
          'chelsea':5000,
          'sweater':3000
        },
    'Second-Hand':{'coat':2000,
          'palazzo':900,
          'bodysuit':200,
          'chelsea':2000,
          'sweater':1500
        }
}
with open("proektik_answers.txt", "w", encoding="utf-8") as file_out:
    print('Перед началом заработка Вы можете ознакомиться с каталогами разных площадок нашего города:')
    ploschadki_s_tovarami(ploschadki)
    print()
    wanted=input('Напишите, какую одежду Вы бы хотели купить через запятую с пробелом: ')
    file_out.write(wanted + '\n')
    wanted=wanted.split(', ')
    print('Это понадобится в будущем, чтобы Вы смогли проанализировать Ваши "хотелки" и совершенные покупки, если таковые будут.')
    print()
    cash=0
    print(f'На данный момент у Вас на счету: {cash} рублей')
    print('У вас недостаточно средств, чтобы приступить к покупкам.')
    print('Вы можете выбрать любой способ заработка: курьер (1000 руб. за смену), репетитор (2000 руб. за смену) или администратор в клубе (1500 руб. за смену)')
    print()
    while cash<10000:
        vid_raboty=input('Введите желаемый способ заработка: ')
        file_out.write(vid_raboty + '\n')
        cash=zp(cash,vid_raboty,all_works)
        if cash>=10000:
            print(f'Поздавляем! У Вас на счету: {cash} рублей.')
            break
        print(f'На данный момент у Вас на счету: {cash} рублей')
        print('У вас недостаточно средств, чтобы приступить к покупкам.')
        
    print('Вы можете приступить к покупке товаров!')
    print('К сожалению, товары быстро раскупают, поэтому вы можете выбрать все необходимые товары только на 1 из 5 площадок нашего города.')
    print('А также учитывайте, что времени мало, поэтому у Вас только 1 попытка сделать заказ: если Вы введёте товары, на которые у Вас не хватит денег, попытка будет аннулирована.')
    print('И в этот сезон Вы не сможете обновить гардероб.')
    print('Каталог товаров с ценами также присутствует:')
    ploschadki_s_tovarami(ploschadki)
    print()

    while True:
        want_to_buy=input('Хотите ли Вы обновить гардероб в этом сезоне? (Да/Нет): ')
        if want_to_buy=='Да' or want_to_buy=='Нет':
            file_out.write(want_to_buy + '\n')
            break
    if want_to_buy=='Да':
        while True:
            vybor_ploschadki=input('\nВыберите 1 площадку ("WB","OZON","AliExpress","GIRLIE ROOM","Second-Hand"): ')
            if vybor_ploschadki in ploschadki:
                file_out.write(vybor_ploschadki + '\n')
                break
            else:
                print('Такой площадки нет. Попробуйте ещё раз.')
        print(f'Ниже представлен каталог "{vybor_ploschadki}"')
        for item in ploschadki[vybor_ploschadki]: #выводим каталог выбр.площадки
            print(f'{item}: {ploschadki[vybor_ploschadki][item]} руб.')
        while True:
            pokupki=input('\nВведите через запятую с пробелом выбранные товары: ')#список покупок
            pokupki_1=pokupki
            pokupki=pokupki.split(', ')
            if all(i in ploschadki[vybor_ploschadki] for i in pokupki):
                file_out.write(pokupki_1 + '\n')
                break
            else:
                print('Этих товаров нет, Вы ввели неправильно название товаров или не через запятую с пробелом.\nПопробуйте ещё раз')
        summa=0
        for tovar in pokupki: #считаем стоимость товаров
                summa+=ploschadki[vybor_ploschadki][tovar]
        if summa<=cash: #проверяем, сможет ли оплатить: если нет, то без покупок остался, либо кредит
            cash=cash-summa
            print('Как Вы хотите забрать заказ: сами из магазина или доставкой? Предупреждаем, что при заказе доставкой может произойти ошибка, от нас не зависящая, и ваша заявка обнулится.')
            while True:
                how_to_get=input("Введите 'Самовывоз' или 'Доставка': ")
                if how_to_get=='Самовывоз' or how_to_get=='Доставка':
                    file_out.write(how_to_get + '\n')
                    break
            if how_to_get=='Доставка':
                site_sletel = random.randint(1, 10) #сайт слетел? 1-да
                if site_sletel==1:
                    print('К сожалению, сайт слетел из-за большого количества входящих заявок, и Ваш заказ не был обработан. Все товары уже раскупили.')
                    otrabotannye_smeny(all_works)#вывод отработанных смен
                    print('Встретимся в следующем сезоне!')
                    print('Конец.')#4 концовка
                else:
                    print(f'Покупки оплачены. Курьер привезёт Вам товар в тчение 1-2 дней. К оплате вышло {summa} руб. У Вас осталось на счету {cash} рублей.')
                    print('Поздравляем! Вы сумели оплатить себе новую одежду на собственные заработанные деньги. Заказ ')
                    otrabotannye_smeny(all_works)#вывод отработанных смен
                    bought(wanted,pokupki)
                    print('Встретимся в следующем сезоне!')
                    print('Конец.') #5 концовка
            else: #если самовывоз
                print(f'Покупки оплачены. Заказ сможете забрать в выбранном магазине, когда Вам придёт уведомление. К оплате вышло {summa} руб. У Вас осталось на счету {cash} рублей.')
                print('Поздравляем! Вы сумели оплатить себе новую одежду на собственные заработанные деньги.')
                otrabotannye_smeny(all_works)#вывод отработанных смен
                bought(wanted,pokupki)
                print('Встретимся в следующем сезоне!')
                print('Конец.') #6 концовка
        else:
            print(f'К сожалению, Вам не хватило {summa-cash} руб. для оплаты.')
            while True:
                want_credit=input('Вы можете купить одежду в кредит. Хотите ли оформить кредит (Да/Нет): ')
                if want_credit=='Да':
                    file_out.write(want_credit + '\n')
                    print(f'На Вас оформлен кредит в размере {summa-cash} руб., который Вы можете закрыть в течение 1 года. ')
                    print(f'Теперь покупки оплачены. К оплате вышло {summa} руб. У Вас осталось на счету 0 рублей.')
                    print('Поздравляем!')
                    otrabotannye_smeny(all_works)#вывод отработанных смен
                    bought(wanted,pokupki)
                    print('Конец.')#2 концовка
                    break
                elif want_credit=='Нет':
                    file_out.write(want_credit + '\n')
                    print('Ваших накопленных средств не хватило на оплату товаров и Вы не захотели брать кредит, поэтому Ваша заявка отклонена.')
                    otrabotannye_smeny(all_works)#вывод отработанных смен
                    print('Встретимся в следующем сезоне!')
                    print('Конец.')#3 концовка
                    break    
    else:
        print('В таком случае до встречи в следующем сезоне. Надеемся, что в следующий раз наш ассортимент заинтересует Вас!')
        otrabotannye_smeny(all_works)#вывод отработанных смен
        print('Встретимся в следующем сезоне!')
        print('Конец.')#1 концовка
