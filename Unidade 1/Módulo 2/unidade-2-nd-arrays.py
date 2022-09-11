#!/usr/bin/env python
# coding: utf-8

# # NumPy - Numerical Python
# Criando arrays NumPy
# 

# In[182]:


# Importando o NumPy
import numpy as np


# #### - Criando arrays de 1 dimensão

# In[183]:


a1D = np.array([1, 2, 3])
a1D

# O objeto criado é um ndarray: n-dimensional array


# In[184]:


# Verificando o tipo dos elementos
a1D.dtype


# In[185]:


b1D = np.array([1, 2, 3], dtype = float)
b1D


# In[186]:


# str > float > int > bool
d1D = np.array([1, 3.14, "NumPy", True])
d1D

# Tudo será string nesse caso


# #### Criando arrays de 2 dimensões

# In[187]:


a2D = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2D


# #### Arrays preenchidos com zeros - zeros()

# In[189]:


zeros = np.zeros(5)
zeros


# In[191]:


zeros = np.zeros((4,3))
zeros


# In[193]:


zeros = np.zeros((3, 4), dtype = int) # 3 linhas e 4 colunas
zeros


# #### Arrays preenchidos com um - ones()

# In[194]:


ums = np.ones(5)
ums


# In[195]:


ums = np.ones((4,3))
ums


# In[196]:


ums = np.ones((3, 4), dtype = int) # 3 linhas e 4 colunas
ums


# In[197]:


ums = np.ones((3, 4), dtype = str) # 3 linhas e 4 colunas
ums


# In[ ]:


a1D = np.arange(10)
a1D


# In[198]:


c1D = np.arange(5,100, 10)
c1D


# In[204]:


# Cria um array com n elementos entre o valor inicial e valor final, igualmente espaçado
# Se não for passada a quantidade de elementos, o padrão é gerar 50 elementos
d1D = np.linspace(0,100, 10) # Cria um array com 2 valores entre 0 e 10
d1D


# In[206]:


#Cria arrays preenchidos com um único valor passado por parâmetro - full()
a1D = np.full(10, 5) # ndarray contendo 10 números 5
a1D


# In[207]:


a2D = np.full((3, 5), 3)  # ndarray de 3 linhas e 5 colunas contendo o número 3
a2D


# In[208]:


ident = np.eye(5) # Cria uma matriz 5x5 preenchida com 1s na diagonal principal e 0 nas posições restantes
ident


# In[209]:


a1D = np.random.randint(0, 100, 10) # Cria um ndarray com 10 elementos entre 0 e 99
a1D


# In[ ]:




