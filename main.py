from sonnets import sonnets_list
from search import Index, Query

print("Reading sonnets...")
index = Index(sonnets_list)
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
