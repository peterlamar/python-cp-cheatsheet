def quickSort(array):
	def sort(array, l, r):
		if l < r:
			p = partition(array, l, r)
			sort(array, p+1, r)
			sort(array, l, p-1)

	def partition(array, l, r):
		pivot = array[r]
		a = l
		for i in range(l, r):
			if (array[i] < pivot):
				array[a], array[i] = array[i], array[a]
				a += 1
		array[a], array[r] = array[r], array[a]                
		return a
	
    sort(array, 0, len(array)-1)
    return array

"""
initial array: [8, 5, 2, 9, 5, 6, 3]: 
pivot = 3 [2, 3, 8, 9, 5, 6, 5]
pivot = 5 [2, 3, 5, 9, 5, 6, 8]
pivot = 8 [2, 3, 5, 5, 6, 8, 9]
pivot = 6 [2, 3, 5, 5, 6, 8, 9]
"""

def quickSort(array):
	
	def sort(arr, l, r):
		if l < r:
			p = part(arr, l, r)
			sort(arr, l, p-1)
			sort(arr, p+1, r)
	
	def part(arr, l, r):
		pivot = arr[r]
		a = l
		for i in range(l,r):
			if arr[i] < pivot:
				arr[i], arr[a] = arr[a], arr[i]
				a += 1
		arr[r], arr[a] = arr[a], arr[r]
		return a
	
	sort(array, 0, len(array)-1)
	
	return array