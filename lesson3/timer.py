"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.time() - self.start_time
        print(f"Время выполнения: {self.elapsed_time:.6f} секунд")


with Timer() as timer:
    # блок кода
    _ = [i for i in range(1000000)]  # пример вычислений
    
    # код для проверки 
    print("Execution time:", timer.elapsed_time)
