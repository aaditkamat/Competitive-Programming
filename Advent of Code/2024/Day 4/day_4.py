import re
import functools

##
# Preconditions:
# 1. The lists have odd lengths and hence you can locate a middle number 
## 
def part_1(inp):
	hash_map = {}
	res = 0

	def check_all_pairs():
		all_nums = list(set(list(hash_map.keys()) + list(hash_map.values())))
		for i in range(len(all_nums)):
			for j in range(i + 1, len(all_nums)):
				if (all_nums[i] in hash_map and hash_map[all_nums[i]] != all_nums[j]) and (all_nums[j] in hash_map and hash_map[all_nums[j]] != all_nums[i]):
					print(all_nums[i], all_nums[j])
					return False
		return True


	for line in inp:
		match = re.search(r'(\d+)\|(\d+)', line)
		if match:
		  key, val = int(match.group(1)), int(match.group(2))
		  if key in hash_map:
		  	hash_map[key].append(val)
		  else:
		  	hash_map[key] = [val]

		elif line == '\n':
			continue
		else:
			lst = [int(x) for x in line.split(',')]
			sorted_lst = sorted(lst, key=lambda num: len(hash_map[num]) if num in hash_map else 0, reverse=True)
			if sorted_lst == lst:
				res += sorted_lst[len(sorted_lst) // 2]

	# check_all_pairs()

	return res


if __name__ == '__main__':
	with open('day_4.txt') as file:
		inp = file.readlines()
		print(f'Adding up all the middle page number from those correctly-ordered updates you get: {part_1(inp)}')