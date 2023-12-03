
# VOLKSWAGEN 0.32235 F OO LL K S V AA GG I N      ->     VOLKSWAGEN  
## вручную Убрать все <unk> из файлов

# from os import walk
import io
import re
import os
from pathlib import Path


def replacer(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read().replace(" 1 ", " ").replace(" A ", " ").replace(" AA ", " ")\
        .replace(" B ", " ").replace(" BB ", " ").replace(" C ", " ").replace(" CH ", " ") \
        .replace(" D ", " ").replace(" DD ", " ").replace(" E ", " ").replace(" EE ", " ")\
        .replace(" F ", " ").replace(" FF ", " ").replace(" G ", " ").replace(" GG ", " ")\
        .replace(" H ", " ").replace(" HH ", " ").replace(" I ", " ").replace(" II ", " ")\
        .replace(" J ", " ").replace(" K ", " ").replace(" KK ", " ").replace(" L ", " ").replace(" LL ", " ")\
        .replace(" M ", " ").replace(" MM ", " ").replace(" N ", " ").replace(" NN ", " ")\
        .replace(" O ", " ").replace(" OO ", " ").replace(" P ", " ").replace(" PP ", " ")\
        .replace(" R ", " ").replace(" RR ", " ").replace(" S ", " ").replace(" SCH ", " ").replace(" SH ", " ").replace(" SS ", " ")\
        .replace(" T ", " ").replace(" TT ", " ").replace(" U ", " ").replace(" UU ", " ")\
        .replace(" V ", " ").replace(" VV ", " ").replace(" Y ", " ").replace(" YY ", " ")\
        .replace(" Z ", " ").replace(" ZH ", " ").replace(" ZZ ", " ")\
        .replace(" AA", " ").replace(" A", " ")\
        .replace(" BB", " ").replace(" B", " ").replace(" CH", " ").replace(" C", " ")\
        .replace(" DD", " ").replace(" D", " ").replace(" EE", " ").replace(" E", " ")\
        .replace(" FF", " ").replace(" F", " ").replace(" GG", " ").replace(" G", " ")\
        .replace(" HH", " ").replace(" H", " ").replace(" II", " ").replace(" I", " ")\
        .replace(" J", " ").replace(" KK", " ").replace(" K", " ").replace(" LL", " ").replace(" L", " ")\
        .replace(" MM", " ").replace(" M", " ").replace(" NN", " ").replace(" N", " ")\
        .replace(" OO", " ").replace(" O", " ").replace(" PP", " ").replace(" P", " ")\
        .replace(" RR", " ").replace(" R", " ").replace(" SCH", " ").replace(" SH", " ").replace(" SS", " ").replace(" S", " ")\
        .replace(" TT", " ").replace(" T", " ").replace(" UU", " ").replace(" U", " ")\
        .replace(" VV", " ").replace(" V", " ").replace(" YY", " ").replace(" Y", " ")\
        .replace(" ZH", " ").replace(" ZZ", " ").replace(" Z", " ")                      

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
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
                text = text.replace(match[0], " ")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
            else:
                aa = 0

        aa = 1
        while aa == 1:
            aa == 0
            match = re.search(' 0.\d', text)
            print(match[0] if match else 'Not found')
            
            if match:
                aa = 1
                text = text.replace(match[0], " ")
            else:
                aa = 0
        
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
        

    with open("lexiconp_text_tmp.txt", 'w', encoding="utf-8") as f:
        f.write(text)

def remove_dublicates(filename):
    with open(filename, 'r', encoding="utf-8") as f:

        text = f
        unique_chars = {}

        text_tmp = text
        for char in text_tmp:

            unique_chars[char] = 1

            text_tmp = ''.join(unique_chars.keys())
        
        text = text_tmp
    
    with open("lexiconp_unique.txt", 'w', encoding="utf-8") as f:  ##OUT NAME
        f.write(text)



replacer("lexiconp.txt")                                            ##IN NAME
remove_dublicates("lexiconp_text_tmp.txt")
os.remove("lexiconp_text_tmp.txt")

