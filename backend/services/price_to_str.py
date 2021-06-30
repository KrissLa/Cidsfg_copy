def price_to_str(value):
    """ Добавляем пробелы в стоимость """
    list_value = list(str(value))
    list_value.reverse()
    if len(list_value) > 3:
        list_value.insert(3, ' ')
    if len(list_value) > 6:
        list_value.insert(7, ' ')
    if len(list_value) > 10:
        list_value.insert(11, ' ')
    list_value.reverse()
    return ''.join(list_value)
