it = iter("string")
for i in it:
    print i

testIt = iter([1, 2, 3, 4, 5]) 
print [x for x in testIt] 


def getSimple(state=[]): 
  if len(state) < 4: 
    state.append(" ") 
    return " " 

testIt2 = iter(getSimple, None) 
print [x for x in testIt2] 