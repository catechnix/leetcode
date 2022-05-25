from xml.dom import minidom


def find_num(ls):
    nums={}
    mid_point = len(ls)//2
    print ("mid_point", mid_point)

    for n in ls:
        print(ls)
        i=0
        count = 0

        while i <= len(ls)-1:
            if n == ls[i]:
                count +=1
            i +=1
        nums[n]=count

    print ("dict is ", nums)
    for key, value in nums.items():
        if value >= mid_point:
            print(key)

find_num([1,2,3,3,4,3,5])


