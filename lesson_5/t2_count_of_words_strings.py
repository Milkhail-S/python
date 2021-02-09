f_name = 't2_non_program_md.txt'

fi = open(f_name, 'r')
strok = 0
for words in fi:
    wrd_count = len(words.split())
    strok += 1
    print(f'В {strok} строке содержится {wrd_count} слов')
print(f'Всего в файле строк: {strok}')
fi.close()
