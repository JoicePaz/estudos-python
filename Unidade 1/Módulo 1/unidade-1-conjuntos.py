#!/usr/bin/env python
# coding: utf-8

# # Conjuntos
# Conjuntos são coleções de elementos únicos, cujas principais características:
# 
# 1. Os elementos não são armazenados em uma ordem específica
# 2.  Conjuntos não contém elementos repetidos
# 3. Conjuntos não suportam indexação como as listas e tuplas

# #### - Como criar conjuntos

# In[84]:


# Criando conjuntos vazios
conj_vazio1 = set() # Essa é a única forma de se criar um conjunto vazio
type(conj_vazio1)


# In[50]:


# Visualizando o tipo
type(dic_vazio)


# In[85]:


# Criando conjuntos com elementos
conj1 = {1, 2, 3, 4, 5}
conj2 = {"A", "B", "C", "D"}
conj3 = {"ABC", 123, 3.14}
# Conjuntos não podem conter outras estruturas aninhadas


# #### - Como acessar elementos de um conjunto

# In[86]:


# Conjuntos não suportam indexação. Então vamos precisar do comando for para acessar os elementos de um conjunto
for elem in conj1:
    print(elem)


# In[87]:


# Nâo existe uma maneira de modificar elementos em um conjunto. 
# O que pode ser feito é a exclusão de um elemento, seguida da inserção de outro elemento


# In[88]:


# Adicionando o elemento 6
conj1.add(6)
conj1


# In[89]:


conj3.clear()
conj3


# In[90]:


# Criando os conjuntos s1 e s2
s1 = {1,2,3,4,5}
s2 = {4,5,6,7}

# Atribui a s3 a diferença do conjunto s1 em relação a s2
s3 = s1.difference(s2)
s3


# In[91]:


s4 = s1.intersection(s2)
s4


# In[93]:


# Verificando se s1 e s2 são disjuntos (diferentes)
s1.isdisjoint(s2)


# In[94]:


# Verificando se s3 e s3 são disjuntos
s3.isdisjoint(s4)


# In[96]:


# verificando se s3 é um subconjunto de s1
s3.issubset(s1)


# In[97]:


# verificando se s1 é um superconjunto de s3
s1.issuperset(s3)


# In[98]:


# Removendo o 3 de conj1 usando o remove()
conj1.remove(3)
conj1


# In[99]:


# Tentar remover um elemento inexistente com discard NÃO provoca um erro
conj1.discard(7)
conj1


# In[100]:


# Calculando o conjunto união. Veja que elementos repetidos só aparecem uma única vez no conjunto resultante
s6 = s1.union(s2)
s6


# In[101]:


# O que acontece se convertermos uma lista que contém elementos repetidos em um conjunto?
lista = [1, 2, 4, 3, 2, 1, 5, 2, 3, 1, 6, 3, 4, 2]

# Convertendo a lista em um conjunto
conj_lista = set(lista)

# Ao visualizar o conjunto obtido através da conversão da lista, vemos que não existem mais elementos repetidos
conj_lista

