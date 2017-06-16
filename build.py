import operator


def solution_asc(dic):
    ascending_ans=[]
    asc=dic.keys()
    asc.sort()
    for i in range(0,len(asc)):
        ascending_ans.append((asc[i],dic[asc[i]]))
    return ascending_ans


def solution_desc(dic):
    descending_ans=[]
    dsc=dic.keys()
    dsc.sort()
    for i in range(len(dsc),0,-1):
        descending_ans.append((dsc[i-1],dic[dsc[i-1]]))
    return descending_ans
