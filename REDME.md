#Назва: Колекція карток Pokemon
#Для кого: для мене (для колкціонері), щоб зберігати інформацію про свою колекцію.
#Запис: назва картки, серія, рідкість, кількість, художник.
#Операції: додати куртку, показати всі картки, знайти картку за назвою, серією або художником, видалити картку. 
#Звіти: загальна кількість карток, кількість карток за серіями, кількість рідкісних карток.

Подивитись всі картки:
py cli.py list
Добавити нові картки:
py cli.py add
Знайти картку за ім'ям:
py cli.py find (name)
Подивитись стати колекції:
py cli.py report
Запуск тестів:
py test.py

## Data Format
The collection is stored in a text file called cards.txt.
Each line represents one Pokémon card and contains five fields:

1. Card name
2. Set
3. Rarity
4. Card number
5. Artist

Fields are separated by commas.
Example:
Blastoise ex, Scarlet & Violet: 151, Special Illustration Rare, 165, Mitsuhiro Arita

Card numbers are stored as text to preserve leading zeros, such as 086.

#Лаб 7
Flask та SQlite щоб сортерувати карти

Нове віртуальне середовище
py -m venv venv
Актив. команд промпт
cmd
venv\Scripts\activates.bat
Завантажити залежності і тд.
pip install -r requirements.txt
Запустити app
py app.py

API
GET /cards - get all cards
POST /cards - add new cards
GET /cards?card_set=... - filter by set
DELETE /cards/1 - delete card by id

Database
Sqlite ('cards.db') сховище карток