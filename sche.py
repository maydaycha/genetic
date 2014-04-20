#!/use/bin/python
# -*- coding: utf-8 -*-

import random as r
import sys

# normal function
# def random_list_of_string1(l):
#     a = []
#     l = list(l)
#     for i in range(len(l)):
#         ele = r.choice(l)
#         l.remove(ele)
#         a.append(ele)
#     return a

def random_list_of_string(l):
    a = []
    l = list(l)
    while l:
        e = r.choice(l)
        # 連續兩堂
        if e[0] == '5':
            index = l.index(e)
            print "now ele: %s=> index %d" % (e, index)
            print l
            a.append(l.pop(index))
            print l
            a.append(l.pop(index))
            print l
        else:
            l.remove(e)
            a.append(e)
        print "now len %d" % len(l)
    return a









# 開頭1 => 49, 2 => 50
# 一個禮拜35節課

# course name
c = "1國"
m_two = "2數"
e = "1英"
s = "1自"
a = "1藝"
h = "1歷"

c_bin = ""
m_two_bin = ""
e_bin = ""
s_bin = ""
a_bin = ""
h_bin = ""

# transform to binary
for i in bytearray(c):
    c_bin += str(i)
print "%s:%d" % (c_bin, len(c_bin))

for i in bytearray(m_two):
    m_two_bin += str(i)
print "%s:%d" % (m_two_bin, len(m_two_bin))

for i in bytearray(e):
    e_bin += str(i)
print "%s:%d" % (e_bin, len(e_bin))

for i in bytearray(s):
    s_bin += str(i)
print "%s:%d" % (s_bin, len(s_bin))

for i in bytearray(a):
    a_bin += str(i)
print "%s:%d" % (a_bin, len(a_bin))

for i in bytearray(h):
    h_bin += str(i)
print "%s:%d" % (h_bin, len(h_bin))


# consrust a course list for a week (a day)
course_list = [c_bin, m_two_bin, m_two_bin, e_bin, s_bin, a_bin, h_bin]

# course binary string length
course_len = len(c_bin)

num_of_course = len(course_list)


# initialize course container for class
class1, class2, class3 = [None] * num_of_course, [None] * num_of_course,  [None] * num_of_course,
class_list = [class1, class2, class3]



# distribute course, for initialize
for c in class_list:
    for current_course in course_list:
        c.pop(0)
        c.append(current_course)



def test1(genetic):
    punish = 0
    for i in range(num_of_course):
        list_for_test = [j[i] for j in genetic]
        if len(set(list_for_test)) != len(list_for_test):
            punish += 1
    return -punish

def selecttion(genetic_list):
    max = - 99
    max  = [i.score for i in genetic_list if i.score > max]
    # for i in genetic_list:
        # if

def mating(par1, par2):
    # seed = r.randrange(0, len(par1))
    front, end = list(par1)[:len(par1)/2], list(par2)[len(par1)/2:]
    front, end = random_list_of_string(front), random_list_of_string(end)
    return front + end


# print class_list
# sys.exit()

# 初始族群
with open("genetic.txt", "w+") as outfile:
    genetic_list = []
    for i in xrange(100):
        gen = []
        for g in class_list:
            print g
            gen.append(random_list_of_string(g))
        dict = {'score': test1(gen), 'genetic': gen}
        outfile.write(str(dict)+"\n")
        genetic_list.append(dict)

# sys.exit()

with open("result.txt", "w+") as outfile:
    for i in range(1000):
        r1, r2 = 0, 0
        while r1 == r2:
            r1 = r.randrange(0, len(genetic_list))
            r2 = r.randrange(0, len(genetic_list))
            # print r1, r2
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




# g_alg = geneticAlg(gen_1, gen_2, course_len, num_of_course)
# print 'parent'
# g_alg.test()
# print 'child'
# g_alg.mating(g_alg.genetic1, g_alg.genetic2)
# print g_alg.child1
# print g_alg.child2
