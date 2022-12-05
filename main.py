import os, random, sys

from engine import entity, items, events

platform = {
    "win32": "cls",
    "linux": "clear"
}

day = 1

x, y = os.get_terminal_size()
dev = 1
dispatcher = events.Events()

def clear():
    os.system(platform[sys.platform])

def statics(user: entity.Entity):
    print(f"""Здоровье: {user.health}/{user.maxHealth}
Атака: {user.damage+user.weapon.damage}/{(user.damage+user.weapon.damage)*2}
Опыт: {user.xp:.2f}/{user.reqxp}
Предметы: {'Отсутствуют' if user.items == [] else ', '.join(map(lambda item: str(item), user.items))}
Оружие: {user.weapon}
Броня: {user.armor}
Уровень: {user.lvl}
Защита: {user.armor.armor}
Тип: {entity.entityTypes[user.type]}
""")
 
def death():
    clear()
    print(f"{chr(10)*(y//2-1)}{' '*(x//2-9//2)}Вы умерли")
    input(f"{' '*(x//2-30//2)}Нажмите Enter чтобы продолжить")
    player.health = player.maxHealth
    player.coins = 0
    player.items = []
    clear()
 
names = ['Орвутер', 'Анаель', 'Цраxьеикс', 'Бенгрун', 'Аомине', 'Мирилис', 'Гербальт', 'Могтаф', 'Исье', 'Мисса', 'Авоик', 'Круспас', 'Майнард', 'Тругомол', 'Гото', 'Могерун', 'Бисеаандер', 'Сенни', 'Хумфридус', 'Изабель', 'Дагдронун', 'Возал', 'Мацумото', 'Сеанайн', 'Илмаф', 'Радульф', 'Малик', 'Релгомод', 'Кетеаансиан', 'Лиеагмон', 'Захнатх', 'Шудулайс', 'Ройс', 'Сцекуин', 'Тазава', 'Цоуин', 'Брогтауч', 'Шимомура', 'Мункофан', 'Ходж', 'Загдрудач', 'Киасдиан', 'Гоин', 'Дерзукаф', 'Чолзол', 'Алис', 'Стеллид', 'Црааикс', 'Аделин', 'Араель', 'Иасутаке', 'Фонгрон', 'Друсеазал', 'Аедс', 'Гевеx', 'Аигфинс', 'Сагакет', 'Лоцрон', 'Отугоу', 'Рилгуерик', 'Канно', 'Ацур', 'Кигфеч', 'Илкоиx', 'Врернолея', 'Оргин', 'Иваиама', 'Велле', 'Хардуинус', 'Ингарет', 'Бригитта', 'Асмодей']

fists = items.Sword("Деревянный меч", "Меч оточеный в тренеровках", "base", 1, 0.08)
rag = items.Armor("Тряпки", "Тряпки, которые даже от мороза не спасут", "base", 0)

title = f"""{' '*(x//2-25//2)} _____ _____    __ _____ 
{' '*(x//2-25//2)}|     |  _  |__|  |   __|
{' '*(x//2-25//2)}| | | |     |  |  |   __|
{' '*(x//2-25//2)}|_|_|_|__|__|_____|_____|"""

print(title)
print(f"{'-'*x}Приветствую путник, перед тем как начать играть в maje придумайте себе ник")

player = entity.Entity(name = input("Ваш ник: "), health = 100, maxHealth = 100, damage = 1, xp = 0, lvl = 1, coins = 0, reqxp = 250, type = "Player", items = [], weapon = fists, armor = rag, events = dispatcher)
player.points = 0
player.location = 0

print(f"{'-'*x}Хорошо {player.name}, да начнется игра!")

input(f"{chr(10)*(y//2-9)}{' '*(x//2-30//2)}Нажмите Enter чтобы продолжить")

clear()

while True:
    dispatcher.checkEvent()
    print(title, end='\n' + '-'*x)
    print(f"""S - Навыки
ME - Иноформация обо мне
T - Торговля
A - Приключения
C - Создание предметов
S1 - Настройки
{"DM - Меню разработчика" if dev else ''}""")
    
    option = input(f'[{player.name}:Выбор] ').upper()
    clear()
    if option == 'S': pass
    if option == "ME":
        clear()
        statics(player)
        input(f"{' '*(x//2-29//2)}Нажмите Enter чтобы вернуться")
        clear()
    if option == 'T': pass
    if option == 'A':
        print(f"{' '*(x//2-(5+len(str(day)))//2)}ДЕНЬ {day}")
        
        health = random.randint(7,11)
        mob = entity.Entity(name = random.choice(names), health = health, maxHealth = health, damage = 1, xp = 20, lvl = 1, coins = 0, reqxp = 250, type = "Zombie", items = [], weapon = fists, armor = rag, events = dispatcher)
        
        print(f"Путешествуя по миру вы наткнулись на моба {mob.name}, его статистика:", end = "\n\n")
        statics(mob)
        text = ''
        while mob.health > 0:
            if player.health <= 0:
                death()
                break
            print(f"""{' '*(x//2-(16+len(str(player.health))+len(str(player.maxHealth)))//2)}Ваше здоровье: {player.health}/{player.maxHealth}
{' '*(x//2-(12+len(mob.name)+len(str(mob.health))+len(str(mob.maxHealth)))//2)}Здоровье {mob.name}: {mob.health}/{mob.maxHealth}
""")
            print("""A - Атака
S - Защита""")
            print(f"Последние сделаное действие: {text}")
            
            action = input(f'[{player.name}:Действие] ').upper()
            if action == "A":
                youhit = player.hit(mob)
                hit = mob.hit(player)
                text = f"Нанесено {'нисколько' if youhit == -1 else youhit}, по вам ударили {'нисколько' if hit == -1 else hit}"
            if action == "S":
                if random.randint(0, 0) == 0:
                    text = "Успешна защита!"
                else:
                    hit = mob.hit(player)
                    text = f"По вам ударили {'нисколько' if hit == -1 else hit}"
            clear()
        else:
            kill = mob.deathEvent(player)
            kill = f"Вы убили {mob.name} и получили {kill['xp']:.2f} XP, {mob.coins} Coins и следующие предметы: {', '.join(map(lambda item: str(item), kill['items']))}"
            print(f"{chr(10)*(y//2-1)}{' '*(x//2-len(kill)//2)}{kill}")
            input(f"{' '*(x//2-30//2)}Нажмите Enter чтобы продолжить")
            clear()
        day += 1
            
            
    if option == 'C': pass 
    