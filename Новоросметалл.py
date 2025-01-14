import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from tkinter import ttk
import random

class MyApp:
 def __init__(self, root):
self.root = root         
root.iconbitmap(default="logo.ico")
self.root.title("PCS-NOVOMET")
self.root.geometry("1280x720")  # Начальный размер окна
self.root.resizable(True, True)  # Разрешить изменение размера окна

# Создание меню
self.menu = tk.Menu(self.root)
self.root.config(menu=self.menu)
self.menu.add_command(label="Закупки", command=self.open_purchases)
self.menu.add_command(label="Продукция", command=self.open_products)
self.menu.add_command(label="Логистика", command=self.open_logistics)
self.menu.add_command(label="Производство", command=self.open_production)
self.menu.add_command(label="Отчёты", command=self.open_reports)
self.menu.add_command(label="Поставщики", command=self.open_suppliers)
self.menu.add_command(label="Продажи", command=self.open_sales)

# Основной фрейм для контента
self.main_frame = tk.Frame(self.root)
self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Фрейм для технических показателей
self.tech_frame = tk.Frame(self.main_frame, bd=1, relief=tk.RAISED)
self.tech_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Заголовок для технических показателей
tech_title = tk.Label(self.tech_frame, text="Технические показатели", font=("Arial", 16, "bold"))
tech_title.pack(pady=10)

# Создание таблиц для технических показателей
self.create_technical_tables()

# Фрейм для статус-баров
self.status_frame = tk.Frame(self.main_frame)
self.status_frame.pack(side=tk.TOP, fill=tk.X)

# Создание статус-баров для каждого цеха
self.status_labels = []
self.progress_vars = []

 for i in range(8):
status_bar = tk.Frame(self.status_frame, bd=1, relief=tk.SUNKEN)
status_bar.pack(side=tk.TOP, fill=tk.X, pady=2)

status_label = tk.Label(status_bar, text=f"Цех {i + 1}: Загруженность: 0%", bd=1, anchor='w')
status_label.pack(side=tk.LEFT, padx=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(status_bar, variable=progress_var, maximum=100)
progress_bar.pack(side=tk.RIGHT, fill=tk.X, padx=5)

self.status_labels.append(status_label)
self.progress_vars.append(progress_var)

# Фрейм для новостей
self.news_frame = tk.Frame(self.root, bg="lightgrey", bd=1)
self.news_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10))
self.news_frame.config(width=int(0.15 * 1280))

# Заголовок для новостей
self.news_title = tk.Label(self.news_frame, text="Последние новости", bg="lightgrey", font=("Arial", 16, "bold"))
self.news_title.pack(pady=10)

# Пример новостей
self.news_blocks = [
f"Успешно завершено производство новой партии катанки и арматуры. Все изделия прошли контроль качества.",
f"Ввод в экспуатацию нового цеха по производству стальных заготовок.",
f"Было закулено 100 единиц новой техники.",
f"Открытие нового благотворительного фонда Небо на ладони.Его создатели - люди со стальным характером и доброй душой",
f"Проведено обучение сотрудников по новым технологиям производства.",
f"Подписан контракт на поставку сырья с новым поставщиком.",
]

for i, news in enumerate(self.news_blocks):
news_block = tk.Frame(self.news_frame, bd=1, relief=tk.SUNKEN)
news_block.pack(pady=5, padx=5, fill=tk.X)

news_label = tk.Label(news_block, text=news, anchor='w', padx=10, pady=5, wraplength=int(0.15 * 1280))
news_label.pack(side=tk.LEFT, fill=tk.BOTH)

news_date = (datetime.now() - timedelta(days=i + 1)).strftime('%Y-%m-%d')
date_label = tk.Label(news_block, text=news_date, fg="grey", anchor='e', padx=10, pady=5)
date_label.pack(side=tk.RIGHT)

# Запуск обновления статус-баров
self.update_status_bars()

def create_technical_tables(self):
# Фрейм для производственных показателей
prod_frame = tk.LabelFrame(self.tech_frame, text="Производственные показатели", font=("Arial", 12, "bold"))
prod_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Создание таблицы для производственных показателей
self.prod_tree = ttk.Treeview(prod_frame, columns=("Показатель", "Значение"), show='headings')
self.prod_tree.heading("Показатель", text="Показатель")
self.prod_tree.heading("Значение", text="Значение")
self.prod_tree.pack(fill=tk.BOTH, expand=True)

# Добавление производственных показателей
prod_data = [
("Производительность", "4500 единиц/день"),
("Уровень брака", "2%"),
("Количество заказов в день", "100"),
("Средняя скорость производства", "500 единиц/час"),
("Процент выполненных заказов", "85%"),
("Количество сотрудников", "350"),
("Нагрузка на оборудование", "75%"),
("Процент выполнения плана", "80%"),
]

for item in prod_data:
self.prod_tree.insert("", tk.END, values=item)

def update_status_bars(self):
"""Обновляет статус-бары каждые 60 секунд."""
for i in range(60):
# Обновление текста статус-бара
current_load = random.randint(0, 100)
self.status_labels[i].config(text=f"Цех {i + 1}: Загруженность: {current_load}%")
self.progress_vars[i].set(current_load)

self.root.after(2000, self.update_status_bars)  # Запланировать следующий вызов через 2 секунды

def open_purchases(self):
messagebox.showinfo("Закупки", "Открыта вкладка Закупки")
        
def open_products(self):
messagebox.showinfo("Продукция", "Открыта вкладка Продукция")

def open_logistics(self):
messagebox.showinfo("Логистика", "Открыта вкладка Логистика")

def open_production(self):
messagebox.showinfo("Производство", "Открыта вкладка Производство")
        
def open_reports(self):
messagebox.showinfo("Отчёты", "Открыта вкладка Отчёты")

def open_suppliers(self):
messagebox.showinfo("Поставщики", "Открыта вкладка Поставщики")
        
def open_sales(self):
messagebox.showinfo("Продажи", "Открыта вкладка Продажи")

if __name__ == "__main__":
root = tk.Tk()
app = MyApp(root)
root.mainloop()
