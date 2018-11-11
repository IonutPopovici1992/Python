def drop_first_last(grades):
    first, *middle, last = grades
    average = sum(middle) / len(middle)
    print(average)


drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])
