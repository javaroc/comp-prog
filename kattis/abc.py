nums = sorted(list(map(int, input().split())))
order = input().strip()
for c in order[:-1]:
	print(nums[ord(c) - ord('A')], end=' ')
print(nums[ord(order[-1]) - ord('A')])
