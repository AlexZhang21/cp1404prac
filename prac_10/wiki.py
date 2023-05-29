import wikipedia


def main():
    search_term = input("Please enter a page title or search phrase (or just press Enter to quit): ")
    while search_term:
        try:
            page = wikipedia.page(search_term, auto_suggest=False)
            print("\nPage - Title: %s" % page.title)
            print("Page - Summary: %s" % page.summary[0:60])
            print("Page - URL: %s" % page.url)
        except wikipedia.exceptions.DisambiguationError:
            print("The page title resulted in multiple matches. Please try a different title.")
        except wikipedia.exceptions.PageError:
            print("The page does not exist. Please try again.")
        search_term = input("Please enter a page title or search phrase (or just press Enter to quit): ")


main()