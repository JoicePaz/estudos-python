#!/usr/bin/env python
# coding: utf-8

# #  Listas
# 
# Lista é uma coleção de elemenos onde cada elemento possui uma posição dentro de uma lista chamada índice.
# Inicia de 0 até n-1.

# In[1]:


lista_vazia = []
lista_vazia2 = list()


# In[2]:


#Para verificar o tamanho de uma lista usamos len()

len(lista_vazia)


# In[51]:


# Exemplos de listas com elementos

lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
lista_reais = [1.5, -2.13, 5.14]
lista_strings = ["Joice", "Python", "estudos", "IA"]
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
listas_aninhadas = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[4]:


#Para acessar o valor 7 de uma lista aninhada

listas_aninhadas[2][0]


# In[7]:


#Para acessar o valor inicial de uma lista
lista[0]


# #### - Como modificar elementos de uma lista

# In[8]:


lista[4] = 50
lista


# In[9]:


#Adicionado o 25 no final da lista

lista.append(25)
lista


# In[10]:


#Limpar todos os elementos

lista.clear()
lista


# #### - Copiando uma lista para outra

# In[21]:


lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
copia = lista
copia


# In[22]:


copia[0] = 10
copia


# In[23]:


lista

#O elemento 10 também foi alterado na lista, e não apenas em copia


# In[31]:


# A maneira correta de copiar uma lista para outra é através da chamada ao método copy()
lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
copia = lista.copy()


# In[32]:


lista


# In[33]:


copia


# In[34]:


copia[0] = 10
copia


# In[35]:


lista


# #### - Verificar quantas vezes um número repete na lista

# In[37]:


copia.count(10)


# #### - Adicionar uma lista no final de outra

# In[38]:


nums = [1, 2, 3]
nums.extend([4,5])
nums


# In[39]:


#Atenção que se utilizar append() para mais de um elemento ele produzirá outro resultado

nums = [1, 2, 3]
nums.append([4,5])
nums


# #### - index()

# In[42]:


# O método index nos permite saber em que posição determinado elemento está armazenado,
# retorna a posição da primeira ocorrência do elemento procurado.

lista = [1, 3, 7, 2, 3, 8, 4]
posicao = lista.index(2)
posicao


# #### - insert()
# 

# In[43]:


# O método insert() permite adicionar um elemento em qualquer posição da lista. 
# Caso a posição não exista, ele insere o elemento desejado na última posição
lista.insert(2, "ABC")
lista
lista.insert(100, "XYZ")
lista


# #### - pop()
# 

# In[44]:


# O método pop() é usado para apagar uma POSIÇÃO da lista
valor = lista.pop(2)
# Visualizando o valor retornado
valor


# In[45]:


lista


# In[46]:


# Removendo o elemento da última posição
lista.pop(-1)
# Visualizando a lista após a remoção 
lista


# #### - remove()

# In[52]:


# Utilizamos o método remove() quando desejamos apagar um elemento específico da lista
lista_strings


# In[53]:


lista_strings.remove("estudos")
lista_strings


# #### - sort()

# In[54]:


lista


# In[56]:


# Ordenando os elementos em ordem crescente
lista.sort()
lista


# In[58]:


# Ordenando os elementos em ordem decrescente
lista.sort(reverse=True)
lista


# In[59]:


# Não é possível ordenar uma lista com elementos de diferentes tipos


# #### - Funções aplicáveis a uma lista

# In[63]:


lista = [8, 3, 21, 14, 2, 45]
lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]


# In[64]:


len(lista)


# In[65]:


len(lista_letras)


# In[66]:


# A função max() retorna o maior elemento de uma lista
max(lista)


# In[67]:


# A função max() retorna o maior elemento de uma lista
max(lista_letras)


# In[68]:


# A função min() retorna o menor elemento de uma lista
min(lista)


# In[69]:


# A função min() retorna o menor elemento de uma lista
min(lista_letras)


# In[70]:


# A função sum() retorna a soma dos elementos de uma lista numérica
sum(lista)


# In[ ]:




