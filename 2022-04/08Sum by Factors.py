def sum_for_list(lst):
    
    for number in lst:
        if number<0: number=-number
        factors = [divider for divider in range(number+1) if divider and number%divider==0]
    return factors
print(sum_for_list([15, 30]))