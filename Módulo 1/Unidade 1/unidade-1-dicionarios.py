#!/usr/bin/env python
# coding: utf-8

# # Dicionários
# Um dicionário é uma coleção de elementos que possuem uma chave e um valor
# Ao invés de um índice, usamos a chave para recuperar um valor
# 

# #### - Como criar uma dicionários

# In[49]:


# Criando um dicionários vazi
dic_vazio = {}
dic_vazio2 = dict()


# In[50]:


# Visualizando o tipo
type(dic_vazio)


# In[52]:


# Criando dicionários com pares chave/valor

dic_estados = { "MG":"Minas Gerais", "PR": "Paraná", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amzonas"}
dic_estados


# In[53]:


dic_notas_alunos = {"João":[30, 12, 21], "Maria": [20, 30, 29], "José": [20, 23, 19]}
dic_notas_alunos


#  #### - Como acessar um valor em um dicionário através de uma chave

# In[54]:


# Acessando o valor associado à chave "PR"
dic_estados["PR"]


# In[58]:


# Acessando a nota da primeira prova do João no dicionário dic_notas_alunos2
dic_notas_alunos["João"][1]


# #### - Modificando valores em um dicionário

# In[60]:


dic_estados["AM"] = "Amazonas"
dic_estados


# In[61]:


# Alterando a segunda nota de João para 22
dic_notas_alunos["João"][1] = 22
dic_notas_alunos


# In[62]:


# Alterando todas as notas de Maria. 
# Essa alteração não será feita nota a nota, mas atribuindo uma nova lista com as notas corretas

dic_notas_alunos["Maria"] = [25, 20, 22]
dic_notas_alunos


# In[64]:


exemplo = dic_notas_alunos.items()
exemplo


# In[70]:


# Remove e retorna o último elemento adicionado ao dicionário

dic_notas_alunos.popitem()
dic_notas_alunos


# In[72]:


# Retorna o valor associado a uma chave (se a chave existir). Caso não exista, insere a chave com o valor (opcional)

dic_notas_alunos.setdefault('batata', 25)
dic_notas_alunos


# In[73]:


dic_notas_alunos.setdefault('batata', 25)


# In[81]:


# Obter os valores de um dicionário

dic_notas_alunos.values()


# In[82]:


# Obter as chaves e os valores de um dicionário

dic_notas_alunos.items()


# In[77]:


# Criando um novo dicionário a partir da seleção das chaves que desejamos
dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10])
dic_num_pares


# In[78]:


# Se desejarmos atribuir um valor default, basta informar após a lista com as chaves
dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10], "par")
dic_num_pares


# In[80]:


# Visualizando as chaves de um dicionário
dic_num_pares.keys()


# In[ ]:





# In[ ]:




