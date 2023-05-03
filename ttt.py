f= open('my_file.txt',encoding='utf-8')
f.close()

with open('my_file.txt', ending= 'utf-8') as f: 
    f.write('The first line\n')
    f.write('This is second line\n')

