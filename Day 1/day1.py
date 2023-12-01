import string
import re


def replace_cursed_things_andStuff(line: str):
    for n in range(len(line)):
        for key, value in mamamia.items():
            line = line.replace(key, value)
    return line


mamamia = {
    'oneight': '18',
    'threeight': '38',
    'fiveight': '58',
    'nineight': '98',
    'sevenine': '79',
    'twone': '21',
    'zerone': '01',
    'eightwo': '82',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',

}
mamamia = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
    'zero': 'z0o',
}
with open('C:\DevC\AdventOfCode23\Day 1\input.txt') as file:
    sum = 0
    first_num, second_num = 0, 0
    lines = file.readlines()
    for line in lines:
        for char in line:
            if str.isnumeric(char):
                if first_num == 0:
                    first_num = char
                    continue
                second_num = char
            if second_num == 0:
                second_num = first_num
        sum += int(first_num + second_num)
        first_num, second_num = 0, 0
    print(sum)
    sum = 0
    first_num, second_num = 0, 0
    for line in lines:
        line = replace_cursed_things_andStuff(line=line)
        for char in line:
            if str.isnumeric(char):
                if first_num == 0:
                    first_num = char
                    continue
                second_num = char
        if second_num == 0:
            second_num = first_num
        sum += int(first_num + second_num)
        first_num, second_num = 0, 0
    print(sum)


def find_things_tm(line):
    trans_line = line.translate(str.maketrans(mamamia))
    print(trans_line)


replace_cursed_things_andStuff("fourseven5seveneightsvtkcjdrfour")
# find_things_tm("fourseven5seveneightsvtkcjdrfour")
