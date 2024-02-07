import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import sys
from io import StringIO

class PythonInterpreter:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Interpreter")
        self.setup_ui()

    def setup_ui(self):
        # Устанавливаем темную тему
        self.root.configure(bg="#212121")

        # Текстовое поле для ввода кода
        self.code_textbox = scrolledtext.ScrolledText(self.root, height=15, width=50, bg="#424242", fg="white")
        self.code_textbox.pack(pady=10)

        # Кнопка "Run" для выполнения кода
        self.run_button = tk.Button(self.root, text="Run", command=self.execute_code, bg="#616161", fg="white")
        self.run_button.pack()

        # Консоль для вывода результатов выполнения
        self.output_console = scrolledtext.ScrolledText(self.root, height=15, width=50, bg="#424242", fg="white")
        self.output_console.pack(pady=10)

    def execute_code(self):
        # Получаем код из текстового поля
        code = self.code_textbox.get("1.0", tk.END)
        # Выполняем код и выводим результат в консоль
        output = self.run_code(code)
        self.output_console.delete("1.0", tk.END)
        self.output_console.insert(tk.END, output)

    def run_code(self, code):
        # Перенаправляем вывод stdout для получения результатов выполнения кода
        sys.stdout = StringIO()
        try:
            # Выполняем код
            exec(code)
        except Exception as e:
            # Если возникает ошибка, выводим ее сообщение
            output = str(e)
        else:
            # В случае успешного выполнения кода, получаем вывод
            output = sys.stdout.getvalue()
        finally:
            # Возвращаем stdout в исходное состояние
            sys.stdout = sys.__stdout__
        return output

# Создаем главное окно
root = tk.Tk()
app = PythonInterpreter(root)
root.mainloop()
