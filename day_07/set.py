# syntax
st = set()
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# or using this : print(fruits | vegetables)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
