# из Фонетизауруса выход:
# анконихнус
# 	a0 n k o0 nj i1 h n u0 s
# арениколитэс
# 	a0 rj e1 nj i0 k o0 lj i1 t e0 s

# получаем:
# анконихнус a0 n k o0 nj i1 h n u0 s
# арениколитэс a0 rj e1 nj i0 k o0 lj i1 t e0 s

import io
import re

def replacer(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()
        text = text.lower()
        text = text.replace("\t", " ")

        a = 0
        bbb = False
        text2 = ""
        for i in text:
            
            
            if i == "\n":
                if bbb == False:
                    a = a + 1
                    # print(a)
                    
                    bbb = True
                else:
                    bbb = False
                    text2 = text2 + i
            else:
                text2 = text2 + i 

    with open("words_out.txt", 'w', encoding="utf-8") as f:  ##тут вордс оут
        f.write(text2)

replacer("file1.txt")    ### тут вордс 