import csv
import loclale
from csv import DictWriter

name: str = 'Пётр' #input('Введите имя кандидата:')
mid_name: str = 'Иванович' #input('Введите отчество кандидата:')
surname: str = 'Сергеев' #input('Введите фамилию кандидата:')
email: str = 'pis@test.ru' #input ('Введите e-mail кандидата:')
registration: int = int(input ('Выберите вариант трудоустройства: 1) Штат 2) Договор ГПХ 3) Договор ИП: '))
salary: float = float(input('Введите сумму "на руки" о которой договорились с кандидатом:'))
s_taxes: float = float((salary/0.87)*1.072)
start_date = input('Введите дату выхода сотрудника:')
if salary == 20000.00:
    position = '"Специалист по контролю качества 3 категории"'
else: print ('ВВЕДИТЕ ВРУЧНУЮ')

with open("jofferdb.csv", mode='w') as csvfile:
    fieldnames = ['name', 'email', 'registration']
    writer: DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'name': name, 'email': email, 'registration' : registration})

print (email)
print ('Добрый день, ', name,' ', mid_name,'!', sep='')
print('Мы рады предложить Вам позицию ', position,'.', sep='')
print('Обязанности:')
if position == '"Специалист по контролю качества 3 категории"':
    print('Тестирование web приложений', 'Разработка тестовой документации', sep="\n")
else: print('ВВЕДИТЕ ВРУЧНУЮ')
print('Условия:')
print('Работа  с 10:00 до 19:00 (понедельник - пятница) по Московскому времени', 'Разработка тестовой документации', sep='\n')
print('Заработная плата:',salary,' рублей на руки (', s_taxes,' рублей с НДФЛ и соц.взносами)')
print('Сотрудничество –  трудоустройство в штат','Отпуск 28 дней в году','Испытательный срок 3 месяца','Выходные и праздники согласно трудовому календарю РФ',sep='\n')
print('Ваш первый рабочий день - ',start_date,'.',end=' ')
print('Пожалуйста, подтвердите ваше согласие с предложенными условиями. Наше предложение действительно в течении одного рабочего дня.')




