# выбираем из словаря 2млн те слова, которых нет

def replacer(filename_2mln, filename_origin):
    with open(filename_2mln, 'r', encoding="utf-8") as f:
        text = f.read()
        text = text.split('\n')
        
    with open(filename_origin, 'r', encoding="utf-8") as g:
        text_origin = g.read()
        text_origin = text_origin.split('\n')

    result = list(filter(lambda x: x not in text_origin, text))
    
    print(result[0])
    print(len(result))
    result = '\n'.join(result)
    
    with open("align_lexocon_out.txt", 'w', encoding="utf-8") as f:  ##тут вордс оут
        f.write(result)


replacer("align_lexicon_2mln.txt", "align_lexicon_origin.txt")    ### тут вордс 