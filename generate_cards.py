from storege import load_cards, save_cards
cards = load_cards()
for i in range(1, 18):
    card = f"Test Pokemon {i}, Test Set, Common, {i:03d}, Test Artist\n"
    cards.append(card)
save_cards(cards)
print("17 test cards added!")
