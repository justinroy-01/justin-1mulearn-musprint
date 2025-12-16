#Tuple continued

#We can use negative index in tuple like list

tup=(234,45,5667,645,34,46,6,76,54,3)

if 45 in tup:
    print ("Hello")
#Slicing in tuple craetes a new tuple
    #Tuple is immutable
#Methods in Tuple

#WE can concatinate 2 tuple
res=tup.count(45)
print("The count of 45 is",res)
res1=tup.index(6)
res1=tup.index(6,4,8)#Here 4-8 is slicing
res2=len(tup)
print("length is ,",res2)

#Exerscice 3
"""
Create a program to display questions like in KBC
"""

questions = [
    "What is 5 + 7?",
    "How many days are there in a week?",
    "Which number is even: 7 or 10?",
    "What is the square of 4?",
    "If a pen costs ₹10, what is the cost of 3 pens?",
    "What comes next in the sequence: 2, 4, 6, ___?",
    "What is 20% of 50?",
    "If x = 5, find 2x + 3.",
    "Which is larger: 3/4 or 2/3?",
    "How many bits make 1 byte?",
    "Find the LCM of 4 and 6.",
    "What is the value of √144?",
    "If the perimeter of a square is 40 cm, what is the length of one side?",
    "Convert binary 1010 to decimal.",
    "A train travels 60 km in 1 hour. What is its speed in m/s?",
    "If A : B = 2 : 3 and B = 15, find A.",
    "Solve: 3x − 7 = 11.",
    "How many trailing zeros are there in 100!?",
    "What is the time complexity of binary search?",
    "If all roses are flowers and some flowers are red, can we say some roses are red?"
]

answers = [
    12,
    7,
    10,
    16,
    30,
    8,
    10,
    13,
    "3/4",
    8,
    12,
    12,
    10,
    10,
    16.67,
    10,
    6,
    24,
    "O(log n)",
    "No"
]
money = [
    1000,        # Q1
    2000,        # Q2
    3000,        # Q3
    5000,        # Q4
    10000,       # Q5
    20000,       # Q6
    40000,       # Q7
    80000,       # Q8
    160000,      # Q9
    320000,      # Q10
    640000,      # Q11
    1250000,     # Q12
    2500000,     # Q13
    5000000,     # Q14
    10000000,    # Q15
    30000000,    # Q16
    50000000,    # Q17
    70000000,    # Q18
    90000000,    # Q19
    100000000    # Q20 (₹1 Crore 💰)
]

prize=0
s=input("Please enter your name :")
print("welcome",s,"To KBC")
for i in range 20:
    print(questions[i])
