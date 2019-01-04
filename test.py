def print_arr(lst):
    for a in lst:
        print a, "*"


arr = [
    "this is the first line   ",
    "        this is the second",
    "",
    "The above line is blank, let's remove it",
    "  ",
    "This should be the last line    ",
    """  
     
        
        """,
]
dic =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(dic)

# for d in dic:
#         print d, ":", dic[d]

# print '*'

arr = []
for i in range(5):
        d = {"a":i, "b":"i"}
        arr.append(d)
        # arr.append(dict(a=i, b="i"))

# print_arr(arr)

for i in range(3):
        keys = ["req", "cho_sin", "cho_mul", "short", "ans"]
        keys = [k + str(i) for k in keys]
        # print_arr(keys)
        # print 