# ЁМКОСТЬ 1 J OO M K A SS TT       ->      ЕМКОСТЬ j o1 m k a sj tj
# from os import walk
import io
import re
## Убрать все <unk> из файлов

def replacer(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read().replace(" 1 ", " ").replace(" A ", " a0 ").replace(" AA ", " a1 ")\
        .replace(" B ", " b ").replace(" BB ", " bj ").replace(" C ", " c ").replace(" CH ", " ch ") \
        .replace(" D ", " d ").replace(" DD ", " dj ").replace(" E ", " e0 ").replace(" EE ", " e1 ")\
        .replace(" F ", " f ").replace(" FF ", " fj ").replace(" G ", " g ").replace(" GG ", " gj ")\
        .replace(" H ", " h ").replace(" HH ", " hj ").replace(" I ", " i0 ").replace(" II ", " i1 ")\
        .replace(" J ", " j ").replace(" K ", " k ").replace(" KK ", " kj ").replace(" L ", " l ").replace(" LL ", " lj ")\
        .replace(" M ", " m ").replace(" MM ", " mj ").replace(" N ", " n ").replace(" NN ", " nj ")\
        .replace(" O ", " o0 ").replace(" OO ", " o1 ").replace(" P ", " p ").replace(" PP ", " pj ")\
        .replace(" R ", " r ").replace(" RR ", " rj ").replace(" S ", " s ").replace(" SCH ", " sch ").replace(" SH ", " sh ").replace(" SS ", " sj ")\
        .replace(" T ", " t ").replace(" TT ", " tj ").replace(" U ", " u0 ").replace(" UU ", " u1 ")\
        .replace(" V ", " v ").replace(" VV ", " vj ").replace(" Y ", " y0 ").replace(" YY ", " y1 ")\
        .replace(" Z ", " z ").replace(" ZH ", " zh ").replace(" ZZ ", " zj ")\
        .replace(" AA", " a1 ").replace(" A", " a0 ")\
        .replace(" BB", " bj ").replace(" B", " b ").replace(" CH", " ch ").replace(" C", " c ")\
        .replace(" DD", " dj ").replace(" D", " d ").replace(" EE", " e1 ").replace(" E", " e0 ")\
        .replace(" FF", " fj ").replace(" F", " f ").replace(" GG", " gj ").replace(" G", " g ")\
        .replace(" HH", " hj ").replace(" H", " h ").replace(" II", " i1 ").replace(" I", " i0 ")\
        .replace(" J", " j ").replace(" KK", " kj ").replace(" K", " k ").replace(" LL", " lj ").replace(" L", " l ")\
        .replace(" MM", " mj ").replace(" M", " m ").replace(" NN", " nj ").replace(" N", " n ")\
        .replace(" OO", " o1 ").replace(" O", " o0 ").replace(" PP", " pj ").replace(" P", " p ")\
        .replace(" RR", " rj ").replace(" R", " r ").replace(" SCH", " sch ").replace(" SH", " sh ").replace(" SS", " sj ").replace(" S", " s ")\
        .replace(" TT", " tj ").replace(" T", " t ").replace(" UU", " u1 ").replace(" U", " u0 ")\
        .replace(" VV", " vj ").replace(" V", " v ").replace(" YY", " y1 ").replace(" Y", " y0 ")\
        .replace(" ZH", " zh ").replace(" ZZ", " zj ").replace(" Z", " z ")                      

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0
                # text = f.read().replace(match[0], "")
        

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], "")
            else:
                aa = 0

    with open("lexiconp_out.txt", 'w', encoding="utf-8") as f:
        f.write(text)



# def abc(filename):
#     with open(filename, 'r') as f:
#         text = f.read().replace('http://', 'https://')
#     with open(filename, 'w') as f:
#         f.write(text)
# def parseFiles(c):
#     w = list(walk(c))[0]
#     if w[1]:
#         for a in w[1]:
#             parseFiles(w[0]+'/'+a)
#     for fn in w[2]:
#         if fn.endswith('.txt'):
#             abc(w[0]+'/'+fn)

# parseFiles('.')

replacer("lexiconp.txt")