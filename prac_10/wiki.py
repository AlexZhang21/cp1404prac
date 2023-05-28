import wikipedia


while True:
    page_title = input("Enter a page title or search phrase (or blank to exit): ")

    if not page_title:
        break

    try:
        page = wikipedia.page(title=page_title)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error: ", e.options)
        continue
    except wikipedia.exceptions.PageError as e:
        print("Page Error: ", e)
        continue

    print("Title: %s" % page.title)
    print("Summary: %s" % page.summary[0:60])
    print("URL: %s" % page.url)