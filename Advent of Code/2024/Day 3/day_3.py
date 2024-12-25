import re

## 
# 1) Identify all the tokens of the form mul(X, Y) where X, Y are numbers using regex.
# 2) Parse the captured groups corresponding to X and Y into their integer forms before multiplying
# 3) Sum all the numbers obtained by multiplication within the list using in built sum function
##
def part_1(inp):
	regex = r'mul\((\d+)\,(\d+)\)'
	matches = re.findall(regex, inp)
	return sum([int(x) * int(y) for x, y in matches])

## 
# 1) Find all the do's() and dont's() in addition to mul(X, Y) tokens
# 2) Instead of doing list comprehension, loop over the tokens and store state corresponding to do and don't
# 3) Sum up the numbers when do state is activated and return the result
##
def part_2(inp):
	regex = r'(do\(\))|(don\'t\(\))|(mul\((\d+)\,(\d+)\))'
	matches = re.findall(regex, inp)
	filtered_matches = [tuple([x for x in tup if x != '']) for tup in matches]
	do_state = True
	res = 0
	for group in filtered_matches:
		token = group[0]
		if token == 'do()':
			do_state = True
		elif token == 'don\'t()':
			do_state = False
		elif do_state:
			x, y = group[-2], group[-1]
			res += int(x) * int(y)
	return res

if __name__ == '__main__':
	with open('day_3.txt') as file:
		inp = file.read()
		res = part_1(inp)
		print(f'Adding up all of the results gets you: {part_1(inp)}')
		print(f'Adding up all of the results after accounting for the custom instructions is: {part_2(inp)}')