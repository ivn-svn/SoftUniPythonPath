# This problem takes its name from arguably the most important event in the life of the ancient historian Josephus.
# According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.
# Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and
# proceeded to kill one man of every three until one last man was left (and that it was supposed to kill himself to
# end the act). Well, Josephus and another man were the last,
# and, as we now know every detail of the story, you may have correctly guessed that they did not precisely follow
# through with the original idea.

# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
#     • the list itself - numbers separated by a single space representing the people in the circle
#     • a number k
# People are standing in a circle waiting to be executed. Counting begins from the first
# one in the circle and proceeds from left to right. After a specified number of people are skipped,
# the k person is executed.
# The procedure is repeated with the remaining people, starting with the next person, going in the same direction,
# and skipping the same number of people until no one remains.
#
#
soldiers_list = input().split(" ")                                              # building a list from the input string
final_soldiers_list = soldiers_list                                             # the output list
k = int(input())  # After a specified number of people are skipped, the k person is executed *** Not sure what K is yet.
# Where is that specified?
death_soldiers_list = []
while len(final_soldiers_list) > 1:
    for soldier_idx in range(0, len(soldiers_list) -1):      # iterating soldiers_list received with a soldier_idx
        if soldier_idx % k == 0:
            final_soldiers_list.remove(soldiers_list[soldier_idx])
            death_soldiers_list.append(soldiers_list[soldier_idx])
        print(death_soldiers_list)
print(final_soldiers_list)