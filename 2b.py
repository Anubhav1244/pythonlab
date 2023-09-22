#binary decimal and octal to hexadecimal
# binary to decimal

def bintodec(bin):
    dec=0
    for digit in bin:
        dec=2*dec+int(digit)
    return dec

def oct_to_hex(oct):
    dec=0
    for digit in oct:
        dec=dec*8+int(digit)
    a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex=" "
    while(dec>0):
        rem=dec%16
        hex+=a[rem]
        dec=dec//16
    return hex


a=bintodec("100")
print(a)
