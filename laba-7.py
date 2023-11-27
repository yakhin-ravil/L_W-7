# Вариант 30. Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
# В программе должны быть реализованы минимум один класс, три атрибута, два метода.

# Задание: в филармонии К музыкальных инструментов (музыкантов). Сформировать все возможные варианты квартетов.

# Ограничение: в филармонии есть подразделение на группы инструментов, которые перечисленны ниже:
# струнные: скрипка, виолончель, альт, контрабас, арфа, гитара, комуз, хомус, кыяк, кобыз, домбыра, гусли, балалайка, домра
# деревянные духовые: флейта, гобой, кларнет, фагот, саксофон, блокфлейта, шалмей, шалюмо, балабан, дудук, жалейка, свирель, зурна, альбока
# медные духовые: валторна, труба, корнет, флюгельгорн, тромбон, туба, сакбут, серпент
# ударные: барабаны, тарелки, бубен, кастаньеты, треугольник, ксилофон, литавры, колокольчики, вибрафон

# Целевая функция: ищет квартет с наибольшим рейтингом инструментов (музыкантов)

class Philharmony:
    def __init__(self, instruments):
        self.instruments = instruments

    # Перебираем методом все возможные комбинации квартета
    def discover_best_quartet(self):
        best_quartet = None
        max_rating = 0
        for i in range(len(self.instruments)):
            for j in range(i + 1, len(self.instruments)):
                for k in range(j + 1, len(self.instruments)):
                    for b in range(k + 1, len(self.instruments)):
                        quartet = [self.instruments[i], self.instruments[j], self.instruments[k], self.instruments[b]]
                        rate_sum = sum(instrument.rating for instrument in quartet)
                        if rate_sum > max_rating:
                            best_quartet = quartet
                            max_rating = rate_sum
        return best_quartet
    
# Класс для описания инструментов
class Instrument:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

# Создаем объекты инструментов
instruments_stringed = [Instrument("Скрипка", 1000), Instrument("Виолончель", 700),
                    Instrument("Альт", 1000), Instrument("Комуз", 400), Instrument("Арфа", 1400),
                    Instrument("Гитара", 900), Instrument("Кыяк", 100), Instrument("Хомус", 100),
                   Instrument("Кобыз", 150), Instrument("Балалайка", 800), Instrument("Контрабас", 500),
                   Instrument("Домбыра", 3), Instrument("Гусли", 2)]
instruments_wooden = [Instrument("Флейта", 200), Instrument("Гобой", 300),
                    Instrument("Кларнет", 900), Instrument("Фагот", 430), Instrument("Саксофон", 600),
                    Instrument("Блокфлейта", 340), Instrument("Шалмей", 200), Instrument("Шалюмо", 100),
                   Instrument("Балабан", 800), Instrument("Дудук", 500), Instrument("Жалейка", 1800),
                   Instrument("Свирель", 3), Instrument("Зурна", 2)]
instruments_brass = [Instrument("Валторна", 900), Instrument("Труба", 800),
                    Instrument("Корнет", 2500), Instrument("Флюгельгорн", 1300), Instrument("Тромбон", 1400),
                    Instrument("Туба", 380), Instrument("Сакбут", 400), Instrument("Серпент", 230)]
instruments_percussion = [Instrument("Барабаны", 900), Instrument("Тарелки", 800),
                    Instrument("Бубен", 2300), Instrument("Кастаньеты", 1300), Instrument("Треугольник", 1400),
                    Instrument("Ксилофон", 380), Instrument("Литавры", 400), Instrument("Колокольчики", 230), Instrument("Вибрафон", 230)]

# Создаем экземпляры квартетов для каждой группы инструментов
quartet_stringed = Philharmony(instruments_stringed)
quartet_wooden = Philharmony(instruments_wooden)
quartet_brass = Philharmony(instruments_brass)
quartet_percussion = Philharmony(instruments_percussion)

# Класс для вывода квартета с наивысшим рейтингом
class QuartetPrinter:
    def __init__(self, quartet):
        self.quartet = quartet

    def print_best_quartet_info(self):
        best_quartet = self.quartet.discover_best_quartet()
        for instrument in best_quartet:
            print(f"Инструмент - {instrument.name}, Рейтинг: {instrument.rating}")
        result_rating = sum(instrument.rating for instrument in best_quartet)
        print("Общая сумма рейтинга квартета:", result_rating)

try:
    number_musical_instruments = int(input('\nВыберите тип инструментов:'
                       '\n1 - струнные''\n2 - деревянные духовые''\n3 - медные духовые''\n4 - ударные\n'))
    
    # Ошибка, если число не подходит под условие
    while number_musical_instruments < 1 or number_musical_instruments > 4: 
        number_musical_instruments = int(input('\nВведите натуральное число больше 0, но меньше 5:\n'))

    print("\nНайден квартет с наибольшим рейтингом:")
    if number_musical_instruments == 1:
        printer = QuartetPrinter(quartet_stringed)
        printer.print_best_quartet_info()
    elif number_musical_instruments == 2:
        printer = QuartetPrinter(quartet_wooden)
        printer.print_best_quartet_info()
    elif number_musical_instruments == 3:
        printer = QuartetPrinter(quartet_brass)
        printer.print_best_quartet_info()
    elif number_musical_instruments == 4:
        printer = QuartetPrinter(quartet_percussion)
        printer.print_best_quartet_info()
except ValueError:
    print('\nПерезапустите программу и введите натуральное число.')  