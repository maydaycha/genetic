#!/use/bin/python
# -*- coding: utf-8 -*-

l = ["1國", "2數", "2數", "1英", "1自", "1藝", "1歷","1英", "1自", "1藝"]
def construct_course_list(l):
    result = []
    for ele in l:
        convert = "".join([str(x) for x in bytearray(ele)])
        result.append(convert)
    return result


# print construct_course_list(l)



def round_up(input, dic):
    return input & 10**(-dic)



print round_up(0.12,2)


