'''
https://www.codewars.com/kata/520446778469526ec0000001/python
'''
def same_structure_as(original,other):
    for i in range(len(original)):
        try:
            if type(original[i])==list or type(other[i])==list:
                break
            else:
                if i+1==len(original) and len(original)==len(other): return True
        except IndexError:
            break
    original_str=str(original)
    other_str=str(other)
    original_structure, other_structure=str(), str()
    for letter in original_str:
        if letter=='[' or letter==']' or letter==',':
            original_structure+=letter
    for letter in other_str:
        if letter=='[' or letter==']' or letter==',':
            other_structure+=letter
    if original_structure==other_structure:
        return True
    else:
        return False

print(same_structure_as([1,'[',']'], ['[',']',1]))