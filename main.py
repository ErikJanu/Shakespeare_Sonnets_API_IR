## This project was completed as a group ##
## Hoang Nam Huynh-Viet, Erik Janusch, Elizaveta Ziulkova ##

from sonnets import Sonnet, sonnets_dictionary_list, sonnets_list
from search import Index, Query

print("Reading sonnets...")
index = Index(sonnets_list)


# Print the result for the task №2:
fifteenth_sonnet = Sonnet(sonnets_dictionary_list[14])

print('Print the result for the fask №2:')
print("Sonnet Number is:", fifteenth_sonnet.id)
print("Sonnet Title is:", fifteenth_sonnet.title)
print("Sonnet Lines are:", fifteenth_sonnet.lines)

# Print the result for the tokenization task:
print('Print the result for the tokenization task:')
print(fifteenth_sonnet.tokenize(use_stemming=False))

# Print the result for the stemming task:
print('Print the result for the stemming task:')
print(fifteenth_sonnet.tokenize(use_stemming=True))

while True:
    search_terms = input("Search for sonnets('q' to quit): ")

    if search_terms.lower() == 'q':
        print("Fare thee well.")
        break

    query = Query(search_terms)

    matching_sonnets = index.search(query)

    sing_plur_sonnet = "sonnets"
    if len(matching_sonnets) == 1:
        sing_plur_sonnet = "sonnet"

    print(f"\nYour search for '{search_terms}' matched {len(matching_sonnets)} {sing_plur_sonnet}: "
          f"{[sonnet.id for sonnet in matching_sonnets]}")

    for matching_sonnet in matching_sonnets:
        print(matching_sonnet)
