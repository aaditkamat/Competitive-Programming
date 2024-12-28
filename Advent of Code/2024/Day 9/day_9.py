
def part_1(inp):
	hash_map = {}
	start_id = 0
	for char in inp[: : 2]:
		hash_map[start_id] = int(char)
		start_id += 1
	
	min_val = 0
	max_val= len(hash_map) - 1
	res = 0
	curr_idx = 0
	filled_vals = False
	total_values = sum(hash_map.values())

	for i in range(len(inp)):
		is_free = (i % 2 == 1)

		for j in range(int(inp[i])):
			if not is_free:
				res += (min_val * (curr_idx + j))
			else:
				if hash_map[max_val] == 0:
					max_val -= 1
				if curr_idx + j == total_values - 1:
					filled_vals = True
					break
				res += (max_val * (curr_idx + j))
				hash_map[max_val] -= 1

			if curr_idx + j == total_values - 1:
				filled_vals = True
				break

		if filled_vals:
			break

		if is_free:
			min_val += 1

		curr_idx += (j + 1)

	return res




if __name__ == '__main__':
	with open('day_9.txt') as file:
		inp = file.read()
		print(f'The resulting file checksum is: {part_1(inp)}')