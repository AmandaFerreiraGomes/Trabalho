def cript():
    telef = int(input('DIGITE OS QUATRO DIGITOS: '))
    #---------BUSCAMOS--OS--VALORES--PARA--a,-b,-c-E-d.
    a = ((telef//1000)%10)
    b = ((telef//100)%10)
    c = ((telef//10)%10)
    d = ((telef//1)%10)

    dig1 =  ((a+6)%10)
    dig2 = ((b+6)%10)
    dig3 = ((c+6)%10)
    dig4 = ((d+6)%10)
    print("CRIPTOGRAFADO: ", dig3, dig4, dig1, dig2)

def descript():
    telef = int(input('DIGITE OS 4 DIGITOS: '))
    dig3 = ((telef//1000)%10)
    dig4 = ((telef//100)%10)
    dig1 = ((telef//10)%10)
    dig2 = ((telef//1)%10)

    if dig1<=5:
        a = ((10+ dig1)-6)
    else:
        a = (dig1-6)

    if dig2<=5:
        b = ((10+ dig2)-6)
    else:
        b = (dig2-6)
    if dig3<=5:
        c = ((10+ dig3)-6)
    else:
        c = (dig3-6)
    if dig4<=5:
        d = ((10+ dig4)-6)
    else:
        d = (dig4-6)
    print('DESCRIPTOGRAFADO: ', a, b, c, d)
    
def main():
    print("OLÁ, SEJA BEM-VINDO!\n")
    op = int(input('DIGITE A OPÇÃO DESEJADA:\n1-CRIPTOGRAFAR\n2-DESCRIPTOGRAFAR\n'))
    if op==1:
               cript()
    else:
               descript()
main()
