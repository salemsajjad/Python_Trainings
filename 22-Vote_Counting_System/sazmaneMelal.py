import collections

tedad = int(input())
ara = collections.OrderedDict()

for i in range(0, tedad):
    country = input()
    ara[country]  = ara.get(country, 0) + 1

ara_ordered = collections.OrderedDict(sorted(ara.items(), key=lambda t: t[0]))

for this_one in list(ara_ordered.keys()):
    print(this_one, ara_ordered[this_one])