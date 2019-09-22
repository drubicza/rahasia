import os, sys, time, random, base64
from time import sleep
os.system('clear')

def load(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


load('percakapan rahasia')
print 'DAFTAR CHAT\n\n1. Chat v1\n2. Chat v2\n'
pil = raw_input('Pilih nomor = ')
if pil == '1':
    os.system('clear')
    load('CHAT RAHASIA')
    print ''
    sleep(0.1)
    print 'Pilih chat kamu\n\n1. Buat pesan\n2. Buka pesan\n'
    load('Pilih nomor')
    no = raw_input('= ')
    if no == '1':
        os.system('clear')
        decode = raw_input('Masukan text = ')
        data = base64.b64encode(decode)
        print 'Hasil nya (', data, ')'
    elif no == '2':
        os.system('clear')
        encode = raw_input('Masukan code = ')
        data = base64.b64decode(encode)
        print 'Pesan anda (', data, ')'
    else:
        os.system('clear')
        load('Kata kunci salah')
elif pil == '2':
    os.system('clear')
    load('Chat rahasia versi 2')
    print 'PILIH PESAN MU\n\n1. Buat pesan\n2. Buka pesan\n'
    print 'Pilih no'
    no = raw_input('= ')
    if no == '1':
        os.system('clear')
        decode = raw_input('Masukan text = ')
        data = base64.b16encode(decode)
        print 'Hasil nya (', data, ')'
    elif no == '2':
        os.system('clear')
        encode = raw_input('Masukan code = ')
        data = base64.b16decode(encode)
        print 'Hasil nya (', data, ')'
    else:
        os.system('clear')
        load('No salah')
else:
    os.system('clear')
    load('Printah salah')
