#Crie uma função em Python para retornar a área de um retângulo, considere a seguinte fórmula
def area_retangulo(base, alt):
    area = base*alt;
    return area;

# print("\n",area_retangulo(2,5),"\n");
# Crie uma função em Python para mostrar a área de um círculo, considere a seguinte fórmula

def area_circulo(raio):
    area = (3.14 * (raio**2));
    return area

# print(area_circulo(2))

# 3.	Crie uma função em Python para mostrar o produto da multiplicação entre n valores.

def mult_valores(*args):
    aux = 1
    for i in args:
        aux*= i
    return aux
# print(mult_valores(2,2,2,2))


#4.	Crie uma função em Python para mostrar apenas as chaves de um dicionário.

# def Mostra_chave(**kwargs):    
#     chaves = kwargs
#     print(f"\nAqui mostra as chaves: {list(chaves.keys())}");
#     print(f"\nAqui mostra os valores: {list(chaves.values())}");
#     print(f"\nAqui mostra os itens: {list(chaves.items())}");
#     print(f"\nAqui é o tamanho do Dicionário: {len(chaves)}\n");
#     return chaves

# Mostra_chave(valor1=111, valor2=222, valor3= 333, valor4 = 444); 


def mostrar_chaves(dicionario):
    return list(dicionario.keys())

def mostrar_valores(dicionario):
    return list(dicionario.values())

def mostrar_itens(dicionario):
    return list(dicionario.items())



meu_dicionario = {"nome": "Italo", "idade": 24, "cidade": "Manaus"}


chaves = mostrar_chaves(meu_dicionario)
valores = mostrar_valores(meu_dicionario)
itens = mostrar_itens(meu_dicionario)

print("As chaves do dicionário são:", chaves);
print("Os valores do dicionário são:", valores);
print("Os itens do dicionário são: ", itens);
