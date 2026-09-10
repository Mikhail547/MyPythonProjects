### Реализация Быстрой сортировки на Python (в олимпиадном стиле):
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай рекурсии: массив из 1 элемента уже отсортирован
    
    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (в середине)
    
    # Распределяем элементы по трем массивам (List Comprehension)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Рекурсивно сортируем лево и право, склеиваем результат
    return quicksort(left) + middle + quicksort(right)
```
