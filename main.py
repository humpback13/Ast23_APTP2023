from itertools import combinations

class Classes:

    def __init__(self, value, day, start, end, kind, prof):
        self.value = value
        self.start = start
        self.end = end
        self.kind = kind
        self.prof = prof
        self.day = day

def printclass(clas):   # 클래스의 인자들을 출력하는 함수

    print(f"{clas.value}\t{clas.day}\t{clas.start}\t{clas.end}\t{clas.kind} \t{clas.prof}")

def listed(lst):       # 입력 받은 값들을 요일별로 구별하는 함수

    mon = []
    tue = []
    wed = []
    thr = []
    fri = []
    for i in lst:
        if "mon" in i.day:
            mon.append(i)
        elif 'tue' in i.day:
            tue.append(i)
        elif 'wed' in i.day:
            wed.append(i)
        elif 'thr' in i.day:
            thr.append(i)
        elif 'fri' in i.day:
            fri.append(i)
    return [mon, tue, wed, thr, fri]


def makecomb(lst, num): # 각 요일의 시간표들의 모든 조합을 만드는 함수 day->list, num->int

    result = list(combinations(lst, num))
    return result

def makeavaile(result): # 만들어진 조합 중에서 실제로 가능한 시간표를 찾아내는 함수 result->list, num->int

    availelist = []
    for k in result:  # mon tue..-> list4
        flag = 0
        kindlist = []
        for kind in k:          # 같은 수업 배제
            kindlist.append(kind.kind)
        if len(kindlist) != len(set(kindlist)):
            continue
        daylist = listed(k)
        for i in daylist: # i->list
            for j in range(len(i)-1):     # 각 요일에 대한 시간표
                if i[j].end > i[j+1].start:
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

    maxidx = [i for i, value in enumerate(valuesum) if value == max(valuesum)]
    return maxidx

def readtxt(filename):

    f = open(filename, 'r')
    classlist = []
    while True:
        f_line = f.readline()
        if not f_line:
            break
        f_list = f_line.split()
        classlist.append(Classes(int(f_list[0]), f_list[1], int(f_list[2]), int(f_list[3]), f_list[4], f_list[5]))

    f.close()
    return classlist

# for i in result:
#     for j in range(num):
#         printclass(i[j])
#     print()
# print()
# print()
# for i in availelist:
#     for j in range(num):
#         printclass(i[j])
#     print()

num = int(input("들을 강의의 개수 : "))
lst = readtxt("lecture.txt")
n = len(lst)
lst.sort(key=lambda x: (x.end, x.start))

result = makecomb(lst, num)
availelist = makeavaile(result)
maxidxlist = makemax(availelist, num)

if len(availelist) == 0:
    print("There is no available schedule")
# print()
# print()
for i in maxidxlist:
    print(i)
print()
for j in maxidxlist:
    for i in range(num):
        printclass(availelist[j][i])
    print()
