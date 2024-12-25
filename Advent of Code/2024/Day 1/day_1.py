import requests
from collections import Counter

## To find the distance between the two lists, you need to:
## 1. If the length of the lists are different, return 0
## 2. Sort both lists in ascending order
## 3. Sum up the differences between the numbers in respective pairs
## Time Complexity: O(n log n) -> Sorting
## Space Complexity: O(n) -> Storing the lists
def part_1(left_lst, right_lst):
	# 1)
	if len(left_lst) != len(right_lst):
		return 0
	# 2)
	sorted_left_lst = sorted(left_lst)
	sorted_right_lst = sorted(right_lst)

	# 3)
	res = sum([abs(sorted_left_lst[i] - sorted_right_lst[i]) for i in range(len(left_lst))])

	return res

## To find the similarity score, you need to:
## 1. Create a hash map with each number in the right list paired to its count
## 2. Iterate through the left list and add up the multiple of each number to its count on the hash map (if it exists otherwise 0)
## Time Complexity: O(n) -> for creating the hash and iterating through the left list, searching takes O(1) time
## Space Complexity: O(n) -> Storing the lists and the hash map
def part_2(left_lst, right_lst):
	# 1)
	hash_map = Counter(right_lst)
	# 2)
	res = sum([num * hash_map[num] for num in left_lst])
	return res

if __name__ == '__main__':
	with open('day_1.txt') as file:
		left_lst, right_lst = [], []
		for line in file.readlines():
			left, right = [int(x) for x in line.strip().split()]
			# Integer on the left is added to the left list
			left_lst.append(int(left))
			# Integer on the right is added to the right list
			right_lst.append(int(right))
		print(f'Total distance between the lists is: {part_1(left_lst, right_lst)}')
		print(f'Similarity score is: {part_2(left_lst, right_lst)}')