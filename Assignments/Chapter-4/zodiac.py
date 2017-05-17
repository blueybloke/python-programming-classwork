#Zodiac Calculator
#Maxwell Phillips
#4 May
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Declare variables
#3)Ask for input
#4)Search the dictionary for the year
#5)Print out the information
#-------------------------------------------------------------------------------
#Greeting
print("="*80)
print("""This program will determine your Chinese zodiac sign and associated personal
characteristics.
""")

#Declare variables and dictionaries
zodiacs = {
    'Rat': {
        'Years':(1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020),
        'Chars':'Rats are quick-witted, resourceful, versatile, kind, smart, and lovely'
        },
    'Ox': {
        'Years':(1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021),
        'Chars':'Oxes are known for diligence, dependability, strength and determination.'

        },
    'Tiger': {
        'Years':(1914, 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022),
        'Chars':'People born in the year of the Tiger are brave, competitive, unpredictable, and self-confident.'

        },
    'Rabbit': {
        'Years':(1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023),
        'Chars':'Rabbits tend to be gentle, quiet, elegant, and alert; quick, skillful, kind, and patient'

        },
    'Dragon': {
        'Years':(1916, 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024),
        'Chars':'Dragons are gifted with innate courage, tenacity and intelligence, dragons are enthusiastic and confident. They are not afraid of challenges, and willing to take risks.'

        },
    'Snake': {
        'Years':(1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025),
        'Chars':'In Chinese culture, the Snake is the most enigmatic animal among the twelve zodiac animals. People born in a year of the Snake are supposed to be the most intuitive.'

        },
    'Horse': {
        'Years':(1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026),
        'Chars':'People born in a year of the Horse are extremely animated, active and energetic.'

        },
    'Goat': {
        'Years':(1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027),
        'Chars':'People born in a year of the Goat are generally believed to be gentle mild-mannered, shy, stable, sympathetic, amicable, and brimming with a strong sense of kindheartedness and justice.'

        },
    'Monkey': {
        'Years':(2016,2004,1992,1980,1980,1968,1956,1944,1932),
        'Chars':'Ambitious and adventurous, but irritable'

        },
    'Rooster': {
        'Years':(1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017),
        'Chars':'Roosters are always active, amusing, and popular within a crowd. Roosters are talkative, outspoken, frank, open, honest, and loyal individuals. They like to be the center of attention and always appear attractive and beautiful.'

        },
    'Dog': {
        'Years':(1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018),
        'Chars':'Dogs are loyal and honest, amiable and kind, cautious and prudent. Due to having a strong sense of loyalty and sincerity, Dogs will do everything for the person who they think is most important.'

        },
    'Pig': {
        'Years':(1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031),
        'Chars':'Pigs are diligent, compassionate, and generous. They have great concentration: once they set a goal, they will devote all their energy to achieving it. Though Pigs rarely seek help from others, they will not refuse to give others a hand. Pigs never suspect trickery, so they are easily fooled.'

        }
}
#Ask for input
year = int(input("Please enter your year of birth: "))
#Search dict for year
for k, v in zodiacs.items():
    if year in v['Years']:
        animal = k
#Print the name
print("\nYou are a",animal+"!")
#Print the information
print(zodiacs[animal]['Chars'])
