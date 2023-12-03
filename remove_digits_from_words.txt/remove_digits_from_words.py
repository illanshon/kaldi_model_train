import io
import re

def replacer(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' \d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
            else:
                aa = 0


        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' ', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0
        

    with open("words_out.txt", 'w', encoding="utf-8") as f:  ##тут вордс оут
        f.write(text)

replacer("words.txt")    ### тут вордс 