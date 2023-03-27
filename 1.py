def nome (n1,n2):
    if n1 > n2:
        return n1
    elif n1 == n2:
        return 'São iguais'
    return n2

n1=int(input("Diga o primeiro número:"))
n2=int(input("Diga o segundo número:"))
maior= nome(n1,n2)
print(maior)

    
