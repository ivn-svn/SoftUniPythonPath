nums = input().split(' ')
n, m = int(nums[0]), int(nums[1])
n_set = set()
m_set = set()
for num_lines in range(0, n):
    n_add = input()
    n_set.add(n_add)
for num_lines in range(0, m):
    m_add = input()
    m_set.add(m_add)

for item in m_set:
    if item in n_set:
        print(item, end='\n')