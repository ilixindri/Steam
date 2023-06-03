EOL = '\n'
try:
    with open('steam.txt', 'x') as _: print('', end='')
except: print('', end='')
with open('steam.txt', 'w') as f:
    m = 300 * (10**3)
    while m < 10**6:
        txt = f'login alexandrogonsan'
        f.write(txt)
        txt = EOL
        f.write(txt)
        for i in range(m, m + 6000):
            txt = f'app_license_request {i}'
            f.write(txt)
            txt = EOL
            f.write(txt)
        m += 5998