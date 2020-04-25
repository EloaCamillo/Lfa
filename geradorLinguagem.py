simbolos = ['d','b', 'c','d']
linguagem = []
imax = 4
jmax = 4
imin = 0
jmin = 0
i= []
j= []
expi = 0
expj = 0
palavra = ""
contador = 0

for x in range(jmax):
   i.append(x)
   j.append(x)

def Linguaguem (simbolos,i, j ):
    palavra = ""
    for x in range(len(i)):
        for y in range(len(simbolos)):
            contador = 0
            contador += 1
            palavra = palavra + (simbolos[y] * x)
        linguagem.append(palavra)
        palavra = ""



Linguaguem(simbolos, i, j)
sufiprefi = 'ddb'
print("Lista : " + str(linguagem))

comSufixo = list(filter(lambda x: x.endswith(sufiprefi), linguagem)) 
semSufixo = list(filter(lambda x: not x.endswith(sufiprefi), linguagem)) 

comPrefixo = list(filter(lambda x: x.startswith(sufiprefi), linguagem)) 
semPrefixo = list(filter(lambda x: not x.startswith(sufiprefi), linguagem)) 
  
 
print("Lista sem sufixo : " + str(semSufixo)) 
print("Lista com sufixo : " + str(comSufixo)) 
print("Lista sem prefixo : " + str(semPrefixo))
print("Lista com prefixo : " + str(comPrefixo)) 

# for x in linguagem:
#     print(x)