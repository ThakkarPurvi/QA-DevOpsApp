""" create a function to find sum of the input """
def no_sum():
   no = list(map(int, input().split()))
   print(no)
   res = 0
   for i in no:
       res = res + i
   print(res)
no_sum()

""" create a function to find product of the input """
def no_product():
    no = list(map(int, input().split()))
    print(no)
    res = 1
    for i in no:
        res = res * int(i)
    print(int(res))
no_product()
