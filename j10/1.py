import random


choices = ['rock', 'paper', 'scissors']
a = random.randint(1,100)
b = random.choice(choices)
c = random.uniform(1,100)
d = random.sample(range(1,1000),10)
e = random.random()
print(a, b, c, d, e)