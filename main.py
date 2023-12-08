def highest(l):
    Max = l[0]
    for num in l:
        if Max < num:
            Max = num
    return Max


 highest ([77,48,19,17,93,90])