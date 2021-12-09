# Task:
# The input given to the console would for example be:
# aaabbcccccdee
# The code should output the repeating characters with an digit index
# for how many encounters of the given char there were in the input, for example the
# above input should result in the following:
# 3a2b5c1d2e

def StringChallenge(strParam):

  encounter_counter = 0 
  encounterlist = list(strParam)
  print(encounterlist)
  encounterlistnew = []
  finalstring = ''
  lettercount = 0
  for x in encounterlist:
    lettercount = encounterlist.count(x)
    print(lettercount)
    encounterlistnew.append(str(lettercount) + x)
    print(encounterlistnew)
    for y in encounterlist:
      if y == x:
        encounterlist.remove(y)
  finalstring = ''.join(encounterlistnew)
  print(finalstring)  
  strParam = finalstring
  return strParam


print(StringChallenge(input()))