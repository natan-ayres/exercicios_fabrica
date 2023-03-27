def nome (n1,n2):
    if n1 % n2 ==0:
      return'é multiplo'
    elif n2 % n1 ==0:
      return 'é multiplo'
    else:
      return 'não é '

n1=int(input("Digite o primeiro número"))
n2=int(input("Digite o segundo número"))

print(nome(n1,n2))
