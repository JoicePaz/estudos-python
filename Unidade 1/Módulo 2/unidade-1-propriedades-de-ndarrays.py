#!/usr/bin/env python
# coding: utf-8

# # Propriedades de um ndarray
# 
# 

# In[182]:


# Importando o NumPy
import numpy as np


# #### - Verificando o formato e quantidade de dimensões de um array - shape e dim

# In[211]:


a2D = np.random.randint(1, 101, (4,5)) # Cria um ndarray de 4 linhas x 5 colunas com elementos entre 1 e 100
a2D


# In[212]:


a2D.shape


# In[213]:


a2D.ndim


# #### Verificando o tamanho das dimensões de um array - len

# In[214]:


len(a2D) # Retorna o tamanho da 1a dimensão (quantidade de linhas)


# In[215]:


len(a2D[0]) # Retorna o tamanho da 2a dimensão (quantidade de colunas)


# #### Verificando a quantidade de elementos de um array - size

# In[216]:


a2D.size


# #### Verificando o tipo dos elementos um array - dtype

# In[217]:


a2D.dtype


# In[218]:


a2D.dtype.name

