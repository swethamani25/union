e = input()
el = set(map(int,raw_input().split()))
f = input()
fl = set(map(int,raw_input().split()))

u = el.union(fl)

print len(u)