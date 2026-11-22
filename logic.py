def count_cards(cards):
    return len(cards) #кількість карт у списку

def find_card(cards, name):
    result = []
    for card in cards:
        card_name = card.split(",")[0]
        if name.lower() in card_name.lower():
            result.append(card)
    return result #Чи є картка за ім'ям

def find_by_set (cards, set_name):
    result = []
    for card in cards:
        card_set = card.split(",")[1]
        if set_name.lower() in card_set.lower():
            result.append(card)
    return result #Шукає картку за сетом

def find_by_rarity(cards, rarity):
    result = []
    for card in cards:
        rarity = card.split(",")[2]
        if rarity.lower() in rarity.lower():
            result.append(card)
    return result #Шукає картку за рідкістю

def find_by_number(cards, number):
    result = []
    for card in cards:
        card_number = card.split(",")[3]
        if number.lower() in card_number.lower():
            result.append(card)
    return result #Шукає картку за номером

def find_by_artist(cards, artist):
    result = []
    for card in cards:
        card_artist = card.split(",")[4]
        if artist.lower() in card_artist.lower():
            result.append(card)
    return result #Шукає картку за художником

def add_card(cards, new_card):
    cards.append(new_card)
    return cards #Додає нову картку до списку

def delete_card(cards, card_set, card_number):
    for card in cards:
        fields = card.split(",")
        current_set = fields[1].strip()
        current_number = fields[3].strip()
        if current_set.lower() == card_set.strip().lower() and current_number == card_number.strip():
            cards.remove(card)
            return True 
    return False #Видаляє картку зі списку за сетом та номером

def count_by_set(cards):
    sets = {}
    for card in cards:
        card_set = card.split(",")[1].strip()
        if card_set in sets:
            sets[card_set] += 1
        else:
            sets[card_set] = 1
    return sets #Підраховує кількість карток у кожному сеті

def count_by_rarity(cards):
    rarities = {}
    for card in cards:
        rarity = card.split(",")[2].strip()
        if rarity in rarities:
            rarities[rarity] += 1
        else:
            rarities[rarity] = 1
    return rarities #Підраховує кількість карток за рідкістю