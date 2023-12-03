# вебстраница вебстраница vj_B e0_I b_I s_I t_I r_I a0_I nj_I i1_I c_I a0_E      ->      вебстраница vj e0 b s t r a0 nj i1 c a0

import io
import re

def replacer(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        
        text = f.read().replace("_B", "").replace("_E", "").replace("_I", "").replace("_S", "")
                
        a = 0
        text_out = ""
        delete_mode = True
        for i in text:
            if i == "\n":
                a = a + 1
                print(a)

                delete_mode = True
                text_out = text_out + i

            elif i == " ":
                if delete_mode == True:

                    delete_mode = False
                else:
                    text_out = text_out + i
            else:
                if delete_mode == False:
                    text_out = text_out + i


    with open("align_lexocon_out.txt", 'w', encoding="utf-8") as f:  ##тут вордс оут
        f.write(text_out)

replacer("align_lexicon.txt")    ### тут вордс 