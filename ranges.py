"ranges"
myrange = range(5)  # range ---> (0,10)

print(myrange) #iterable object ---> You loop over it to get the value
for i in myrange:
    print(i)
""" you can cast the range object to be a list """

# myrange = list(myrange)
# print(myrange)

"""
    range object ===> start=0, stop=5 , step= 1 
        [0,1,2,3,4]
        
        start < stop 
        
        "generate values from the start to the stop-step 
"""

"""to customize the range object """
# myr = range(1, 11, 1)
# myr = list(myr)
# print(myr)

# myr = range(1, 11, 2)
# myr = list(myr)
# print(myr)

##########################
"start > stop --> step= -1"

nums = range(10, 0, -1)  # stop value --> stop -  step ===> 0 -(-1) = 1
nums= list(nums)
print(nums)

###########################
"write a program to ask the user to fill a list with 5 items"

# mylist = []
# for i in range(5):
#     val = input(f"please enter value at index {i} : ")
#     mylist.append(val)
#
# print(mylist)



rr = range(4)
ll  =[]
for i in rr:
    value = input(f"please enter value {i}")
    ll.append(value)
print(ll)