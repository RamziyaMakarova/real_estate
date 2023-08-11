import pandas as pd
import matplotlib as plt
import pandas_profiling as pp
#df = pd.read_csv('/home/ramziya/FLATS/_data.csv')
#profile = pp.ProfileReport(df)
#profile.to_file("output_file.html")

flats = pd.read_csv('/home/ramziya/FLATS/flats_copy.csv')
flats['Метро'] = flats['Метро'].astype('str')
def assign_weight(row):
    if 'Александровский сад' in row['Метро']:
        return 1
    if 'Арбатская' in row['Метро']:
        return 2
    if 'Библиотека им. Ленина' in row['Метро']:
        return 3
    if 'Боровицкая' in row['Метро']:
        return 4
    if 'Кропоткинская' in row['Метро']:
        return 5
    if 'Охотный ряд' in row['Метро']:
        return 6
    if 'Площадь Революции' in row['Метро']:
        return 7
    if 'Театральная' in row['Метро']:
        return 8
    if 'Пушкинская' in row['Метро']:
        return 9
    if 'Тверская' in row['Метро']:
        return 10
    if 'Чеховская' in row['Метро']:
        return 11
    if 'Маяковская' in row['Метро']:
        return 12
    if 'Парк Культуры' in row['Метро']:
        return 13
    if 'Кузнецкий мост' in row['Метро']:
        return 14
    if 'Лубянка' in row['Метро']:
        return 15
    if 'Смоленская' in row['Метро']:
        return 16
    if 'Китай-город' in row['Метро']:
        return 17
    if 'Новокузнецкая' in row['Метро']:
        return 18
    if 'Третьяковская' in row['Метро']:
        return 19
    if 'Полянка' in row['Метро']:
        return 20
    if 'Белорусская' in row['Метро']:
        return 21
    if 'Трубная' in row['Метро']:
        return 22
    if 'Цветной бульвар' in row['Метро']:
        return 23
    if 'Сухаревская' in row['Метро']:
        return 24
    if 'Сретенский бульвар' in row['Метро']:
        return 25
    if 'Тургеневская' in row['Метро']:
        return 26
    if 'Чистые пруды' in row['Метро']:
        return 27
    if 'Октябрьская' in row['Метро']:
        return 28
    if 'Киевская' in row['Метро']:
        return 29
    if 'Баррикадная' in row['Метро']:
        return 30
    if 'Краснопресненская' in row['Метро']:
        return 31
    if 'Добрынинская' in row['Метро']:
        return 32
    if 'Серпуховская' in row['Метро']:
        return 33
    if 'Красные ворота' in row['Метро']:
        return 34
    if 'Курская' in row['Метро']:
        return 35
    if 'Чкаловская' in row['Метро']:
        return 36
    if 'Фрунзенская' in row['Метро']:
        return 37
    if 'Ломоносовский проспект' in row['Метро']:
        return 38
    if 'Марксистская' in row['Метро']:
        return 39
    if 'Таганская' in row['Метро']:
        return 40
    if 'Павелецкая' in row['Метро']:
        return 41
    if 'Раменки' in row['Метро']:
        return 42
    if 'Улица 1905 года' in row['Метро']:
        return 43
    if 'Кутузовская' in row['Метро']:
        return 44
    if 'Университет' in row['Метро']:
        return 45
    if 'Проспект Мира' in row['Метро']:
        return 46
    if 'Красносельская' in row['Метро']:
        return 47
    if 'Студенческая' in row['Метро']:
        return 48
    if 'Менделеевская' in row['Метро']:
        return 49
    if 'Новослободская' in row['Метро']:
        return 50
    if 'Комсомольская' in row['Метро']:
        return 51
    if 'Беговая' in row['Метро']:
        return 52
    if 'Спортивная' in row['Метро']:
        return 53
    if 'Парк Победы' in row['Метро']:
        return 54
    if 'Воробьевы горы' in row['Метро']:
        return 55
    if 'Минская' in row['Метро']:
        return 56
    if 'Динамо' in row['Метро']:
        return 57
    if 'Ленинский проспект' in row['Метро']:
        return 58
    if 'Шаболовская' in row['Метро']:
        return 59
    if 'Достоевская' in row['Метро']:
        return 60
    if 'Выставочная' in row['Метро']:
        return 61
    if 'Деловой центр' in row['Метро']:
        return 62
    if 'Международная' in row['Метро']:
        return 63
    if 'Рижская' in row['Метро']:
        return 64
    if 'Площадь Ильича' in row['Метро']:
        return 65
    if 'Римская' in row['Метро']:
        return 66
    if 'Проспект Вернадского' in row['Метро']:
        return 67
    if 'Бауманская' in row['Метро']:
        return 68
    if 'Крестьянская застава' in row['Метро']:
        return 69
    if 'Пролетарская' in row['Метро']:
        return 70
    if 'Академическая' in row['Метро']:
        return 71
    if 'Сокольники' in row['Метро']:
        return 72
    if 'Сокол' in row['Метро']:
        return 73
    if 'Марьина роща' in row['Метро']:
        return 74
    if 'Аэропорт' in row['Метро']:
        return 75
    if 'Алексеевская' in row['Метро']:
        return 76
    if 'Новые Черёмушки' in row['Метро']:
        return 77
    if 'Фили' in row['Метро']:
        return 78
    if 'Профсоюзная' in row['Метро']:
        return 79
    if 'Октябрьское Поле' in row['Метро']:
        return 80
    if 'Тульская' in row['Метро']:
        return 81
    if 'Савеловская' in row['Метро']:
        return 82
    if 'Полежаевская' in row['Метро']:
        return 83
    if 'Щукинская' in row['Метро']:
        return 84
    if 'Калужская' in row['Метро']:
        return 85
    if 'Багратионовская' in row['Метро']:
        return 86
    if 'Юго-Западная' in row['Метро']:
        return 87
    if 'Славянский бульвар' in row['Метро']:
        return 88
    if 'Электрозаводская' in row['Метро']:
        return 89
    if 'Крылатское' in row['Метро']:
        return 90
    if 'Автозаводская' in row['Метро']:
        return 91
    if 'Дубровка' in row['Метро']:
        return 92
    if 'ВДНХ' in row['Метро']:
        return 93
    if 'Кунцевская' in row['Метро']:
        return 94
    if 'Пионерская' in row['Метро']:
        return 95
    if 'Тропарёво' in row['Метро']:
        return 96
    if 'Филевский парк' in row['Метро']:
        return 97
    if 'Дмитровская' in row['Метро']:
        return 98
    if 'Войковская' in row['Метро']:
        return 99
    if 'Молодежная' in row['Метро']:
        return 100
    if 'Нагатинская' in row['Метро']:
        return 101
    if 'Волгоградский проспект' in row['Метро']:
        return 102
    if 'Технопарк' in row['Метро']:
        return 103
    if 'Авиамоторная' in row['Метро']:
        return 104
    if 'Водный стадион' in row['Метро']:
        return 105
    if 'Тимирязевская' in row['Метро']:
        return 106
    if 'Нагорная' in row['Метро']:
        return 107
    if 'Нахимовский Проспект' in row['Метро']:
        return 108
    if 'Тушинская' in row['Метро']:
        return 109
    if 'Коломенская' in row['Метро']:
        return 110
    if 'Речной вокзал' in row['Метро']:
        return 111
    if 'Беляево' in row['Метро']:
        return 112
    if 'Строгино' in row['Метро']:
        return 113
    if 'Семеновская' in row['Метро']:
        return 114
    if 'Спартак' in row['Метро']:
        return 115
    if 'Коньково' in row['Метро']:
        return 116
    if 'Каховская' in row['Метро']:
        return 117
    if 'Севастопольская' in row['Метро']:
        return 118
    if 'Ботанический сад' in row['Метро']:
        return 119
    if 'Свиблово' in row['Метро']:
        return 120
    if 'Кожуховская' in row['Метро']:
        return 121
    if 'Сходненская' in row['Метро']:
        return 122
    if 'Планерная' in row['Метро']:
        return 123
    if 'Петровско-Разумовская' in row['Метро']:
        return 124
    if 'Партизанская' in row['Метро']:
        return 125
    if 'Чертановская' in row['Метро']:
        return 126
    if 'Измайловская' in row['Метро']:
        return 127
    if 'Каширская' in row['Метро']:
        return 128
    if 'Варшавская' in row['Метро']:
        return 129
    if 'Южная' in row['Метро']:
        return 130
    if 'Первомайская' in row['Метро']:
        return 131
    if 'Бульвар Рокоссовского' in row['Метро']:
        return 132
    if 'Преображенская площадь' in row['Метро']:
        return 133
    if 'Битцевский парк' in row['Метро']:
        return 134
    if 'Новоясеневская' in row['Метро']:
        return 135
    if 'Теплый стан' in row['Метро']:
        return 136
    if 'Владыкино' in row['Метро']:
        return 137
    if 'Ясенево' in row['Метро']:
        return 138
    if 'Шоссе Энтузиастов' in row['Метро']:
        return 139
    if 'Митино' in row['Метро']:
        return 140
    if 'Домодедовская' in row['Метро']:
        return 141
    if 'Медведково' in row['Метро']:
        return 142
    if 'Отрадное' in row['Метро']:
        return 143
    if 'Черкизовская' in row['Метро']:
        return 144
    if 'Новогиреево' in row['Метро']:
        return 145
    if 'Улица академика Янгеля' in row['Метро']:
        return 146
    if 'Бабушкинская' in row['Метро']:
        return 147
    if 'Люблино' in row['Метро']:
        return 148
    if 'Пражская' in row['Метро']:
        return 149
    if 'Братиславская' in row['Метро']:
        return 150
    if 'Пятницкое шоссе' in row['Метро']:
        return 151
    if 'Аннино' in row['Метро']:
        return 152
    if 'Щелковская' in row['Метро']:
        return 153
    if 'Бибирево' in row['Метро']:
        return 154
    if 'Лесопарковая' in row['Метро']:
        return 155
    if 'Текстильщики' in row['Метро']:
        return 156
    if 'Шипиловская' in row['Метро']:
        return 157
    if 'Бульвар Дмитрия Донского' in row['Метро']:
        return 158
    if 'Улица Старокачаловская' in row['Метро']:
        return 159
    if 'Орехово' in row['Метро']:
        return 160
    if 'Волжская' in row['Метро']:
        return 161
    if 'Марьино' in row['Метро']:
        return 162
    if 'Печатники' in row['Метро']:
        return 163
    if 'Кузьминки' in row['Метро']:
        return 164
    if 'Алтуфьево' in row['Метро']:
        return 165
    if 'Борисово' in row['Метро']:
        return 166
    if 'Кантемировская' in row['Метро']:
        return 167
    if 'Волоколамская' in row['Метро']:
        return 168
    if 'Царицыно' in row['Метро']:
        return 169
    if 'Красногвардейская' in row['Метро']:
        return 170
    if 'Зябликово' in row['Метро']:
        return 171
    if 'Перово' in row['Метро']:
        return 172
    if 'Рязанский проспект' in row['Метро']:
        return 173
    if 'Алма-Атинская' in row['Метро']:
        return 174
    if 'Выхино' in row['Метро']:
        return 175
    if 'Жулебино' in row['Метро']:
        return 176
    if 'Мякинино' in row['Метро']:
        return 177
    if 'Лермонтовский проспект' in row['Метро']:
        return 178
    if 'Улица Скобелевская' in row['Метро']:
        return 179
    if 'Новокосино' in row['Метро']:
        return 180
    if 'Бульвар адмирала Ушакова' in row['Метро']:
        return 181
    if 'Улица Горчакова' in row['Метро']:
        return 182
    if 'Бунинская аллея' in row['Метро']:
        return 183
    if 'Румянцево' in row['Метро']:
        return 184
    if 'Саларьево' in row['Метро']:
        return 185
    if 'Котельники' in row['Метро']:
        return 186
    
    if 'Марк' in row['Метро']:
        return 2023
    if 'Новодачная' in row['Метро']:
        return 2024
    if 'Долгопрудная' in row['Метро']:
        return 2025
    if 'Ховрино' in row['Метро']:
        return 2026
    if 'Лианозово' in row['Метро']:
        return 2027
    if 'Селигерская' in row['Метро']:
        return 2028
    if 'ЗИЛ' in row['Метро']:
        return 2029
    if 'Крымская' in row['Метро']:
        return 2030
    if 'Верхние котлы' in row['Метро']:
        return 2031
    if 'Покровское' in row['Метро']:
        return 2032
    if 'Площадь Гагарина' in row['Метро']:
        return 2033
    if 'Нахимовский проспект' in row['Метро']:
        return 2034
    if 'Улица Акадмика Янгеля' in row['Метро']:
        return 2035
    if 'Битца' in row['Метро']:
        return 2036
    if 'Москворечье' in row['Метро']:
        return 2037
    if 'Пенягино' in row['Метро']:
        return 2038
    if 'Перерва' in row['Метро']:
        return 2039
    if 'Кубанская' in row['Метро']:
        return 2040
    if 'Депо' in row['Метро']:
        return 2041
    if 'Окская' in row['Метро']:
        return 2042
    if 'Красный Балтиец' in row['Метро']:
        return 2043
    if 'Коптево' in row['Метро']:
        return 2044
    if 'Окружная' in row['Метро']:
        return 2045
    if 'Лихоборы' in row['Метро']:
        return 2046
    if 'Дегунино' in row['Метро']:
        return 2047
    if 'Беломорская' in row['Метро']:
        return 2048
    if 'Ростокино' in row['Метро']:
        return 2049
    if 'Выставочный центр' in row['Метро']:
        return 2050
    if 'Эйзенштейна' in row['Метро']:
        return 2051
    if 'Эйзенштейна' in row['Метро']:
        return 2052
    if 'Давыдково' in row['Метро']:
        return 2053
    if 'Мичуринский проспект' in row['Метро']:
        return 2054
    if 'Аминьевская' in row['Метро']:
        return 2055
    if 'Озерная' in row['Метро']:
        return 2056
    if 'Локомотив' in row['Метро']:
        return 2057
    if 'Тропарево' in row['Метро']:
        return 2058
    if 'Новопеределкино' in row['Метро']:
        return 2059
    if 'Рабочий поселок' in row['Метро']:
        return 2060
    if 'Измайлово' in row['Метро']:
        return 2061
    if 'Юго-Восточная' in row['Метро']:
        return 2062
    
    else:
        return 0

flats['Weight_index'] = flats.apply(assign_weight, axis=1)
print(flats)

for i, row in flats.iterrows():
    if pd.isna(row['Парковка']) and ('стихийная' in row['Описание'] or 'стихийный' in row['Описание'] or
                                     'стихийно' in row['Описание'] or 'наземная' in row['Описание'] or 
                                     'наземный' in row['Описание'] or 'парковка' in row['Описание'] 
                                     or 'Парковка' in row['Описание'] or 'Стихийная' in row['Описание'] 
                                     or 'Стихийный' in row['Описание'] or 'Наземная' in row['Описание'] 
                                     or 'ПАРКОВКА' in row['Описание'] or 'машиноместа' in row['Описание'] 
                                     or 'машино-место' in row['Описание'] or 'машино-местом' in row['Описание'] 
                                     or 'Парковочное' in row['Описание'] or 'парковочное'  in row['Описание']):
        flats.loc[i, 'Парковка'] = 'наземная'

for i, row in flats.iterrows():
    if pd.isna(row['Парковка']) and ('подземный' in row['Описание'] or 'подземном' in row['Описание'] or 
                                     'подземная' in row['Описание'] or 'машиноместо' in row['Описание']
                                      or 'паркинг' in row['Описание'] or 'Паркинг' in row['Описание'] 
                                      or 'Подземный' in row['Описание'] or 'Машиноместо' in row['Описание'] 
                                      or 'МАШИНОМЕСТО' in row['Описание'] or 'ПАРКИНГ' in row['Описание'] 
                                      or 'подземной' in row['Описание']):
        flats.loc[i, 'Парковка'] = 'подземная'



#description = parking_00['Описание']
#description.to_csv('_парковки.txt', index=False, header=True)

no_metro = flats.query('Weight_index == 0')
print(no_metro)

print(flats.head(10))
flats.to_csv('flats_updated.csv', index=False)

parking_00 = flats[flats['Парковка'].isna()]
#flats = flats['Парковка'].fillna('отсутствует', inplace=True)
flats.loc[flats['Парковка'].isna(), 'Парковка'] = 'отсутствует или информация о ней не предоставлена в полном объеме'
print(flats.head(10))

metro_zero = flats[flats['Weight_index'] == 0]
metro_zero.to_csv('metro_2023_stations.csv', index=False)

flats_new = flats[flats['Weight_index'] != 0].copy()
flats_new.to_csv('flats_updated_ИТОГ_по_метро_и_парковкам_Москва.csv', index=False)

