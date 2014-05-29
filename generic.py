#!/use/bin/python
# -*- coding: utf-8 -*-

import random as r
import sys
import json

# normal function
def random_list_of_string(l):
    a = []
    l = list(l)
    while l:
        e = r.choice(l)
        if e[:2] == '50': # 連續2堂
            index = l.index(e)
            for i in xrange(2):
                a.append(l.pop(index))
        elif e[:2] == '51': # 連續3堂
            for i in xrange(3):
                index = l.index(e)
                a.append(l.pop(index))
        else:
            l.remove(e)
            a.append(e)
    return a


def random_list_of_string2(g):
    a = []
    result = []
    for i in g:
        l = list(i)
        while l:
            e = r.choice(l)
            if e[:2] == '50': # 連續2堂
                index = l.index(e)
                for i in xrange(2):
                    a.append(l.pop(index))
            elif e[:2] == '51': # 連續3堂
                for i in xrange(3):
                    index = l.index(e)
                    a.append(l.pop(index))
            else:
                l.remove(e)
                a.append(e)
        result.append(a)
        a = []
    return result



# 開頭1 => 49, 2 => 50, 3 => 51
# 一個禮拜35節課
# course list
def construct_course_list(l):
    result = []
    for ele in l:
        convert = "".join([str(x) for x in bytearray(ele)])
        result.append(convert)
    return result


# consrust a course list for a week (a day)
course_list = ["1國", "2數", "2數", "1英", "1自", "1藝", "1歷", "1藝", "1英", "1歷", "1體", "1音", "1化"]
course_list.extend(["1國", "1英", "1自", "1藝", "1歷", "1音", "1化", "1息"])
course_list.extend(["1國", "1英", "1自", "1藝", "1歷", "1音", "1化", "1息"])
course_list = construct_course_list(course_list)





# course binary string length
def course_binary_length(name_chinese):
    return len("".join([str(x) for x in bytearray(name_chinese)]))
course_len = course_binary_length("1國")


num_of_course = len(course_list)


# initialize course container for class
# 2個班
class_list = []
for i in range(3):
    class_list.append([None] * num_of_course)




# distribute course, for initialization
for c in class_list:
    for current_course in course_list:
        c.pop(0)
        c.append(current_course)


# 計算衝堂個數
def test1(genetic):
    punish = 0
    for i in range(num_of_course):
        list_for_test = [j[i] for j in genetic]
        if len(set(list_for_test)) != len(list_for_test):
            punish += 1
    return -punish


def selection(genetic_list):
    max = -99
    max  = [i.score for i in genetic_list if i.score > max]
    # for i in genetic_list:
        # if


# 交配
def mating(par1, par2):
    # seed = r.randrange(0, len(par1))
    front, end = list(par1)[:len(par1)/2], list(par2)[len(par1)/2:]
    front, end = random_list_of_string2(front), random_list_of_string2(end)
    return front + end


# print class_list

# 初始族群
with open("genetic.txt", "w+") as outfile:
    genetic_list = []
    for i in xrange(100):
        gen = []
        for g in class_list:
            gen.append(random_list_of_string(g))
        dict = {'score': test1(gen), 'genetic': gen}
        outfile.write(str(dict)+"\n")
        genetic_list.append(dict)


with open("result.txt", "w+") as outfile:
    for i in range(1000000):
        r1, r2 = 0, 0
        while r1 == r2:
            r1 = r.randrange(0, len(genetic_list))
            r2 = r.randrange(0, len(genetic_list))
        child = mating(genetic_list[r1]['genetic'], genetic_list[r2]['genetic'])
        test_score = test1(child)
        if test_score > genetic_list[r1]['score'] or test_score > genetic_list[r2]['score']:
            if genetic_list[r1]['score'] > genetic_list[r2]['score']:
                genetic_list[r2] = {'score': test_score, 'genetic': child, 'child': True}
            else:
                genetic_list[r1] = {'score': test_score, 'genetic': child, 'child': True}

    for ele in genetic_list:
        outfile.write(str(ele)+"\n")













class GeneticAlg(object):
    def __init__(self, genetic1, genetic2, course_len, num_of_course, num_of_class = 2):
        self.genetic1 = genetic1
        self.genetic2 = genetic2
        self.course_len = course_len
        self.chromosome_len = course_len * num_of_course
        self.section = len(genetic1) / self.chromosome_len
        self.num_of_class = num_of_class
        self.child1, self.child2 = [None] * self.num_of_class, [None] * self.num_of_class

    # 不衝堂
    def test1(self, genetic):
        punish = 0
        for i in range(self.num_of_course):
            list_for_test = [j[i] for j in genetic]
            if len(set(list_for_test)) != len(list_for_test):
                punish += 1
        return punish


    def test2(self, genetic):
        test_score2 = 0
        return test_score2


    def score(self, genetic):
        return 1 / (self.test1(genetic))


    # 不缺課
    def rule1(self):
        pass


    def is_acceptable(self):
        for x in range(self.section):
            start, end = self.chromosome_len * x, self.chromosome_len * (x+1)
            if sum([int(i) for i in self.genetic1[start:end]]) == sum([int(i) for i in self.genetic2[start:end]]):
                return False
        return True



    def is_acceptable2(self, genetic):
        if self.test1(genetic) < 3:
            return True
        else:
            return False



    def termintae(self):
        if 1 / (self.test1() + 1) == 1:
            return True
        else:
            return False



    def mating(self, par1, par2):
        seed = r.randrange(0, len(par1))
        self.child1[seed], self.child2[seed] = list(par2[seed]), list(par1[seed])
        self.child1[seed], self.child2[seed] = random_list_of_string(self.child2[seed]), random_list_of_string(self.child1[seed])
        for i in range(self.num_of_class):
            if i == seed:
                pass
            else:
                self.child1[i] = list(par1[i])
                self.child2[i] = list(par2[i])



    def mutation(self):
        print "hi"



    def run(self):
        for i in range(1000):
            self.child1 = self.mating(self.genetic1, self.genetic2)
            self.child2 = self.mating(self.genetic1, self.genetic2)
            if not self.is_acceptable2(self.child1):
                print "skip child1", i, self.child1
                continue
            if not self.is_acceptable2(self.child2):
                print "skip child2", i, self.child2
                continue



