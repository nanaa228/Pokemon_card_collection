from logic import find_card, count_cards, count_by_rarity, count_by_set, add_card
import sys
from storege import load_cards, save_cards
def main():
    if len(sys.argv) < 2:
        print("Enter a command")
        return
    command = sys.argv[1]
    if command == "list":
        cards = load_cards()
        if not cards:
            print ("Your collection is empty :(")
        else:
            for card in cards:
                print(card.strip())
    elif command == "find":
        if len(sys.argv) < 3:
            print("Enter a card name")
            print("Example: py cli.py find Gastly")
            return
        name = sys.argv[2]
        cards = load_cards()
        results = find_card(cards, name)
        if results:
            for card in results:
                print(card.strip())
        else:
            print(f"Card not found: '{name}'")
    elif command == "count":
        cards = load_cards()
        total = count_cards(cards)
        print(f"Total cards: {total}")
    elif command == "report":
        cards = load_cards()
        print("Total cards:", count_cards(cards))
        print("Cards by set:")
        for card_set, amount in count_by_set(cards).items():
            print(card_set, ":", amount)
        print("Cards by rarity:")
        for rarity, amount in count_by_rarity(cards).items():
            print(rarity, ":", amount)
    elif command == "add":
        cards = load_cards()
        name = input("Card name: ").strip()
        if not name:
            print("Card name cannot be empty.")
            return
        card_set = input("Set: ").strip()
        rarity = input("Rarity: ").strip() 
        number = input("Number: ").strip()
        if not number.isdigit():
            print("Error: Card number must contain only digits.")
            return
        artist = input("Artist: ").strip()
        if not card_set or not rarity or not artist:
            print("Error: All fields must be filled.")
            return
        new_card = f"{name}, {card_set}, {rarity}, {number}, {artist}\n"
        add_card(cards, new_card)
        save_cards(cards)
        print("Card added successfully.")
    elif command == "help":
        print ("Pokemon Card Collection")
        print ("Avilable commands:")
        print ("add - Add a new card")
        print ("list - Show all cards")
        print ("find - Search for a card")
        print ("report - Show collection statistics")
        print ("help - Show available commands")
    else:
        print("Unknown command")
if __name__ == "__main__":
    main()