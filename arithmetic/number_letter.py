# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-9-6 下午2:25


def number_letter(digits):
    number_map = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
    if digits == '':
        return []

    result = ['']
    for index in digits:
        result = [i + j for i in result for j in number_map[index]]
    return result


print(number_letter('2'))
