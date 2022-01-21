# Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves who pretend to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.

# user_input = ""


user_input = input().split(", ")

n = len(user_input)

for i in (range(n)):


    if list[n-1] == "wolf" :
        print("Please go away and stop eating my sheep")
        break
    elif user_input[i]=="wolf" :
        print(f"Oi! Sheep number {n-i-1}! You are about to be eaten by a wolf!")
        break