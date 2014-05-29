#!/use/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import random as r
import sys, json, copy, math



GENETIC_LENGTH = 5                 # 基因長度
POPULATION_CNT = 100                # 母群數量
ITERA_CNT = 10000                    # 迭代次數
CROSSOVER_RATE = 0.5               # 交配率
MUTATION_RATE = 0.1                # 突變率


# consrust a course list for a week (a day)
# course_list = ["1國", "2數", "2數", "1英", "1自", "1藝", "1歷", "1藝", "1英", "1歷", "1體", "1音", "1化"]
# course_list.extend(["1國", "1英", "1自", "1藝", "1歷", "1音", "1化", "1息"])
# course_list.extend(["1國", "1英", "1自", "1藝", "1歷", "1音", "1化", "1息"])
# course_list = construct_course_list(course_list)

course_list = []

temp_course_list = []
monday = ["1103", "2102", "2102", "1107", "1104", "1118", "1116"]
tuesday = ["1107", "1107", "2109","2109", "2105","2105", "1110"]
wednesday = ["1107", "1103", "1102", "1118", "1117", "1116", "1114"]
thursday = ["2117","2117", "2114","2114", "1121","2120","2120"]
friday = ["2101","2101", "2105","2105", "1109", "1110", "1112"]

temp_course_list.extend(monday)
temp_course_list.extend(tuesday)
temp_course_list.extend(wednesday)
temp_course_list.extend(thursday)
temp_course_list.extend(friday)
course_list.append(temp_course_list)


num_of_course = len(monday) + len(tuesday) + len(wednesday) + len(thursday) + len(friday)

temp_course_list = []
monday = ["1101", "2102", "2102", "1107", "1104", "1118", "1116"]
tuesday = ["1107", "1107", "2109","2109", "2105","2105", "1110"]
wednesday = ["1107", "1103", "1102", "1118", "1117", "1116", "1114"]
thursday = ["2117","2117", "2114","2114", "1121","2120","2120"]
friday = ["2101","2101", "2105","2105", "1109", "1110", "1112"]
temp_course_list.extend(monday)
temp_course_list.extend(tuesday)
temp_course_list.extend(wednesday)
temp_course_list.extend(thursday)
temp_course_list.extend(friday)
course_list.append(temp_course_list)

temp_course_list = []
monday = ["2105", "2105", "2102", "2102", "1111", "2118", "2118"]
tuesday = ["1102", "2109", "2109","1110", "2105","2105", "1112"]
wednesday = ["2107", "2107", "2102", "2102", "2117", "2117", "1114"]
thursday = ["1117","1111", "2114","2114", "1121","2120","2120"]
friday = ["2111","2111", "2110","2110", "1109", "1115", "1112"]
temp_course_list.extend(monday)
temp_course_list.extend(tuesday)
temp_course_list.extend(wednesday)
temp_course_list.extend(thursday)
temp_course_list.extend(friday)
course_list.append(temp_course_list)

temp_course_list = []
monday = ["1109", "2110", "2110", "2107", "2107", "2118", "2118"]
tuesday = ["1110", "2107", "2107","2109", "2109","1105", "1110"]
wednesday = ["1107", "1103", "1102", "1118", "1117", "1116", "1114"]
thursday = ["1117","1107", "2114","2114", "1120","2121","2121"]
friday = ["2113","2113", "2105","2105", "1109", "1110", "1112"]
temp_course_list.extend(monday)
temp_course_list.extend(tuesday)
temp_course_list.extend(wednesday)
temp_course_list.extend(thursday)
temp_course_list.extend(friday)
course_list.append(temp_course_list)

temp_course_list = []
monday = ["2102", "2102", "1102", "1107", "1104", "1120", "1116"]
tuesday = ["2107", "2107", "2109","2109", "1101","2105", "2105"]
wednesday = ["2107", "2107", "2109","2109", "1101","2105", "2105"]
thursday = ["2117","2117", "2114","2114", "1121","2120","2120"]
friday = ["1101", "2102", "2102", "1107", "1104", "1118", "1116"]
temp_course_list.extend(monday)
temp_course_list.extend(tuesday)
temp_course_list.extend(wednesday)
temp_course_list.extend(thursday)
temp_course_list.extend(friday)
course_list.append(temp_course_list)


# monday = ["1101", "1102", "1109", "1107", "1104", "1110", "1116"]
# tuesday = ["2107", "2107", "2109","2109", "1105","1120", "1110"]
# wednesday = ["2117","2117", "2105","2105", "1117", "1116", "1114"]
# thursday = [ "1109", "1110", "2114","2114", "1121","2120","2120"]
# friday = ["1121","1109", "2105","2105", "1109", "2114","2114"]

# monday = ["2117","2117","1110", "1112", "1104", "1118", "1116"]
# tuesday = ["2107", "2107", "2109","2109", "2105","2105", "1110"]
# wednesday = ["1107", "1103", "1102", "1118", "1117", "1116", "1114"]
# thursday = ["2101", "2105",  "1118", "1117",  "1104", "1118", "1116"]
# friday = ["1102", "1118", "2105","2105", "1109", "1110", "1112"]

# monday = ["1101", "2102", "2102", "1107", "1104", "1118", "1116"]
# tuesday = ["1107", "1104","2117","2117", "1109", "1110", "1110"]
# wednesday = ["1107", "2102", "2102", "1118", "1117", "1116", "1114"]
# thursday = ["2117","2117","2105","2105", "1109", "1110", "1112"]
# friday = ["2101","2101", "1109", "1110", "2117","2117", "1112"]

# temp_course_list.extend(monday)
# temp_course_list.extend(tuesday)
# temp_course_list.extend(wednesday)
# temp_course_list.extend(thursday)
# temp_course_list.extend(friday)
# course_list.append(temp_course_list)
# course_list = construct_course_list(course_list)


class_list = course_list

population = []
pool = []
best_gen = {'fitness': 0, 'genetic': list}
print id(best_gen)

# 進行初始化
def initialize(best_gen):
    for i in xrange(POPULATION_CNT):
        gen = []
        for g in class_list:
            gen.append(random_list_of_string(g))
        population.append({'fitness': cal_fitness(gen), 'genetic': gen})
        if i == 0:
            best_gen['fitness'] = population[0]['fitness']
            best_gen['genetic'] = copy.deepcopy(population[0]['genetic'])
        elif population[i]['fitness'] > best_gen['fitness']:
            best_gen['fitness'] = population[i]['fitness']
            best_gen['genetic'] = copy.deepcopy(population[i]['genetic'])




# 適應函式
def cal_fitness(genetic):
    punish = 0
    try:
        punish = 1 / (adaptable1(genetic) + adaptable2(genetic) + adaptable3(genetic) + conflict(genetic) + 1)
    except ValueError:
        punish = 0
    return punish


# 計算衝堂個數
def conflict(genetic):
    punish = 0
    for i in range(len(genetic[0])):
        list_for_test = [j[i] for j in genetic]
        if len(set(list_for_test)) != len(list_for_test):
            punish += 1
    return punish * 100


# 隨機取得突變位置
def GAPosRand():
    return r.randint(0, GENETIC_LENGTH-1)

# 隨機產生~1 的亂數
def srand():
    return r.randint(0, 1) / 10

# 複製, 輪盤式選擇(分配式)
def reproduction():
    slack = POPULATION_CNT
    fitness_sum = 0
    # 計算所有適應值總合
    for i in population:
        fitness_sum += i['fitness']

    # 計算每個母體應複製幾個到交配池中，並直接做複製
    for i in xrange(POPULATION_CNT):
        if slack == 0:
            break
        try:
            cnt = int(math.ceil(population[i]['fitness'] / fitness_sum + 0.5))
        except:
            cnt = 0
        if cnt > slack:
            cnt = slack
        for j in xrange(cnt):
            pool.append(population[i])
        # 調整Slack
        slack -= cnt
    # 若還有沒複製完的
    while len(pool) < POPULATION_CNT:
        # 隨機挑二條不同染色體出來
        pos1 = r.randint(0, POPULATION_CNT-1)
        pos2 = r.randint(0, POPULATION_CNT-1)
        # 比較好的那條丟到交配池去
        if population[pos1]['fitness'] > population[pos2]['fitness']:
            pool.append(population[pos1])
        else:
            pool.append(population[pos2])

def crossover():
    cnt = 0
    for x in xrange(POPULATION_CNT):
        if cnt >= 100:
            break
        p1 = r.randint(0, POPULATION_CNT-1)
        p2 = r.randint(0, POPULATION_CNT-1)

        # 決定是否交配
        crossover_if = srand()

        if crossover_if > CROSSOVER_RATE: # 不交配, 將交配池中之個體丟回母體
            population[cnt] = copy.deepcopy(pool[p1])
            cnt += 1
            population[cnt] = copy.deepcopy(pool[p2])
            cnt += 1
        else: # 單點交配, 交配完後再丟回母體
            pos = GAPosRand()
            for i in xrange(pos):
                population[cnt]['genetic'][i] = copy.copy(pool[p1]['genetic'][i])
                population[cnt+1]['genetic'][i] = copy.copy(pool[p2]['genetic'][i])
            for i in xrange(pos, GENETIC_LENGTH):
                population[cnt+1]['genetic'][i] = copy.copy(pool[p1]['genetic'][i])
                population[cnt]['genetic'][i] = copy.copy(pool[p2]['genetic'][i])
            cnt += 2


def mutation():
    for i in xrange(POPULATION_CNT):
        mutation_if = srand()
        if mutation_if <= MUTATION_RATE:
            pos = GAPosRand() # 突變位置
            pos2 = r.randint(0, len(population[i]['genetic'][pos])-1)
            pos3 = r.randint(0, len(population[i]['genetic'][pos])-1)
            temp = population[i]['genetic'][pos][pos2]
            population[i]['genetic'][pos][pos2] = population[i]['genetic'][pos][pos3]
            population[i]['genetic'][pos][pos3] = temp
        # 突變完後再算一次母體適應值
        population[i]['fitness'] = cal_fitness(population[i]['genetic'])

        if i == 0:
            best_gen['fitness'] = population[0]['fitness']
            best_gen['genetic'] = copy.deepcopy(population[0]['genetic'])
        elif population[i]['fitness'] > best_gen['fitness']:
            best_gen['fitness'] = population[i]['fitness']
            best_gen['genetic'] = copy.deepcopy(population[i]['genetic'])
        print "best"
        print best_gen




# normal function
def random_list_of_string(l):
    a = []
    l = list(l)
    # print "===============origin=================="
    # print l
    # print "===============origin=================="
    while l:
        e = r.choice(l)
        if e[:1] == '2': # 連續2堂
            index = l.index(e)
            for i in xrange(2):
                a.append(l.pop(index))
        elif e[:1] == '3': # 連續3堂
            for i in xrange(3):
                index = l.index(e)
                a.append(l.pop(index))
        else:
            l.remove(e)
            a.append(e)

        # print "=============================="
        # print a
    return a


def random_list_of_string2(g):
    a = []
    result = []
    for i in g:
        l = list(i)
        while l:
            e = r.choice(l)
            if e[:1] == '2': # 連續2堂
                index = l.index(e)
                for i in xrange(2):
                    a.append(l.pop(index))
            elif e[:1] == '3': # 連續3堂
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


def mating2(par1, par2):
    select_class = r.randint(0, len(course_list) - 1 )
    child2 = []
    p1 = copy.deepcopy(par1)
    # 將 p1 交配至 c2
    for i in xrange(len(course_list)):
        if i == select_class:
            child2.append([None] * 35)
            while len(p1[select_class]) > 0:
                ele = r.choice(p1[select_class]) # 隨機選擇一節課
                if ele[:1] == '2': # 選出來的課是連課
                    index = p1[select_class].index(ele)
                    random_input_index = r.randint(0, 6)
                    child2[i][random_input_index] = p1[select_class].pop(index)
                    child2[i][(random_input_index+1)] = p1[select_class].pop(index)
                else:
                    index = p1[select_class].index(ele)
                    random_input_index = r.randint(0, 6)
                    child2[i][random_input_index] = p1[select_class].pop(index)
        else: # 不用交配的班級直接放
            child2.append(par2[i])
    return child2


# 硬性規定
    # 禮拜三早上週會 (15節)
def hard_rule1(adjusted_class1, adjusted_class2, adjusting_class1, adjusting_class2):
    order_of_class = 15
    adjusting_class1[order_of_class] = adjusted_class2[order_of_class]
    adjusting_class2[order_of_class] = adjusted_class1[order_of_class]



# 軟性規定

# 一天不排兩節或兩節以上的國文(03)、英文(07)、數學(02)、生物(22)、理化(23)
def adaptable1(genetic):
    total_punish = 0
    gen = copy.deepcopy(genetic)
    for i in xrange(len(genetic)):
        for j in range(5):
            count = 0
            for x in xrange(7):
                if gen[i].pop(0)[:1] == '2':
                    count += 1
            if count > 2:
                total_punish += 1
    return 100 * total_punish

# 社會 ＝ "24", 歷史 ＝ "16", 地理 = "10", 公民 = "14", 音樂 = "09", 美術 = "25", 體育 = "08"
def adaptable2(genetic):
    gen = copy.deepcopy(genetic)
    compaire_list = [{'course_num': '24', 'counter': 0, 'encounter': False}, {'course_num': '16', 'counter': 0, 'encounter': False}, {'course_num': '10', 'counter': 0, 'encounter': False}, {'course_num': '14', 'counter': 0, 'encounter': False}, {'course_num': '09', 'counter': 0, 'encounter': False}, {'course_num': '25', 'counter': 0, 'encounter': False}, {'course_num': '08', 'counter': 0, 'encounter': False}]
    total_punish = 0
    for i in xrange(len(genetic)):
        for j in range(5):
            for x in xrange(7):
                temp = gen[i].pop(0)
                for l in compaire_list:
                    if temp[2:] == l['course_num']:
                        l['encounter'] = True
            for l in compaire_list:
                if l['encounter'] == True:
                    if l['counter'] == 1:
                        total_punish += 1
                        l['counter'] = 0
                    else:
                        l['counter'] += 1
                else:
                    l['counter'] = 0
                l['encounter'] == False
    return 100 * total_punish


# 連堂不可以跨上午下午 (不能在第四，第五節)
def adaptable3(genetic):
    gen = copy.deepcopy(genetic)
    total_punish = 0
    for i in xrange(len(gen)):
        for j in xrange(5):
            if gen[i][ 7 * j + 4][:1] == '2':
                if gen[i][ 7 * j + 4] == gen[i][ 7 * j + 5]:
                    total_punish += 1
    return 10 * total_punish











# course binary string length
# def course_binary_length(name_chinese):
#     return len("".join([str(x) for x in bytearray(name_chinese)]))
# def course_
# course_len = course_binary_length(4)



# initialize course container for class
# n個班
# class_list = []
# for i in range(len(course_list)):
#     class_list.append([None] * num_of_course)



# distribute course, for initialization
# for c in class_list:
#     for current_course in course_list:
#         c.pop(0)
#         c.append(current_course)
# class_list = course_list



# 初始族群
# with open("genetic.txt", "w+") as outfile:
#     genetic_list = []
#     for i in xrange(100):
#         gen = []
#         for g in class_list:
#             gen.append(random_list_of_string(g))
#         dict = {'score': conflict(gen), 'genetic': gen}
#         outfile.write(str(dict)+"\n")
#         genetic_list.append(dict)


# with open("result.txt", "w+") as outfile:
#     for i in range(1000000):
#         r1, r2 = 0, 0
#         while r1 == r2:
#             r1 = r.randrange(0, len(genetic_list))
#             r2 = r.randrange(0, len(genetic_list))
#         child = mating2(genetic_list[r1]['genetic'], genetic_list[r2]['genetic'])
#         test_score = conflict(child)
#         if test_score > genetic_list[r1]['score'] or test_score > genetic_list[r2]['score']:
#             if genetic_list[r1]['score'] > genetic_list[r2]['score']:
#                 genetic_list[r2] = {'score': test_score, 'genetic': child, 'child': True}
#             else:
#                 genetic_list[r1] = {'score': test_score, 'genetic': child, 'child': True}

#     for ele in genetic_list:
#         outfile.write(str(ele)+"\n")


if __name__ == '__main__':
    initialize(best_gen)
    times = 0
    for i in xrange(ITERA_CNT):
        times = i
        reproduction()   # 選擇(分配式)
        crossover() # 交配
        mutation() # 突變
    print population
    print "\n =========================\n"
    print "%d, times" % times
    for j in xrange(POPULATION_CNT):
        print "fitness %f" % (population[j]['fitness'])

    print "\n =========================\n"
    print " ever find best gene : "
    print best_gen







