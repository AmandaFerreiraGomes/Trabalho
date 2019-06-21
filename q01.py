def fEsp(x):
    porc = x/1048584
    return porc

def  fPorc( x):
    porc = x/25.8157
    return porc

def usuarios():
    i = 0
    arq_u = open('usuarios.txt', 'r')
    arq_r = open("relatorio.txt", "w")
    arq_r.write('ACME Inc.   \t   \t  Uso do espaço em disco pelos usuários\n')
    arq_r.write('------------------------------------------------------------------------------------\n')           
    arq_r.write("  Nr.  \t      Usuario      \t      Espaco utilizado      \t              % de uso    \t   \n")

    with open('usuarios.txt', 'r') as f:
        i = len(f.readlines())
        j = 0
        pass
    t = 0
    for linha in arq_u:
       valores = linha.split()
       if  j <= i:
           j = j + 1
           m = str(j)
           v = str(valores[0])
           arq_r.write('\n ')
           arq_r.write(m)
           arq_r.write('   \t ')        
           arq_r.write(v)
           num = float(valores[1])
           k = float(fEsp(num))
           d = str(k)
           arq_r.write("    \t  ")
           arq_r.write(d)
           arq_r.write("  \tMB")
           k2 = float(fPorc(k))
           e = str(k2)
           arq_r.write("    \t  ")
           arq_r.write(e)
           arq_r.write("  \t%")
           t = t + k
    med = t/i
    t1 = str(t)
    arq_r.write("\n Espaco total ocupado: ")
    arq_r.write(t1)
    arq_r.write("  \tMB")
    arq_r.write("\n Espaco medio ocupado: ")
    ax = float('%.2f' % med)
    med1 = str(ax)
    arq_r.write(med1)
    arq_r.write("  \tMB")
    
def main():
    usuarios()
main()
            




    
