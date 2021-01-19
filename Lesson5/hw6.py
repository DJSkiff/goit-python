

def normalize(string):

    # dict with transliteral letters

    trans_dict = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('є'): 'ye', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y', 
    ord('і'): 'i', ord('ї'): 'yi', ord('й'): 'y', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', 
    ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ю'): 'yu', 
    ord('я'): 'ya', ord('ы'): 'y', ord('э'): 'e', ord('ё'): 'yo' }

    upperIndex = [] 
    
    stringUp = []

    normalized = ''

    # determine the index of the capital letter

    for c in string: 
        if c.isupper():
            upperIndex.append(string.index(c))

    # bring the string to lowercase

    stringLo = string.lower()

    # main part of function

    for c in stringLo:

        if stringLo.index(c) in upperIndex:

            c = c.translate(trans_dict)
            
            stringUp.append(c.capitalize())
        
        elif not c.isalpha() and not c.isdigit():
        
            c = '_'
        
            stringUp.append(c)
        
        else:

            c = c.translate(trans_dict)

            stringUp.append(c) 
        

    return normalized.join(stringUp)