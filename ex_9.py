"""
Nome: Equação de 2º Grau
Descrição: Este programa descobre as raízes de uma equação de 2º grau
Autor: Nikolas
Versão: 0.0.1
Data: 26/06/2023

"""

print("Este programa descobre as raízes de uma equação de 2º grau")

#Atribuição de Variáveis

i=0

#Entrada de Dados

while i<3:
    if i==0:
        a = float(input(f"\nDigite o valor do termo \"a\" da equação:"))
        i+=1
    if i==1:
        b = float(input(f"\nDigite o valor do termo \"b\" da equação:"))
        i+=1
    if i==2:
        c = float(input(f"\nDigite o valor do termo \"c\" da equação:"))
        i+=1
#Processamento de Dados

delta = b**2 - 4*a*c
print("delta=",delta,)

if ((delta>=0) and (a!=0)):

    x1 = (-b + (delta**(1/2)))/(2*a)
    x2 = ( b + (delta**(1/2)))/(2*a)

#Saída de Dados

    if a>0 or a<0:
        if b>0:
            if c>0:
                print("\nAs raízes da equação",a,"x^2 +",b,"x +",c,"= 0 são x'=",x1,"e x\"=",x2,".")
            elif c<0:
                print("\nAs raízes da equação",a,"x^2 +",b,"x",c,"= 0 são x'=",x1,"e x\"=",x2,".")
            else:
                print("\nAs raízes da equação",a,"x^2 +",b,"x = 0 são x'=",x1,"e x\"=",x2,".")
        elif b<0:
            if c>0:
                print("\nAs raízes da equação",a,"x^2",b,"x +",c,"= 0 são x'=",x1,"e x\"=",x2,".")
            elif c<0:
                print("\nAs raízes da equação",a,"x^2",b,"x",c,"= 0 são x'=",x1,"e x\"=",x2,".")
            else:
                print("\nAs raízes da equação",a,"x^2",b,"x = 0 são x'=",x1,"e x\"=",x2,".")
        elif b==0:
            if c>0:
                print("\nAs raízes da equação",a,"x^2 +",c,"= 0 são x'=",x1,"e x\"=",x2,".")
            elif c<0:
                print("\nAs raízes da equação",a,"x^2",c,"= 0 são x'=",x1,"e x\"=",x2,".")
            else:
                print("\nAs raízes da equação",a,"x^2 = 0 são x'=",x1,"e x\"=",x2,".")
    else:
        print("\nEsta não é uma equação válida.")

elif delta<0 and a!=0:
    print("\nEquação com parte imaginária, não programei pra isso...")
elif a==0:
    print("\nDivisão por 0!")