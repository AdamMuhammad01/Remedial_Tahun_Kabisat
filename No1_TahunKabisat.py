print('No 1 Adam')
tahun = float(input('input tahun: '))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print('Hasil : TAHUN KABISAT');
        else:
            print('Hasil: BUKAN TAHUN KABISAT');
    else:
        print ('Hasil : TAHUN KABISAT');
else:
    print('Hasil : BUKAN TAHUN KABISAT');