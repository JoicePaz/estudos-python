#!/usr/bin/env python
# coding: utf-8

# # Strings
# Em Python, variáveis strings são do tipo **str**. Como em outras linguagens de programação, as strings em Python são uma sequência (ou uma cadeia) de caracteres.

# #### - Como criar strings

# In[ ]:


# Strings são criadas através de aspas simples (apóstrofos) ou aspas duplas (aspas).


# In[102]:


'Hello world!!!'
"Hello world!!!"


# In[103]:


# Criando conjuntos com elementos
conj1 = {1, 2, 3, 4, 5}
conj2 = {"A", "B", "C", "D"}
conj3 = {"ABC", 123, 3.14}
# Conjuntos não podem conter outras estruturas aninhadas


# #### - Slicing (fatiamento) em strings

# * `s[ind]` => Acessa uma única posição.
# * `s[inicial:final]` => Acessa os caracteres armazenados entre os índices *ind_inicial* e *ind_inicial-1*
# * `s[inicial:final:inc]` => Acessa os caracteres armazenados entre os índices *inicial* e *ind_inicial-1* com incremento *inc*
# 

# In[104]:


# Redefinindo a string s
s = "I am learning python"


# In[106]:


# Retornando learning - Primeira opção
s[5:13]


# In[110]:


# Retornando learning - Segunda opção
s[-15:-7]


# In[112]:


# Retornando learning - Terceira opção
s[:13]  # Estamos acessando o string s a partir do início até o índice 13


# In[116]:


# Retornando apenas a palavra learning - 4a opção
s[:-7] # Estamos acessando o string s a partir do início até o índice -10


# In[120]:


# Nós podemos acessar posições não contínuas
s[0:12:2] # Serão acessados os caracteres armazenados nas posiçõs 0, 2, 4 e 6 (o incremento informado foi 2)


# In[121]:


# Serão acessadas os caracteres armazenados desde o início até o final, com incremento de 3 (posições 0,3,6,9,12,15)
s[::3] 


# In[122]:


s = 'ABC'*10
s


# In[123]:


'ABC' in 'ABCDEFGH'


# In[124]:


'XYZ' not in 'ABCDEFGH'


# #### - Strings são imutáveis

# In[125]:


s = "PythoM" # Python digitado com erro
s[5] = "n" # tentando corrigir, substituindo o caractere M armazenado no índice pelo n
# Irá causar um erro


# In[126]:


# Para corrigir vamos precisar redefinir o string
s = "Python"
s


# In[128]:


s = "i am learning python!"
s1 = s.capitalize()
print(s)
print(s1)


# In[129]:


s = "AbCdEf"
s1 = s.casefold()
s1


# In[130]:


s2 = s.lower()
s2


# In[131]:


s3 = s.upper()
s3


# In[132]:


# casefold() é mais agressivo em sua conversão se comparado ao lower()
s4 = "Der Fluß"
s5 = s4.casefold()
s5


# In[133]:


s6 = s4.lower()
s6


# In[134]:


s = "PYTHON"
s1 = s.center(20) # Centralizar s em um string de tamanho 20 - completa com espaços a esquerda e direita
s1


# In[135]:


s2 = s.center(30, "*") # Centralizar s em um string de tamanho 30 - completa com espaços a esquerda e direita
s2


# In[136]:


s = "I am learning python!"
s.count("a")


# In[137]:


s.count("am")


# In[140]:


s.endswith("demais!") 


# In[141]:


s.endswith("python!")


# In[142]:


s.startswith("I") # True


# In[143]:


s = "col1\tcol2\tcol3"
s1 = s.expandtabs() # Substitui as tabulações por espaços (default = 8)
print(s1)


# In[144]:


s = "A linguagem Python é demais! Python é sensacional."
s.find("Python") # Procura pelo substring "Python" no string s usando o método find()


# In[145]:


s.rfind("Python") # Procura pelo substring "Python" no string s usando o método rfind()


# In[146]:


s.index("Python") # Procura pelo substring "Python" no string s usando o método index(), se não achar da erro


# In[148]:


nome = "Joice"
idade = 25
print("My name is {} and I am {} years old.".format(nome, idade))


# In[149]:


print("My name is {name} and I am {age} years old.".format(age=25, name="Joice"))


# In[150]:


s = "D3C1FR4NDO"
s.isalnum() 


# In[151]:


s1 = "D3C1FR4NDO 0 CÓD1G0" 
s1.isalnum() # Falso por causa da presença de espaços


# In[152]:


s = "D3C1FR4NDO"
s.isalpha()


# In[153]:


s1 = "CÓDIGO"
s1.isalpha()


# In[154]:


s2 = "DECIFRANDO O CODIGO"
s2.isalpha()


# In[155]:


cidade = 'ӓmsterdӓm'
cidade.isascii()


# In[156]:


cidade = 'amsterdam'
cidade.isascii()
# A tabela ASCII é composta por 128 "caracteres" (sendo a maioria caracteres "imprimíveis") e não contempla caracteres acentuados.


# #### - Exemplo dos métodos isdecimal(), isdigit() e isnumeric()
# 
# * isdecimal() => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# * isdigit()   => caracteres decimais + subscrito e sobrescrito
# * isnumeric   => caracteres decimais + subscrito e sobrescrito + caracteres UNICODE que representem frações, números romanos, etc

# In[157]:


a = "12345"
b = "1234²"
c = "123²½"
print("a.isdecimal() = ", a.isdecimal())
print("b.isdecimal() = ", b.isdecimal())
print("c.isdecimal() = ", c.isdecimal())
print("="*25)
print("a.isdigit() = ", a.isdigit())
print("b.isdigit() = ", b.isdigit())
print("c.isdigit() = ", c.isdigit())
print("="*25)
print("a.isnumeric() = ", a.isnumeric())
print("b.isnumeric() = ", b.isnumeric())
print("c.isnumeric() = ", c.isnumeric())


# #### - Exemplo do método istitle()
# Retorna true se todas as palavras iniciarem com letra maiúscula

# In[158]:


titulo = "A Linguagem Python"
titulo.istitle()


# In[159]:


titulo = "A Linguagem de Programação Python"
titulo.istitle()


# #### - Exemplo dos métodos ljust() e rjust()

# In[160]:


#Adiciona espaçamentos em branco caso não definido.
s = "Esquerda".ljust(20)
s


# In[161]:


s1 = "Direita".rjust(20)
s1


# In[162]:


s2 = "Esquerda".ljust(20,"<")
s2


# #### Exemplo dos métodos lstrip(), rstrip() e strip()

# In[163]:


# lstrip() retira espaços, caso nao definido, da esquerda,
s = "      ABC   "
s1 = s.lstrip()
s1


# In[165]:


link = "https://www.python.org/"
s4 = link.lstrip("hpst:/")
s4


# In[164]:


# rstrip() retira espaços, caso nao definido, da direita
s2 = s.rstrip()
s2


# In[166]:


s5 = link.rstrip("hpst:/")
s5


# In[167]:


s6 = link.strip("hpst:/")
s6


# #### - Exemplo dos métodos partition(), rpartition(), split() e rsplit()

# In[169]:


email = "pessoa@dominio.com.br"


# In[170]:


t1 = email.partition("@")
t1
# A particição vira uma tupla.


# In[171]:


type(t1)


# In[172]:


l1 = email.split("@")
l1
# A particição vira uma lista.


# In[173]:


type(l1)


# In[175]:


l2 = email.rsplit("@")
l2
# Divide em lista a partir do caractere definido e não o exibe.


# In[176]:


t2 = email.partition(".")
t2
# Divide em tupla a partir do caractere definido.


# In[177]:


l5 = email.split(".", 1)
l5


# In[178]:


l6 = email.rsplit(".", 1)
l6


# In[ ]:


seq = "012.345.678.910"
t3 = seq.partition(".")
t3


# In[ ]:


t4 = seq.rpartition(".")
t4


# In[ ]:


msg = "Minha biblioteca favorita é numpy."
print(msg)
msg2 = msg.replace("numpy", "pandas")
print(msg2)


# In[179]:


s = "Essa é\numa\nstring\n\ncom várias\nlinhas"
print(s)


# In[180]:


linhas = s.splitlines()
linhas


# In[ ]:


s = "MAIÚSCULO | minúsculo!"
s1 = s.swapcase()
print(s)
print(s1)


# In[ ]:


titulo = "a linguagEm de programação pyThon"
novo_titulo = titulo.title()
print(novo_titulo)


# In[ ]:


cod_prod1 = "123".zfill(6)
cod_prod1


# In[ ]:


cod_prod2 = "234".zfill(8)
cod_prod2


# In[ ]:


cod_prod3 = "123456".zfill(5)
cod_prod3

