def calc_1(test, acc, nums):
	if len(nums) == 0:
		return test == acc
	if acc == 0:
	   return calc_1(test, nums[0] * nums[1], nums[2: ]) \
	   or calc_1(test, nums[0] + nums[1], nums[2: ])
	else:
	   return calc_1(test, acc + nums[0], nums[1: ]) \
	   or calc_1(test, acc * nums[0], nums[1: ]) \

def concat(num1, num2):
	return int(str(num1) + str(num2))

def calc_2(test, acc, nums):
	if len(nums) == 0:
		return test == acc
	if acc == 0:
	   return calc_2(test, nums[0] * nums[1], nums[2: ]) \
	   or calc_2(test, nums[0] + nums[1], nums[2: ]) \
	   or calc_2(test, concat(nums[0], nums[1]), nums[2: ])
	else:
	   return calc_2(test, acc + nums[0], nums[1: ]) \
	   or calc_2(test, acc * nums[0], nums[1: ]) \
	   or calc_2(test, concat(acc, nums[0]), nums[1: ])

def part_1(inp):
	res = 0
	for row in inp:
		tokens = row.strip().split(' ')
		test = int(tokens[0].strip(':'))
		nums = [int(x) for x in tokens[1: ]]
		if calc_1(test, 0, nums):
			res += test
	return res

def part_2(inp):
	res = 0
	for row in inp:
		tokens = row.strip().split(' ')
		test = int(tokens[0].strip(':'))
		nums = [int(x) for x in tokens[1: ]]
		if calc_2(test, 0, nums):
			res += test
	return res

if __name__ == '__main__':
	with open('day_6.txt') as file:
		inp = file.readlines()
		print(f'Total calibration result: {part_1(inp)}')
		print(f'Total calibration result after adding concat operation: {part_2(inp)}')