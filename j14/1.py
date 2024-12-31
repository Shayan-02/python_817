f = open("./test2.txt", "a")

# print(f.readline())
# print(f.readlines())
# print()
# print(f.read())

a = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, laboriosam.\n
"""


f.writelines(a)

try:
    print(f.readline())
except Exception as e:
    print(e)