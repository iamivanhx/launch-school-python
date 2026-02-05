# write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:
def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match region:
        case 'US':
            return 'Hey!'
        case 'GB':
            return 'Hello!'
        case 'AU':
            return 'Howdy!'
        case _:
            return greet(language)

def extract_language(locale):
    return locale[:2]

def extract_region(locale):
    return locale.split('.')[0][-2:]

def greet(lang):
    match lang:
        case 'en':
            return 'Hi!'
        case 'fr':
            return "Salut!"
        case 'pt':
            return "Olá!"
        case 'de':
            return "Hallo!"
        case 'sv':
            return "Hej!"
        case 'af':
            return "Haai!"



print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

# Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, and feel free to fall back on the language-specific greetings in all other cases, for example:
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
