# -*- coding: utf-8 -*-

height = 1.75
tem = input('weight:')
weight = float(tem)
bmi = weight/(height*height)
if bmi<18.5:
    print('too light')
elif bmi<=25:
    print('Normal')
elif bmi<=28:
    print('too heavy')
elif bmi<=32:
    print('fat')
else:
    print('too fat')