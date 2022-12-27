#!/usr/bin/python3
for k in range(100):
    if k == 99:
        print('{:02d}'.format(k))
        continue
    print('{:02d}, '.format(k))
