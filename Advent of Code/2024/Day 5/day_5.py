
## Time Complexity: O(mn)
## Space Complexity: O(mn)
def part_1(inp):
	# Parse input in the form of 2D grid
	grid = []
	x, y = 0, 0
	row_num = 0
	# Get the initial position of the guard
	for row in inp:
		for col_num in range(len(row)):
			if row[col_num] == '^':
				x, y = row_num, col_num
		grid.append(row.strip())
		row_num += 1

	# Traverse the guard's route
	positions = set()
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	i = 0
	while x in range(len(grid[0])) and y in range(len(grid)):
		# Update direction for guard after meeting obstacle
		if grid[x][y] == "#":
			 initial_direction = directions[i]
			 x , y = x - initial_direction[0], y - initial_direction[1]
			 i = (i + 1) % len(directions)
			 new_direction = directions[i]
			 x, y = x + new_direction[0], y + new_direction[1]
		# Otherwise continue in the same direction
		else:
			positions.add((x, y))
			current_direction = directions[i]
			x, y = x + current_direction[0], y + current_direction[1]
	return len(positions)


if __name__ == '__main__':
	with open('day_5.txt') as file:
		inp = file.readlines()
		print(f'Number of distinct positions visited by the guard: {part_1(inp)}')