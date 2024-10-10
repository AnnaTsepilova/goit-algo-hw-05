def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо елемент не знайдений, верхньою межею є arr[left], якщо left не виходить за межі масиву
    if left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Тестуємо функцію:
arr = [1.2, 2.3, 3.5, 4.6, 5.7, 6.8, 7.9]
target = 4.0
result = binary_search(arr, target)
print(result)  # Виведе (кількість ітерацій, верхня межа)
