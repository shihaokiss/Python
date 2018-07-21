# -*- coding:utf-8 -*-

def findinlist(targetlist, x):
    return x in targetlist

def wordcount(file, word):
    return sum([line.count(word) for line in open(file, 'r')])

if __name__ == '__main__':
    # print(findinlist(['a', 'b'], 'b'))
    print(wordcount('words.txt', 'is'))
