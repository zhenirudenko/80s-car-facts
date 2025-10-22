import json
import random
import datetime

# Читаем файл с фактами
with open('facts.json.txt', 'r', encoding='utf-8') as file:
    facts = json.load(file)

# Выбираем случайный факт
random_fact = random.choice(facts)
fact_id = random_fact['id']
fact_text = random_fact['fact']
fact_year = random_fact['year']

# Создаём имя файла с текущей датой
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
filename = f'fact-{current_date}.md'

# Записываем факт в новый Markdown-файл
with open(filename, 'w', encoding='utf-8') as file:
    file.write(f'# Fact #{fact_id} - {fact_year}\n\n')
    file.write(f'{fact_text}\n')

print(f'Создан файл: {filename} с фактом #{fact_id}')
