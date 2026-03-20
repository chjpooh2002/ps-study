N = int(input())
ch = list(input().split())
s = set()
for a in ch:
    if a.endswith("Cheese"):
        s.add(a)
if len(s)==4:
    print("yummy")
else:
    print("sad")