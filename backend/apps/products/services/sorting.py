def sort_series(series_list):
    series_without_sort_number = []
    for i, ser in enumerate(series_list):
        if not ser.sort_number and ser.sort_number != 0:
            series_without_sort_number.append(series_list.pop(i))
    n = 1
    while n < len(series_list):
        for i in range(len(series_list) - n):
            if series_list[i].sort_number > series_list[i + 1].sort_number:
                series_list[i], series_list[i + 1] = series_list[i + 1], series_list[i]
        n += 1
    return series_list + series_without_sort_number
