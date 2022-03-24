'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

'''
def snail(snail_map):
    content = []
    while True:
        snail_map = [x for x in snail_map if x]
        if len(snail_map) >= 3:   
            n = len(snail_map)
            for lis in range(n):
                content.append(snail_map[0].pop(0))
            for lis in range(n-1):
                content.append(snail_map[lis+1].pop(n-1))
            for lis in range(n-1):
                content.append(snail_map[n-1].pop(n-2-lis))
            for lis in range(n-2):
                content.append(snail_map[n-2-lis].pop(0))
        elif len(snail_map) == 2:
            content.append(snail_map[0][0])
            content.append(snail_map[0][1])
            content.append(snail_map[1][1])
            content.append(snail_map[1][0])
            return content
        elif len(snail_map) == 1:
            content.append(snail_map[0][0])
            return content
        else:
            return content

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))
