def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def reverse_list(lst):
    return lst[::-1]
print("Felix")
print("Toño")

def contarPalabraClave(lista, clave):
    return lista.count(clave)
def promedio (lista):
    if len(lista)==0:
        return 0
    return sum(lista)/len(lista)
