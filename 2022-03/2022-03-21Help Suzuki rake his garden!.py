'''
https://www.codewars.com/kata/571c1e847beb0a8f8900153d/python
Help Suzuki rake his garden!

The monastery has a magnificent Zen garden made of white gravel and rocks and it is raked diligently everyday by the monks. 
Suzuki having a keen eye is always on the lookout for anything creeping into the garden that must be removed during the daily raking such as insects or moss. 
'''
def rake_garden(garden):
    return ' '.join([obj if obj == 'gravel' or obj == 'rock' else 'gravel' for obj in garden.split()])


garden1 = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
print(rake_garden(garden1))
