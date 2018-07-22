# -*- coding:utf-8 -*-
import commands


def findinlist(targetlist, x):
    return x in targetlist

def wordcount(file, word):
    return sum([line.count(word) for line in open(file, 'r')])

def wordcount2(file, word):
    command = "grep -wo %s %s | wc -l" % (word, file)
    status, output = commands.getstatusoutput(command)
    if status != 0:
        return 0
    else:
        return int(output)

if __name__ == '__main__':
    # print(findinlist(['a', 'b'], 'b'))
    # print(wordcount('words.txt', 'is'))
    print(wordcount2('t2', 'world'))
