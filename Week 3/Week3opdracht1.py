def check(a,i):  # ga na of i aan a toegevoegd kan worden
   n = len(a)
   return not (i in a or
                # niet in dezelfde kolom 
               i+n in [a[j]+j for j in range(n)] or
                # niet op dezelfde diagonaal 
               i-n in [a[j]-j for j in range(n)]) 
                # niet op dezelfde diagonaal

def printQueens(a):
   n = len(a)
   for i in range(n):
      for j in range(n):
         if a[i] == j:
            print("X",end= " ")
         else:
            print("*",end= " ")
      print()
   print()

def rsearch(N):
   global a
   global b

   if len(a) == N: # geschikte a gevonden
      b.append(a.copy())
      return True

   z = False
   for i in range(N):
      if check(a,i):
         a.append(i)
         z = rsearch(N) or z
         a.pop() # verwijder laatste element
   return z


a = [] # a geeft voor iedere rij de kolompositie aan
b = [] # bevat gevonden a's
rsearch(8)
print(a)
print(b)
printQueens(a)
print(len(b))