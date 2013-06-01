import ConfigParser as CP

def getConfig(filename):
    config = CP.ConfigParser()
    config.read(filename)
    sections = config.sections()
    items = {}
    for s in sections:
        items[s] = config.items(s)
    return items

if __name__ == "__main__":
    print(getConfig('./application.conf'))
