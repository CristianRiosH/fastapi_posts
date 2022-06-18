from uuid import uuid4

"""
r= uuid4()
print(type(r))
print(type(r.hex))
print(type(str(r)))
"""

d = [54,25,94,45]
print(d)

def update_list(d, i, v):
    for index, value in enumerate(d):
        if index == i:
            d[index] = v
            print("updated succesfully")

update_list(d, 2, 14)
print(d)