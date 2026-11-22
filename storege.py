FILE_NAME = "cards.txt" 
def save_cards(cards):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.writelines(cards)
def load_cards():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            cards = file.readlines()
            valid_cards = []
            for card in cards:
                fields = card.strip().split(",")
                if len(fields) == 5 and all(field.strip() for field in fields):
                    valid_cards.append(card)
                else:
                    print("Warning: Invalid card entry skipped:", card.strip())
            return valid_cards
    except FileNotFoundError:
        return []
