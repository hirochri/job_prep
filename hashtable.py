'''
Used to store key/value pairs


Time Search/Insert/Delete O(1) avg/best, O(n) worst
Space O(n)

Upon reaching load factor (2/3) for python, increase 
size and rehash elements

Alternative to full rehash: During resize allocate new table, keep old 
table around. Check both tables on lookup/delete, but only insert into
new table. At each insertion move r elements from old to new, deallocate 
old table once all elements are removed. For old table to completely be copied
over before new table is in need of resizing, the table must
be increased by a factor of at least (r+1)/r

Hash function maps data of arbitrary size to fixed size
Should be easy to compute, have uniform distribution and less collisions

Collision resolution can be done with 
* Separate chaining (linked lists at each bucket, nodes have key/val pairs)
* Linear probing (all pairs store in array, keep going linearly in array until empty slot or key found)
* Quadratic probing (same idea, but quadratic jumps each time (i + x^2))
* Double hashing (probing also, but with a function to compute jumps)

'''
class HashTable():

  def __init__(self):
    self.hashtable = [[] for _ in range(256)]


  def insert(self, key, value):
    hashed_key = hash(key) % len(self.hashtable)

    for i, pair in enumerate(self.hashtable[hashed_key]):
      k, v = pair

      if key == k:
        self.hashtable[hashed_key][i] = ((key, value))
        break
    else:
      self.hashtable[hashed_key].append((key, value))


  def get(self, key):
    hashed_key = hash(key) % len(self.hashtable)

    for i, pair in enumerate(self.hashtable[hashed_key]):
      k, v = pair

      if key == k:
        return v
    else:
      print('KeyError')

