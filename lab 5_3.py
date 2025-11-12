students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 90, None, 75]

# Виведення пар ім'я-бал для кожного студента
for i in range(len(students)):
    student = students[i]
    
    # Перевіряємо, чи є бал для поточного студента
    if i < len(scores) and scores[i] is not None:
        score = scores[i]
        print(f"{student} - {score}")
    else:
        print(f"{student} - No score available")