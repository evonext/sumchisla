import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Функция для вычисления суммы цифр числа с использованием цикла for
def sum_digits_for(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits

# Функция для вычисления суммы цифр числа с использованием цикла while
def sum_digits_while(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits

# Функция для обработки нажатия кнопки
def calculate_sum():
    try:
        number = int(entry_number.get())
        cycle_type = combo_cycle.get()
        if cycle_type == 'for':
            result = sum_digits_for(number)
        elif cycle_type == 'while':
            result = sum_digits_while(number)
        else:
            raise ValueError("Invalid cycle type selected")
        
        label_result.config(text=f"Сумма цифр: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное целое число.")

# Создание главного окна
root = tk.Tk()
root.title("Сумма цифр числа")
root.geometry("300x200")

# Виджет для ввода числа
label_number = tk.Label(root, text="Введите целое число:")
label_number.pack(pady=5)
entry_number = tk.Entry(root)
entry_number.pack(pady=5)

# Виджет Combobox для выбора типа цикла
label_cycle = tk.Label(root, text="Выберите тип цикла:")
label_cycle.pack(pady=5)
combo_cycle = ttk.Combobox(root, values=["for", "while"])
combo_cycle.set("for")  # Установить значение по умолчанию
combo_cycle.pack(pady=5)

# Кнопка для вычисления суммы цифр
button_calculate = tk.Button(root, text="Вычислить", command=calculate_sum)
button_calculate.pack(pady=10)

# Метка для отображения результата
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# Запуск главного цикла обработки событий
root.mainloop()
