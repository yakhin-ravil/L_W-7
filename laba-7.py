# Вариант 30. Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
# В программе должны быть реализованы минимум один класс, три атрибута, два метода.

# Задание: в филармонии К музыкальных инструментов (музыкантов). Сформировать все возможные варианты квартетов.

# Ограничение: в филармонии есть подразделение на группы инструментов, которые перечисленны ниже:
# струнные: скрипка, виолончель, альт, контрабас, арфа, гитара, комуз, хомус, кыяк, кобыз, домбыра, гусли, балалайка, домра
# деревянные духовые: флейта, гобой, кларнет, фагот, саксофон, блокфлейта, шалмей, шалюмо, балабан, дудук, жалейка, свирель, зурна, альбока
# медные духовые: валторна, труба, корнет, флюгельгорн, тромбон, туба, сакбут, серпент
# ударные: барабаны, тарелки, бубен, кастаньеты, треугольник, ксилофон, литавры, колокольчики, вибрафон

# Целевая функция: ищет квартет с наибольшим рейтингом инструментов (музыкантов)

try:
    class Philharmony:
        def __init__(self, instruments, instruments2, instruments3, instruments4):
            self.instruments = instruments
            self.instruments2 = instruments2
            self.instruments3 = instruments3
            self.instruments4 = instruments4

        # Перебираем методом все возможные комбинации квартета из объектов
        def discover_best_quartet(self, number_musical_instruments):
            if number_musical_instruments == 1:
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

            if number_musical_instruments == 2:
                best_quartet = None
                max_rating = 0
                for i in range(len(self.instruments2)):
                    for j in range(i + 1, len(self.instruments2)):
                        for k in range(j + 1, len(self.instruments2)):
                            for b in range(k + 1, len(self.instruments2)):
                                quartet = [self.instruments2[i], self.instruments2[j], self.instruments2[k], self.instruments2[b]]
                                rate_sum = sum(instrument.rating for instrument in quartet)
                                if rate_sum > max_rating:
                                    best_quartet = quartet
                                    max_rating = rate_sum

            if number_musical_instruments == 3:
                best_quartet = None
                max_rating = 0
                for i in range(len(self.instruments3)):
                    for j in range(i + 1, len(self.instruments3)):
                        for k in range(j + 1, len(self.instruments3)):
                            for b in range(k + 1, len(self.instruments3)):
                                quartet = [self.instruments3[i], self.instruments3[j], self.instruments3[k], self.instruments3[b]]
                                rate_sum = sum(instrument.rating for instrument in quartet)
                                if rate_sum > max_rating:
                                    best_quartet = quartet
                                    max_rating = rate_sum

            if number_musical_instruments == 4:
                best_quartet = None
                max_rating = 0
                for i in range(len(self.instruments4)):
                    for j in range(i + 1, len(self.instruments4)):
                        for k in range(j + 1, len(self.instruments4)):
                            for b in range(k + 1, len(self.instruments4)):
                                quartet = [self.instruments4[i], self.instruments4[j], self.instruments4[k], self.instruments4[b]]
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
    instruments = [Instrument("Скрипка", 1000), Instrument("Виолончель", 700),
                    Instrument("Альт", 1000), Instrument("Комуз", 400), Instrument("Арфа", 1400),
                    Instrument("Гитара", 900), Instrument("Кыяк", 100), Instrument("Хомус", 100),
                   Instrument("Кобыз", 150), Instrument("Балалайка", 800), Instrument("Контрабас", 500),
                   Instrument("Домбыра", 3), Instrument("Гусли", 2)]
    
    instruments2 = [Instrument("Флейта", 200), Instrument("Гобой", 300),
                    Instrument("Кларнет", 900), Instrument("Фагот", 430), Instrument("Саксофон", 600),
                    Instrument("Блокфлейта", 340), Instrument("Шалмей", 200), Instrument("Шалюмо", 100),
                   Instrument("Балабан", 800), Instrument("Дудук", 500), Instrument("Жалейка", 1800),
                   Instrument("Свирель", 3), Instrument("Зурна", 2)]
    
    instruments3 = [Instrument("Валторна", 900), Instrument("Труба", 800),
                    Instrument("Корнет", 2500), Instrument("Флюгельгорн", 1300), Instrument("Тромбон", 1400),
                    Instrument("Туба", 380), Instrument("Сакбут", 400), Instrument("Серпент", 230)]
    
    instruments4 = [Instrument("Барабаны", 900), Instrument("Тарелки", 800),
                    Instrument("Бубен", 2300), Instrument("Кастаньеты", 1300), Instrument("Треугольник", 1400),
                    Instrument("Ксилофон", 380), Instrument("Литавры", 400), Instrument("Колокольчики", 230), Instrument("Вибрафон", 230)]

    # Создаем объект класса филармонии и передаем список инструментов
    philharmony = Philharmony(instruments, instruments2, instruments3, instruments4) 

    number_musical_instruments = int(input('\nВыберите тип инструментов:'
                       '\n1 - струнные''\n2 - деревянные духовые''\n3 - медные духовые''\n4 - ударные\n'))

    # Ошибка, если число не подходит под условие
    while number_musical_instruments < 1 or number_musical_instruments > 4: 
        number_musical_instruments = int(input('\nВведите натуральное число больше 0, но меньше 5:\n'))

    # Используем метод из класса филармонии для поиска квартета
    best_quartet = philharmony.discover_best_quartet(number_musical_instruments)

    if best_quartet:
        print("Найден квартет с наибольшим рейтингом:")
        for instrument in best_quartet:
            print(f"Инструмент - {instrument.name}, Рейтинг: {instrument.rating}")
        result_rating = sum(instrument.rating for instrument in best_quartet)
        print("Общая сумма рейтинга квартета:", result_rating)
except ValueError:
    print('\nПерезапустите программу и введите натуральное число.')