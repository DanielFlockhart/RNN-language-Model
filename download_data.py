import wikipedia

while True:
    dat = str(input("topic : "))
    pages = wikipedia.search(dat)
    with open("data.txt", "a+") as f:
        for x in pages:
            try:
                page = wikipedia.page(x)
                f.write(page.content)
            except:
                pass
        print("added data")
