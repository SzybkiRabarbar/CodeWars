'''
https://www.codewars.com/kata/515bb423de843ea99400000a/python
'''
class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        temp=[]
        content=[]
        for i,c in enumerate(collection):
            temp.append(c)
            if len(temp)==items_per_page or len(collection)==i+1:
                content.append(temp)
                temp=[]
        self.content=content
  
  # returns the number of items within the entire collection
    def item_count(self):
        return sum([len(content) for content in self.content])
  
  # returns the number of pages
    def page_count(self):
        return len(self.content)
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        try:    
            return len(self.content[page_index])
        except IndexError:
            return -1
        
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        last_item=self.item_count()-1
        if item_index>last_item or item_index<0: return -1
        pages_len=self.page_item_count(0)
        return (item_index//pages_len)

  