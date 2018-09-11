import pandas as pd

def check_letters(name):
    for letter in name.lower():
        if letter not in ['a', 'b', 'c', 'd', 'e', 'f', ' ']:
            return False
    return True

namesdf = pd.read_csv('potential_hexnames.csv').fillna('')

hexdf = namesdf[namesdf.apply(lambda x: check_letters(x.canonicalName), axis=1)]

hexdf.to_csv('hex_names.csv')
