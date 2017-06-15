# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:32:42 2017

@author: zui
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:24:54 2017

@author: zui
"""
import copy
import os
import datetime
import sys

def ReadGraphFromFile(fileName):
    filePath = "C:/Users/zui/Desktop/test" + "/" + fileName
    with open(filePath, 'r') as fr:
        i = 0
        for line in fr:
            if line[-1] == '\n':
                line = line[:-1]
            if line.strip() != "": 
                line = line.strip().replace(' ','')
                if line != '-1':
                    data = map(int, line.split(','))
                    graph[i] = data
                else:
                    graph[i] = []
                i += 1
    return

def Check(path, x):
    p = copy.deepcopy(path)
    if len(p) > 0:
        p.pop(0)
    while len(p) > 0:
        if p[0] == x:
            return True
        p.pop(0)
    return False

def DFS(path, key):
    value = graph[key]
    for t in value:
        while Check(path,t) == False:
            path.append(t)
            simplePath.append(copy.deepcopy(path))
            if path[0] != t:
                DFS(copy.deepcopy(path),t)
        while path[-1] != key:
            path.pop()
    path.pop()
    return

def GetSimplePath():
    for key in graph.keys():     
        path = []
        path.append(key)
        simplePath.append(copy.deepcopy(path))
        DFS(copy.deepcopy(path),key)
        path.pop()       
    return

#path1是否是path2的子路径
def IsSub(path1, path2):
    len1 = len(path1)
    len2 = len(path2)
    if len1 > len2:
        return False
    i=0
    j=0
    while (i<len1 and j<len2):
        if path1[i] == path2[j]:
            i+=1
            j+=1
        else:
            j = j - i + 1
            i = 0
    if i >= len1:
        return True
    return False

def GetPrimePath():
    global primePath
    primePath = copy.deepcopy(simplePath)
    i = 0
    while(i != len(primePath)):
        for j in range(0, len(primePath)):
            flag = False
            if i == j:
                pass
            else:
                if IsSub(primePath[i], primePath[j]) == True:
                    del(primePath[i])
                    flag = True
                    break
        if flag == False:
            i += 1
     
def ResultToFiles(fileName):
    filePath = "C:/Users/zui/Desktop/test" + "/" + fileName
    with open(filePath, 'w') as fr:
        fr.write("graph = {\n")
        for g in graph.items():
            fr.write('\t' + str(g)[1:-1] + '\n')
        fr.write("}\n")
        fr.write("the number of primePath:%d"%(len(primePath)) + '\n')
        i = 0
        for path in primePath:
            i += 1
            fr.write("path" + str(i) + ': ' + str(path) + '\n')
    return   

print("graph     the number of primepath")
for i in range(0, 15):
    graph = dict()
    simplePath = []
    primePath =[]
    graph.clear()
    ReadGraphFromFile('case'+str(i)+'.txt')
    GetSimplePath()
    GetPrimePath()
    primePath = sorted(primePath, key=lambda a: (len(a), a))
    #print(primePath)
    #ResultToFiles('result_'+str(i)+'.txt')
    print("case"+str(i)+":    %d"%(len(primePath)))





