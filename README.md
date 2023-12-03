# kaldi_model_train

оригинальные файлы:
align_lexicon - словарь с транскрипцией из папки Graph/phones
lexiconp - словарь с транскрипцией
words.txt - пронумерованный словарь без транскрипции в котором нужно убать цифры
file1 - из фонетизауруса

align_lexicon_to_words.dic
вебстраница вебстраница vj_B e0_I b_I s_I t_I r_I a0_I nj_I i1_I c_I a0_E      ->      вебстраница vj e0 b s t r a0 nj i1 c a0

lexiconp_to_word.txt
VOLKSWAGEN 0.32235 F OO LL K S V AA GG I N      ->     VOLKSWAGEN  

lexiconp_to_words_dic
ЁМКОСТЬ 1 J OO M K A SS TT       ->      ЕМКОСТЬ j o1 m k a sj tj

phonetisaurus докером выводит транскрипцию
sudo docker run --rm -it -v $PWD:/work phonetisaurus/phonetisaurus "phonetisaurus-apply -m model.fst -wl test.wlist">>file1

small_model - оригинальная модель vosk для обучения

main.py - проверка модели в питоне с микрофоном

official_from_wav_file.py - проверка модели в питоне с .wav файлом