#!/usr/bin/env python
# coding: utf-8

# Imprime en consola Hello World.
# 

# In[ ]:


pwd /Users/rodrigogutierrez
cd 1.1-lab_bash
pwd /Users/rodrigogutierrez/1.1-lab_bash
touch soluciones.txt


# Crea un directorio nuevo llamado new_dir.
# 

# mkdir new_dir

# Elimina el directorio

# In[ ]:


rm -r new_dir


# Copia el archivo sed.txt dentro de la carpeta lorem a la carpeta lorem-copy. TIP: Puede ser necesario crear la carpeta lorem-copy primero.
# 

# In[ ]:


pwd /Users/rodrigogutierrez/1.1-lab_bash
mkdir lorem
cd lorem
touch sed.txt
cd ..
mkdir lorem.copy
cp lorem/sed.txt lorem.copy/copysed.txt


# Muestra el contenido del archivo sed.txt dentro de la carpeta lorem.
# 

# In[ ]:


pwd /Users/rodrigogutierrez/1.1-lab_bash
cd lorem
cat sed.txt
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, 
sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 
Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. 
Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, 
nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, 


# Muestra el contenido de los archivos at.txt y lorem.txt dentro de la carpeta lorem.
# 

# In[ ]:


cd lorem
cat at.txt
At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum 
deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non 
provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
Et harum quidem rerum facilis est et expedita distinctio. 
Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod 
maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. 
Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet 
ut et voluptates repudiandae sint et molestiae non recusandae. 
Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores 
alias consequatur aut perferendis doloribus asperiores repellat
cat lorem.txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


# Visualiza las primeras 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy
# 

# In[ ]:


cd lorem.copy
head -3 copysed.txt
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit,


# Añade Homo homini lupus. al final de archivo sed.txt dentro de la carpeta lorem-copy.

# echo "Homo homini lupus." >> copysed.txt
# 

# Visualiza las últimas 3 líneas del archivo sed.txt dentro de la carpeta lorem-copy. Deberías ver ahora Homo homini lupus..
# 

# In[ ]:


tail -3 copysed.txt

Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, 
nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, 
vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Homo homini lupus.


# Encuentra al usuario activo en el sistema.
# 

# In[ ]:


whoami
rodrigogutierrez


# Encuentra dónde estás en tu sistema de ficheros.
# 

# In[ ]:


Users/rodrigogutierrez/1.1-lab_bash/lorem.copy()


# Lista los archivos que terminan por .txt en la carpeta lorem.
# 

# In[ ]:


pwd /Users/rodrigogutierrez/1.1-lab_bash/lorem.copy
cd ..
ls lorem/*.txt
lorem/at.txt  lorem/lorem.txt  lorem/sed.txt


# Cuenta el número de líneas que tiene el archivo sed.txt dentro de la carpeta lorem.
# 

# In[ ]:


cd lorem
wc -l sed.txt
8 sed.txt


# Cuenta el número de archivos que empiezan por lorem que están en este directorio y en directorios internos.
# 

# In[ ]:


-


# Cuenta el número de apariciones del string et en at.txt dentro de la carpeta lorem.
# 

# In[ ]:


grep -c "et" lorem/at.txt

