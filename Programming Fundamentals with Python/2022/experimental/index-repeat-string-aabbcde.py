# aabbcde - test string
userinput = input()

def StringChallenge(strParam):

  # code goes here
  encounter_counter = 0 
  encounterlist = list(strParam)
  encounterlistnew = []
  finalstring = ''
  lettercount = 0
  for x in encounterlist:
    lettercount = encounterlist.count(x)
    encounterlistnew.append(str(lettercount) + x)
    for y in encounterlist:
      if y == x:
        encounterlist.remove(y)
  finalstring = ''.join(encounterlistnew)  
  strParam = finalstring
  return strParam

# keep this function call here 
print(StringChallenge(userinput))
