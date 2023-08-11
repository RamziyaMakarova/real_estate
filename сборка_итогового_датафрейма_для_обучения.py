#Удаляем ненужные столбцы
retail_new = retail.drop(retail.columns[[0,2,3,5,10,11,13,14,15,16,17,18,19,20,21,22,23]], axis= 1)

#Выделяем общую стоимость аренды
new_price = retail_new['Цена'].str.split(' ', expand=True)
new_price[0] = new_price[0].astype("float")

#Выделяем количество этажей
retail_new['Дом'].apply(lambda x: x.split('/')[0]).astype("float")


#Создаем новый дф и заносим туда данные
ret_f = pd.DataFrame()
#ret_f.insert(0, 'Price', new_price['ID объявления'])
ret_f.insert(0, 'Price', new_price[0])
ret_f.insert(1, 'Metro_index', retail_new['Weight_index'])
ret_f.insert(2, 'S', retail_new['Площадь, м2'].apply(lambda x: x.split('/')[0]))
ret_f['S'] = ret_f['S'].astype(float)
ret_f.insert(3, 'Floor', retail_new['Дом'].apply(lambda x: x.split('/')[0]))
ret_f['Floor'] = ret_f['Floor'].astype(int)
ret_f.insert(4, 'Price for 1m2', new_price[0] / ret_f['S'])
ret_f['Price for 1m2'] = ret_f['Price for 1m2'].round(2)
ret_f.insert(5, 'Remont_index', retail_new['Ремонт'])
ret_f.insert(6, 'Parking_index', retail_new['Парковка'])


#Индексируем ремонт
ret_f['Remont_index'] = ret_f['Remont_index'].astype('str')
def rem_index(row):
    if 'Дизайнерский' in row['Remont_index']:
        return 3
    if 'Евроремонт' in row['Remont_index']:
        return 2
    if 'Косметический' in row['Remont_index']:
        return 1
    if 'Без ремонта' in row['Remont_index']:
        return 0
    else:
        return 0
ret_f['Remont_index'] = ret_f.apply(rem_index, axis=1)


#Индексируем парковку
ret_f['Parking_index'] = ret_f['Parking_index'].astype('str')
def park_index(row):
    if 'на крыше' in row['Parking_index']:
        return 5
    if 'подземная' in row['Parking_index']:
        return 4
    if 'многоуровневая' in row['Parking_index']:
        return 3
    if 'наземная' in row['Parking_index']:
        return 2
    if 'открытая' in row['Parking_index']:
        return 1
    if 'отсутствует или информация о ней не предоставлена в полном объеме' in row['Parking_index']:
        return 0
    else:
        return 0
ret_f['Parking_index'] = ret_f.apply(park_index, axis=1)

ret_f.dtypes