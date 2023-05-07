from itertools import combinations

class Classes:

    def __init__(self, value, day, start, end, kind, prof):
        self.value = value
        self.start = start
        self.end = end
        self.kind = kind
        self.prof = prof
        self.day = day

def printlist(clas):

    print(f"{clas.value}\t{clas.day}\t{clas.start}\t{clas.end}\t{clas.kind} \t{clas.prof}")

def listed(lst):

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


def makecomb(day, num):

    result = list(combinations(day, num))
    return result

def makeavaile(result):

    availelist = []
    for i in result:
        flag = 0
        for j in range(num-1):
            if i[j].end > i[j+1].start:
                flag = 1
        if flag == 0:
            availelist.append(i)
    return availelist

def makemax(availelist):

    valuesum = []
    for i in availelist:
        vs = 0
        for j in range(num):
            vs += i[j].value
        valuesum.append(vs)

    maxidx = valuesum.index(max(valuesum))
    return maxidx


n = int(input("강의의 개수를 입력해주세요 : "))
num = int(input("하루에 들을 강의의 개수 : "))
lst = []

for i in range(n):
    v,s,e = map(int, input("가중치, 시작시간, 끝시간 : ").split())
    d,k,p = map(str, input("날짜, 강의종류, 교수님 : ").split())
    lst.append(Classes(v,d,s,e,k,p))
lst.sort(key=lambda x: (x.end, x.start))

daylist = listed(lst)
mon = daylist[0]
tue = daylist[1]
wed = daylist[2]
thr = daylist[3]
fri = daylist[4]

result = makecomb(mon, num)
availelist = makeavaile(result)
maxidx = makemax(availelist)

for i in range(num):
    printlist(availelist[maxidx][i])
