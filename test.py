from logic import count_by_rarity, count_cards, find_by_artist, find_by_number, find_by_rarity, find_by_set, find_card, add_card, delete_card, count_by_set
from storege import save_cards, load_cards
cards = ["Blastoise ex, Scarlet & Violet: 151, Special Illustration Rare, 165, Mitsuhiro Arita\n", "Scolipede, Scarlet & Violet: Black Bolt, Illustration Rare, 086, Oku\n"]
total_cards = count_cards(cards)
print(f"Total cards: {total_cards}")
empty_cards = []
result2 = count_cards(empty_cards)
print("Empty cards count:", result2)

#test 1
found = find_card(cards, "Blastoise ex")
print("Found cards:", found)

not_found = find_card(cards, "Pikachu")
print("Not found cards:", not_found)

#test 2
found_set = find_by_set(cards, "Scarlet & Violet")
print("Found cards:", found_set)

missing_set = find_by_set(cards, "Sun & Moon")
print("Missing cards:", missing_set)

#test 3
found_rarity = find_by_rarity(cards, "Special Illustration Rare")
print("Found cards by rarity:", found_rarity)

missing_rarity = find_by_rarity(cards, "Ultra Rare")
print("Missing cards by rarity:", missing_rarity)

#test 4
found_number = find_by_number(cards, "086")
print("Found cards by number:", found_number)

missing_number = find_by_number(cards, "999")
print("Missing cards by number:", missing_number)

#test 5
found_artist = find_by_artist(cards, "Mitsuhiro Arita")
print("Found cards by artist:", found_artist)

missing_artist = find_by_artist(cards, "Ken Sugimori")
print("Missing cards by artist:", missing_artist)

#test 6
test_cards = cards.copy()
new_card = "Pincurchin, Mega Evolution: Delta Reign, Illustration Rare, 103, Tetsu Kayama\n"
add_card(test_cards, new_card)
print("Cards after adding:", count_cards(test_cards))

empty_collection = []
add_card(empty_collection, new_card)
print("Cards in empty collection:", count_cards(empty_collection))

#test 7
#save_cards(test_cards)
saved_cards = load_cards()
print("Saved cards:", saved_cards)

#test 8
test_delete = cards.copy()
result = delete_card(test_delete, "Scarlet & Violet: Black Bolt", "086")
print("Card deleted:", result)
print("Cards left:", count_cards(test_delete))

result2 = delete_card(test_delete, "Scarlet & Violet: Black Bolt", "999")
print("Card deleted:", result2)
print("Cards left:", count_cards(test_delete))

#test 9
set_counts = count_by_set(cards)
print("Cards by set:", set_counts)

empty_set_counts = count_by_set([])
print("Empty set counts:", empty_set_counts)

#test 10
rarity_counts = count_by_rarity(cards)
print("Cards by rarity:", rarity_counts)

empty_rarity_counts = count_by_rarity([])
print("Empty rarity counts:", empty_rarity_counts)

#test 11
assert count_cards([]) == 0
assert count_cards(cards) == len(cards)
print("count_cards tests passed")

#test 12
assert find_card(cards, "Blastoise ex") == ["Blastoise ex, Scarlet & Violet: 151, Special Illustration Rare, 165, Mitsuhiro Arita\n"]
assert len(find_card(cards, "Blastoise")) == 1
assert find_card(test_cards, "Pikachu") == []
print("find_card tests passed")

#test 13
assert len(find_by_set(test_cards, "Scarlet & Violet")) == 2
assert find_by_set(test_cards, "Sun & Moon") == []
print("find_by_set tests passed")

#test 15
assert len(find_by_artist(test_cards, "Mitsuhiro Arita")) == 1
assert find_by_artist(test_cards, "Ken Sugimori") == []
print("find_by_artist tests passed")

#test 16
assert len(find_by_number(test_cards, "086")) == 1
assert find_by_number(test_cards, "999") == []
print("find_by_number tests passed")

#test 17
new_cards = []
add_card(new_cards, "Pikachu, Base Set, Common, 025, Ken Sugimori\n")
assert len(new_cards) == 1
add_card(new_cards, "Charizard, Base Set, Rare, 006, Ken Sugimori\n")
assert len(new_cards) == 2
print("add_card tests passed")

#test 18
delete_test_cards = ["Blastoise ex, Scarlet & Violet: 151, Special Illustration Rare, 165, Mitsuhiro Arita\n",
                     "Scolipede, Scarlet & Violet: Black Bolt, Illustration Rare, 086, Oku\n"]
assert delete_card(delete_test_cards, "Scarlet & Violet: Black Bolt", "086") == True
assert len(delete_test_cards) == 1
assert delete_card(delete_test_cards, "Scarlet & Violet: Black Bolt", "999") == False
assert len(delete_test_cards) == 1
print("delete_card tests passed")

#test 19
report_test_cards = ["Blastoise ex, Scarlet & Violet: 151, Special Illustration Rare, 165, Mitsuhiro Arita\n",
                     "Scolipede, Scarlet & Violet: Black Bolt, Illustration Rare, 086, Oku\n",
                     "Pincurchin, Mega Evolution: Delta Reign, Illustration Rare, 103, Tetsu Kayama\n"]
print("Actual result:", count_by_set(report_test_cards))
assert count_by_set(report_test_cards) == {"Scarlet & Violet: 151": 1, "Scarlet & Violet: Black Bolt": 1, "Mega Evolution: Delta Reign": 1}
assert count_by_set([]) == {}
print("count_by_set tests passed")

#test 20
print("Actual result:", count_by_rarity(report_test_cards))
assert count_by_rarity(report_test_cards) == {"Special Illustration Rare": 1, "Illustration Rare": 2}
assert count_by_rarity([]) == {}
print("count_by_rarity tests passed")
