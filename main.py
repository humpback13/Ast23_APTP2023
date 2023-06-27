from itertools import combinations
from tkinter import *

class Classes:

    def __init__(self, value, day, start, end, day2, start2, end2, kind, prof):
        self.value = value
        self.start = start
        self.end = end
        self.day2 = day2
        self.start2 = start2
        self.end2 = end2
        self.kind = kind
        self.prof = prof
        self.day = day

def printclass(clas):   # 클래스의 인자들을 출력하는 함수

    print(f"{clas.value}\t{clas.day}\t{clas.start}\t{clas.end}\t{clas.day2}\t{clas.start2}\t{clas.end2}"
          f"\t{clas.kind} \t{clas.prof}")

def listed(lst):       # 입력 받은 값들을 요일별로 구별하는 함수

    mon = []
    tue = []
    wed = []
    thr = []
    fri = []
    for i in lst:
        if i.day == 'mon':
            mon.append([i.day, i.start, i.end])
        if i.day == 'tue':
            tue.append([i.day, i.start, i.end])
        if i.day == 'wed':
            wed.append([i.day, i.start, i.end])
        if i.day == 'thr':
            thr.append([i.day, i.start, i.end])
        if i.day == 'fri':
            fri.append([i.day, i.start, i.end])
        if i.day2 == 'mon':
            mon.append([i.day2, i.start2, i.end2])
        if i.day2 == 'tue':
            tue.append([i.day2, i.start2, i.end2])
        if i.day2 == 'wed':
            wed.append([i.day2, i.start2, i.end2])
        if i.day2 == 'thr':
            thr.append([i.day2, i.start2, i.end2])
        if i.day2 == 'fri':
            fri.append([i.day2, i.start2, i.end2])

    mon.sort(key=lambda x: (x[2], x[1]))
    tue.sort(key=lambda x: (x[2], x[1]))
    wed.sort(key=lambda x: (x[2], x[1]))
    thr.sort(key=lambda x: (x[2], x[1]))
    fri.sort(key=lambda x: (x[2], x[1]))
    return [mon, tue, wed, thr, fri]


def makecomb(lst, num): # 각 요일의 시간표들의 모든 조합을 만드는 함수 day->list, num->int

    result = list(combinations(lst, num))
    return result

def makeavaile(result): # 만들어진 조합 중에서 실제로 가능한 시간표를 찾아내는 함수 result->list, num->int

    availelist = []
    for k in result:  # 시간표
        flag = 0                                      # 전부 k에 대한 작업 진행중
        kindlist = []
        for kind in k:          # 같은 수업 배제
            kindlist.append(kind.kind)
        if len(kindlist) != len(set(kindlist)):
            continue        # 여기까지는 그냥 하면됨
        daylist = listed(k)
        for i in daylist: # i->mon, tue ...
            for j in range(len(i)-1):     # 각 요일에 대한 시간표
                if i[j][2] > i[j+1][1]:
                    flag = 1
        if flag == 0:
            availelist.append(k)
    return availelist

def makemax(availelist, num):    # 실제로 가능한 시간표 중에서 가중치가 가장 높은 시간표의 위치를 찾는 함수 availelist->list, num->int

    valuesum = []
    for i in availelist:
        vs = 0
        for j in range(num):
            vs += i[j].value
        valuesum.append(vs)
    if len(valuesum) != 0:
        v = max(valuesum)
    else:
        v = 0
    maxidx = [i for i, value in enumerate(valuesum) if value == max(valuesum)]
    return maxidx, v

def readtxt(filename):

    f = open(filename, 'r')
    classlist = []
    while True:
        f_line = f.readline()
        if not f_line:
            break
        f_list = f_line.split()
        classlist.append(Classes(int(f_list[0]), f_list[1], int(f_list[2]), int(f_list[3]), f_list[4], int(f_list[5]),
                                 int(f_list[6]), f_list[7], f_list[8]))

    f.close()
    return classlist

def writetxt(filename, maxidxlist, ava, num, val):

    f = open(filename, 'w')
    if len(ava) == 0:
        f.write(f"There is no available schedule")
    for i in maxidxlist:
        f.write(f"sum of value : {val}\n")
        f.write(f"position of max value : {i}\n")
    f.write("\n")
    for i in maxidxlist:
        for j in range(num):
            f.write(f"{ava[i][j].value}\t{ava[i][j].day}\t{ava[i][j].start}\t{ava[i][j].end}\t{ava[i][j].day2}\t"
                    f"{ava[i][j].start2}\t{ava[i][j].end2}\t{ava[i][j].kind} \t{ava[i][j].prof}\n")
        f.write(f"\n")
    f.close()
    return

num = int(input("들을 강의의 개수 : "))
lst = readtxt("lecture.txt")
lst.sort(key=lambda x: (x.end, x.start))

result = makecomb(lst, num)
availelist = makeavaile(result)
maxidxlist, val = makemax(availelist, num)

writetxt('result.txt', maxidxlist, availelist, num, val)

#for i in result:
#    for j in range(num):
#        printclass(i[j])
#    print()
#print()
#print()
#for i in availelist:
#    for j in range(num):
#       printclass(i[j])
#    print()

if len(availelist) == 0:
    print("There is no available schedule\n")

#print(f"{len(availelist)}\n")
print(f"가중치 합 : {val}\n")
for i in maxidxlist:
    print(f"가중치 합이 최대인 시간표의 위치 : {i}\n")

for j in maxidxlist:
    for i in range(num):
       printclass(availelist[j][i])
    print()
