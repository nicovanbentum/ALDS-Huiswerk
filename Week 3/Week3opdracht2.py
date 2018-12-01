class ListNode:
   def __init__(self,data,next_node):
      self.data = data
      self.next = next_node

   def __repr__(self):
      return str(self.data)

class circularLinkedList:
   def __init__(self):
      self.tail = None # represents the tail in the returned string

   def __repr__(self):
      s = ''
      current = self.tail
      while current.next != self.tail:
         s = s + " -> " + str(current)
         current = current.next
      s = s + " -> " + str(current)

      if not s: # s == '':
         s = 'empty list'
      return s

   def append(self, n):
      if self.tail == None:
         self.tail = ListNode(n, None)
         self.tail.next = self.tail
      else:
         it_node = self.tail
         while it_node.next != self.tail:
            it_node = it_node.next
         it_node.next = ListNode(n, self.tail)

   def get(self, e):
      if self.tail == None:
         return None
      it_node = self.tail
      while it_node.next != self.tail:
         if it_node.data == e:
            return it_node
         else:
            it_node = it_node.next

      if it_node.data is not e:
         return None
      else:
         return it_node

   def delete(self, n):
      if self.tail.next == None:
         return

      #there's no other option than to just start at the tail and iterate until 
      # you find the item you want to delete which is O(n).
      #assignments says to check the last item first which doesn't make sense since 
      # getting to the last element is O(n) anyway.
      it = self.tail
      previous_it = None
      while it.next != self.tail:
         previous_it = it
         it = it.next
         if it.data == n:
            it_after = it.next
            previous_it.next = it_after

mcl = circularLinkedList()
mcl.append(5)
mcl.append(9)
mcl.append(7)
mcl.append(1)

print(mcl)

mcl.delete(9)

print(mcl)

last_node = mcl.get(1)
print(last_node.next) #test if circular



