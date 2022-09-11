#!/usr/bin/env python
# coding: utf-8

# # Tuplas
# 
# * Assim com uma lista, uma tupla também é uma coleção de elementos. A diferença entre elas, é que a tupla é IMUTÁVEL. Ou seja, uma vez definidos os seus elementos, a tupla não pode mais ser alterada
# * Cada elemento possui uma posição dentro de uma lista. Essa posição é chamada índice
# 

# #### - Como criar uma tupla

# In[31]:


# Criando uma tupla vazia
tupla_vazia = ()
tupla_vazia2 = tuple()


# In[33]:


# Visualizando o tipo
type(tupla_vazia)


# In[34]:


# Verificando o tamanho da lista
len(tupla_vazia)


# In[36]:


# Criando tuplas com elementos

tupla1 = (3, 19, 4, 21, 3, 5, 13)
tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla", (1, 2, 3))
tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])


#  #### - Como acessar elementos de uma tupla

# In[37]:


tupla1[0]


# In[40]:


tupla3[8][1]


# #### - A imutabilidade de uma tupla

# In[42]:


# Tuplas são imutáveis, porém quando contém outros elementos não imutáveis, exemplo, lista, permitem a alteração.
tupla3[8][1] = 5
tupla3


# In[43]:


# Podemos adicionar elementos à lista armazenada no índice 8 da tupla
tupla3[8].extend([4, 5, 6])
tupla3


# #### - Convertendo uma tupla em lista

# In[44]:


lista = list(tupla1)
lista


# In[46]:


lista[6] = 10
lista


# In[47]:


tupla1

