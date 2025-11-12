# Реалізація сортування методом бульбашки
def bubble_sort(arr):
    """
    Функція для сортування списку у порядку зростання методом бульбашки
    """
    n = len(arr)
    
    # Проходимо через всі елементи списку
    for i in range(n):
        # Останні i елементів вже на своїх місцях
        for j in range(0, n - i - 1):
            # Порівнюємо сусідні елементи
            if arr[j] > arr[j + 1]:
                # Міняємо місцями, якщо елемент більший за наступний
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Демонстрація сортування
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Початковий список:", numbers)

sorted_numbers = bubble_sort(numbers.copy())
print("Відсортований список:", sorted_numbers)

# Демонстрація використання in та not in
print("\n--- Демонстрація конструкцій in та not in ---")

# Приклад зі списком
my_list = [1, 2, 3, 4, 5]

# Перевірка наявності елемента за допомогою in
if 3 in my_list:
    print("Елемент 3 знайдено у списку.")

# Перевірка відсутності елемента за допомогою not in
if 6 not in my_list:
    print("Елемент 6 відсутній у списку.")

# Приклад з рядком
my_string = "Hello, world!"

# Перевірка наявності підрядка
if "world" in my_string:
    print("Слово 'world' знайдено у рядку.")

# Перевірка відсутності символу
if "x" not in my_string:
    print("Літера 'x' відсутня у рядку.")

# Практичне використання in/not in з відсортованим списком
print("\n--- Практичне використання з відсортованим списком ---")

fruits = ["яблуко", "банан", "апельсин", "киві", "груша"]
print("Список фруктів:", fruits)

# Сортуємо список
sorted_fruits = bubble_sort(fruits.copy())
print("Відсортовані фрукти:", sorted_fruits)

# Перевіряємо наявність конкретних фруктів
search_fruits = ["яблуко", "манго", "апельсин"]

for fruit in search_fruits:
    if fruit in sorted_fruits:
        print(f"Фрукт '{fruit}' є у списку")
    else:
        print(f"Фрукт '{fruit}' відсутній у списку")

# Оптимізована версія бульбашкового сортування
def optimized_bubble_sort(arr):
    """
    Оптимізована версія бульбашкового сортування
    з перевіркою на вже відсортований список
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False  # Прапорець для перевірки обмінів
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Якщо не було жодного обміну, список вже відсортований
        if not swapped:
            break
    
    return arr

print("\n--- Оптимізоване сортування ---")
test_list = [5, 1, 4, 2, 8]
print("Тестовий список:", test_list)
print("Відсортований список:", optimized_bubble_sort(test_list.copy()))