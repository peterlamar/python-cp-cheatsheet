def quickSort(array):
	def partition(arr, s, e):
		i = s - 1
		pivot = arr[e]
		
        print("pivot ", pivot, end=" ")
		for j in range(s, e):
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		
		arr[i+1], arr[e] = arr[e], arr[i+1]
		return i+1
		
		
	def helper(arr, s, e):
		if len(arr) == 1:
			return arr
		if s < e:
			print(arr)
			pi = partition(arr, s, e)
			print(arr)

			helper(arr, s, pi -1)
			helper(arr, pi+1, e)

	helper(array, 0, len(array)-1)
	
	return array


def quickSort(array):
	def partition(arr, s, e):
		i = s - 1
		pivot = arr[e]
		
        print("pivot ", pivot)
		for j in range(s, e):
			print("arrj ", arr[j])
			if arr[j] <= pivot:
				print("arr[j] <= pivot ", arr[j] <= pivot)
				i += 1
				print(i)

				arr[i], arr[j] = arr[j], arr[i]
		print(arr)

		arr[i+1], arr[e] = arr[e], arr[i+1]
		return i+1
		
		
	def helper(arr, s, e):
		if len(arr) == 1:
			return arr
		if s < e:
			print(arr)
			print("start ", s)
			pi = partition(arr, s, e)
			print(arr)

			helper(arr, s, pi -1)
			helper(arr, pi+1, e)

	helper(array, 0, len(array)-1)
	
	return array