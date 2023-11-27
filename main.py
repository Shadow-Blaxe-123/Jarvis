import webbrowser

def open_in_browser(url):
    # todo: make it search up the site url from name and use it
    webbrowser.open(url)


if __name__ == "__main__":
    url = input('say: ')
    open_in_browser(f"www.{url}.com")
    print('hello World!!!')