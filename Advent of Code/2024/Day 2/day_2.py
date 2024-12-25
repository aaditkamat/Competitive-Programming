## To solve this problem, you need to:
## 1) Return safe for a report if its length is 1 or less
## 2) For each report with length greater than 2, determine the difference between
## the first two levels to gauge the direction of change (increase or decrease).
## If the difference is not within range 1 to 3 (in absolute), the report is unsafe.
## Then, determine the difference between the subsequent pairs of reports.
## If these differences are not within range 1 to 3 or in a direction that's different
## from the first difference, the report is unsafe.
## 3) Sum up all the reports that are safe across the input and return the result
## Time Complexity: O(mn) -> where m is the number of reports and n is the number of levels
## Space Complexity: O(mn) -> store the reports as a 2 dimensional matrix (list) 

def part_1(reports):
	# 3)
	num_safe = 0
	for report in reports:
		# 1)
		if len(report) <= 1:
			num_safe += 1
			break
		# 2)
		is_safe = True
		for i in range(1, len(report)):
			diff = report[i] - report[i - 1]
			if i == 1:
				first_diff = diff
			if abs(diff) not in range(1, 4) or ((diff > 0 and first_diff < 0) or (diff < 0 and first_diff > 0)):
			   is_safe = False
			   break
		if is_safe:
			num_safe += 1
	return num_safe

if __name__ == '__main__':
	with open('day_2.txt') as file:
		reports = []
		for line in file.readlines():
			reports.append([int(level_str) for level_str in line.strip().split()])
		print(f'Number of safe reports is: {part_1(reports)}')
		# print(f'Number of safe reports after Problem Dampener is: {part_2(reports)}')