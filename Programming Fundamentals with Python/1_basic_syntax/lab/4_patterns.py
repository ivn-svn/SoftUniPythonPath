# A solution by Yordan Jambazov
desired_size = int(input())
direction = 1
current_size = 0
#
while current_size < desired_size or direction == -1:
    current_size += direction
    row = '*' * current_size
    if row:
        print(row)
    else:
        break
    if desired_size == current_size:
        direction = -1
# Makes the pyramid grow one-sided.



    # PDB - a python built-in module. E.g.
    # breakpoint()
    # /\ used to debug Python code. It could be put in the middle of the code.