#!/usr/bin/env python
# coding: utf-8

# # Hola Eduardo!
# 
# Mi nombre es David Bautista, soy code reviewer de Tripleten y hoy tengo el gusto de revisar tu proyecto.
# 
# Cuando vea un error la primera vez, lo señalaré. Deberás encontrarlo y arreglarlo. La intención es que te prepares para un espacio real de trabajo. En un trabajo, el líder de tu equipo hará lo mismo. Si no puedes solucionar el error, te daré más información en la próxima ocasión.
# 
# Encontrarás mis comentarios más abajo - por favor, no los muevas, no los modifiques ni los borres.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# 
# Puedes responderme de esta forma: 
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# </div>
# 
# ¡Empecemos!

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypotheses)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
#     * [3.2 Hipótesis 2: preferencias musicales los lunes y los viernes](#week)
#     * [3.3 Hipótesis 3: preferencias de género en Springfield y Shelbyville](#genre)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; y otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar las hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba tres hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 2. Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre los viernes por la noche.
# 3. Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar las hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos
#  2. Preprocesamiento de datos
#  3. Prueba de hipótesis
# 
# 
# ### Desafío
# 
# En este proyecto, preparamos un pequeño reto para ti. Incluimos un nuevo tipo de estructura de datos: las marcas temporales. Las marcas temporales son muy comunes y merecen una atención adicional. Más adelante en el programa, aprenderás mucho sobre ellas. Sin embargo, por ahora las trataremos como simples strings. Necesitamos marcas temporales en este proyecto para poner a prueba una de nuestras hipótesis. No te preocupes, te ayudaremos con esto. Tu nivel de conocimientos actual será suficiente para abordarlo.
# 
# Por ejemplo, digamos que tenemos dos marcas temporales: `dt1 = "12:00:00"` y `dt2 = "06:00:00"`. Queremos comparar estas dos marcas temporales y ver cuál es posterior.
# 
# Podemos compararlas mediante los operadores de comparación estándar (`<`, `>`, `<=`, `>=`, `==`, `!=`). Ejecuta la siguiente celda de código para comparar dos marcas temporales:
# 

# In[1]:


# Comparar los objetos datetime

dt1 = "12:00:00"
dt2 = "06:00:00"

if dt1 < dt2:
    print("La marca temporal 2 es posterior")
else:
    print("La marca temporal 1 es posterior")


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Muy bien, recuerda que para todo los proyectos que realices es importante genera un contexto donde se comente que trata el caso y cuáles con los objetivos a cumplir, además es indispensable que se genere una tabla de contenido con el fin de mantener el orden en la entrega. Buen trabajo con el reto.
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos en Y.Music y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[2]:


# importar pandas
import pandas as pd


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Importaste correctamente la librería ``pandas``</div>

# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[3]:


# Leer el archivo y almacenarlo en df
df = pd.read_csv('/datasets/music_project_en.csv')


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Cargaste adecuadamente el DataFrame</div>

# Muestra las 10 primeras filas de la tabla:

# In[4]:


# Obtener las 10 primeras filas de la tabla df
display(df.head(10))


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Te recomiendo usar ``display()`` en lugar de ``print()`` intentalo y notarás la diferencia~ </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a><br>
# No recibí noticia de que se haya evaluado mi proyecto por lo que hasta ahora me pongo a atender las revisiones. Desconocía el método display(). Por lo que pude leer el método es nativo de python sino que pertenece a entornos interactivos como Jupyter notebook para mostrar contenido enriquecido.
#     
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a><br>
# No te preocupes Eduardo, tienes razón display muestra el contenido de manera enriquecida.
#     
# </div>

# Obtén la información general sobre la tabla con un comando:

# In[5]:


# Obtener información general sobre los datos en df
print(df.info())


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Empleas bien el método ``.info()``</div>

# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Todas almacenan el mismo tipo de datos: `object` (objeto).
# 
# Según la documentación:
# - `' userID'` — identificador del usuario o la usuaria;
# - `'Track'` — título de la canción;
# - `'artist'` — nombre del artista;
# - `'genre'` — género musical;
# - `'City'` — ciudad del usuario o la usuaria;
# - `'time'` — hora exacta en la que se reprodujo la canción;
# - `'Day'` — día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas; otros, en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. `Detecta el tercer problema por tu cuenta y descríbelo aquí`.
# En los encabezados de la tabla algunos de ellos tienen espacios adicionales al principio o al final del texto. Se deberia aplicar snake case, cada palabra deberia estar escrita con caracteres en minusculas y eliminar los espacios para que todos los encabezados sean uniformes.
# 
# 

# ### Tus observaciones <a id='data_review_conclusions'></a>
# 
# `Escribe tus observaciones aquí:
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
# Son datos tipo object que contienen información y caracteristicas sobre la reproducción de canciones. Para entender lo que almacenan es posible examinar algunos ejemplos de datos contenidos en esas columnas.  
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestras tres hipótesis o necesitamos más información?`
# La tabla nos proporciona información relevante para las hipótesis pero podriamos necesitar mas datos, para evaluar completamente las 3 hipótesis.
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# Además de los problemas anteriormente mencionados en los encabezados, observando los primeros 10 registros de acuerco con la instrucción anterior, se puede observar un valor Nan en la fila 10 de la columna 'artist' y no se observan valores duplicados. Yo utilizaria isna() o isnull() para buscar valroes Nan y posteriormente rellenarlos con ceros o eliminar las filas y también buscaria duplicados en el data frame. 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Cuando utilizas ``.info()`` te puedas dar cuenta que las variables ``track``, ``artist`` y ``genre`` tienen valores nulos. Por lo demás buenas respuestas. </div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla:

# In[6]:


# La lista de encabezados para la tabla df
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * todos los caracteres deben ser minúsculas;
# * elimina los espacios;
# * si el nombre tiene varias palabras, utiliza snake_case.

# Pon todos los caracteres en minúsculas y muestra el encabezado de la tabla de nuevo:

# In[7]:


# Bucle en los encabezados poniendo todo en minúsculas
new_columns = []
for column in df.columns:
    new_columns.append(column.lower()) #Iteramos para convertir a minusculas los encabezados
    
df.columns = new_columns
print(df.columns)


# Ahora elimina los espacios al principio y al final de los encabezados y muéstralos:

# In[8]:


# Bucle en los encabezados eliminando los espacios
new_columns = []
for column in df.columns:
    new_columns.append(column.strip()) #Iteramos para eliminar los espacios
    
df.columns = new_columns
print(df.columns)


# Aplica snake_case al encabezado userID y muestra el encabezado de la tabla:

# In[9]:


# Cambiar el nombre del encabezado "user_id"
df.rename(columns = {'userid': 'user_id'}, inplace = True)
print(df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[10]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Buen trabajo modificando el nombre de las columnas!
# </div>

# [Volver a Contenidos](#back)

# ### MissValores ausentes <a id='missing_values'></a>
# Primero, encuentra el número de valores ausentes en la tabla. Para ello, utiliza dos métodos pandas:

# In[11]:


# Calcular el número de valores ausentes
missing_values = df.isna().sum()
print(missing_values)


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Para hacer esto, crea la lista `columns_to_replace`, recórrela con un bucle `for` y reemplaza los valores ausentes en cada columna:

# In[12]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace = ['track', 'artist', 'genre']

for column in columns_to_replace:
    df[column].fillna('unknown', inplace=True)


# Asegúrate de que la tabla no contiene más valores ausentes. Cuenta de nuevo los valores ausentes.

# In[13]:


# Contamos los valores ausentes
missing_values = df.isna().sum()

# Verificamos si no existen valores ausentes
if missing_values.sum() == 0:
    print("No hay valores ausentes en la tabla.")
else:
    print("Todavía hay valores ausentes en la tabla.")
    
print(missing_values)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Genial! Haces un uso novedoso de las sentencias ``try`` y ``except`` para mostrar los valores nulos de la tabla. </div>

# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla usando un comando:

# In[14]:


# Contar duplicados explícitos
duplicates_count = df.duplicated().sum() 
print("Los duplicados en la tabla:", duplicates_count)


# Llama al método `pandas` para deshacerte de los duplicados explícitos:

# In[15]:


# Eliminar duplicados explícitos
df = df.drop_duplicates().reset_index(drop = True)


# Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[16]:


# Comprobación de duplicados
print(df.duplicated().sum())


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Recuerda que cuando elimines los registros de una tabla tienes que reindexarla o podrías tener problemas. Te recomiendo emplear el método~
# 
# ```python 
# .reset_index(drop = True)
# ``` 
# ~y anidarlo en una misma línea de código~
#   
# </div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a><br>
# Es verdad, olvidé que el indice se altera una vez que se realiza el drop_duplicates(). Ya lo he corregido
#     
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a><br>
# 
# Buen trabajo Eduardo!
# </div>

# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para hacerlo:
# * recupera la columna deseada del dataFrame;
# * llama al método que te devolverá todos los valores de columna únicos;
# * aplica un método de ordenamiento a tu resultado.
# 

# In[17]:


# Inspeccionando los nombres de géneros únicos
 #unique_genres = df['genre'].unique() #En esta linea se obtiene un objeto numpy.ndarray
 #unique_genres_df = pd.DataFrame(unique_genres, columns=['genre']) #Convertimos la serie en un DataFrame
 #unique_genres_df = unique_genres_df.sort_values(by='genre')  # Ordena los géneros alfabéticamente

unique_genres = df['genre'].sort_values().unique()

display(unique_genres)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Buen trabajo te recomiendo utilizar ``.sort()_values`` en lugar de ``sorted()``~
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a><br>
# Tuve unos problemas en tratar de utilizar el método .sort_value(), hasta que lei un poco y pude emplearlo correctamente.
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a><br>
# 
# ~~Eduardo el output no es el esperado, lo modificaste, creo que te enredaste mucho haciendo este paso, te voy a dejar una guía para que puedas hacerlo fácilmente:~~
#     
# ```python
# unique_genres = df['genre'].sort_values().unique()
# ```
#     
# </div>
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante #2</b> <a class="tocSkip"></a><br>
# Ok creo que ya entendi pense que debia necesariamente crear todo un nuevo DataFrame para poder usar el sort_values() y manipularlo.
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a><br>
# 
# Buen trabajo Eduardo

# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, declara la función `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=` — la lista de duplicados;
# * `correct_genre=` — el string con el valor correcto.
# 
# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplaza cada valor de la lista `wrong_genres` con el valor en `correct_genre`. Utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos y reemplazarlos con el género correcto en la lista principal.

# In[18]:


# Función para reemplazar duplicados implícitos
def replace_wrong_genres(df, wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genre, correct_genre)
# Lista de duplicados implícitos
wrong_genres = ['hip', 'hop', 'hip-hop']
# Género correcto
correct_genre = 'hiphop'


# Llama a `replace_wrong_genres()` y pásale argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[19]:


# Eliminar duplicados implícitos
replace_wrong_genres(df, wrong_genres, correct_genre)


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[20]:


# Comprobación de duplicados implícitos
 #unique_genres = df['genre'].unique()
 #unique_genres_df = pd.DataFrame(unique_genres, columns=['genre'])
 #unique_genres_df = unique_genres_df.sort_values(by='genre') 
unique_genres = df['genre'].sort_values().unique()
display(unique_genres)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Buen trabajo Eduardo, cuando compruebes la eliminación de los duplicados implícitos no olvides aplicar el método ``.sort_values()``~
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a><br>
# Ya fue corregido ese detalle.
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a><br>
# 
# ~~Ten en cuenta la misma recomendación que te hice en el comentario anterior!~~
# </div>
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante #2</b> <a class="tocSkip"></a><br>
# Ya fue corregido tambien en este punto.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a><br>
# 
# Buen trabajo.

# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`
# 
# Analizar los duplicados en la columna 'genre', se puede notar que había varios nombres que representaban el mismo género pero  escritos de forma diferente o con alternativas.
# 
# Para la eliminación de duplicados, se creó una función llamada `replace_wrong_genres()` que recibió la lista de duplicados ("wrong_genres") y los valores correctos ("correct_genre"). Esta función reemplaza cada valor en la lista "wrong_genres" con el valor en "correct_genre."
# 
# Después de aplicar esta función, los duplicados se eliminaron y los nombres de género se estandarizaron. Al mostrar la lista de valores únicos de la columna 'genre' nuevamente, obteniendo una lista de géneros únicos sin duplicados.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo con tus observaciones para esta sección!
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypotheses'></a>

# ### Hipótesis 1: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[21]:


# Contando las canciones reproducidas en cada ciudad
city_groups = df.groupby('city')['track'].count()
display(city_groups)


# `Comenta tus observaciones aquí`
# 
# Puedes observar la diferencia en la actividad musical entre las dos ciudades, Springfield y Shelbyville permitiendo comprender si hay diferencias en la cantidad de canciones reproducidas en las dos ciudades. Puede servir como base para investigaciones posteriores y probar hipotesis.
# 
# 
# 
# 
# 

# Ahora agrupa los datos por día de la semana y encuentra el número de canciones reproducidas el lunes, miércoles y viernes.
# 

# In[22]:


selected_days = ['Monday', 'Wednesday', 'Friday']
filtered_df = df[df['day'].isin(selected_days)]
# Agrupar por ciudad y día, y contar la cantidad de canciones reproducidas
city_day_groups = filtered_df.groupby(['city', 'day'])['track'].count()

display(city_day_groups)


# `Comenta tus observaciones aquí`
# Es posible observar cómo varía la actividad de reproducción de música a lo largo de la semana. Identificar si hay patrones específicos para la musica que se escucha en función del día de la semana. Puedes comparar la actividad en los tres días y observar si hay diferencias.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente, en la segunda parte fuiste más allá de lo requerido por el ejercicio filtrando por ciudades.
# 
# </div>

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la `number_tracks()` para calcular el número de canciones reproducidas en un determinado día y ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'`.
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[23]:


# <creando la función number_tracks()>
# Declararemos la función con dos parámetros: day=, city=.
# Deja que la variable track_list almacene las filas df en las que
# el valor del nombre de la columna ‘day’ sea igual al parámetro day= y, al mismo tiempo,
# el valor del nombre de la columna ‘city’ sea igual al parámetro city= (aplica el filtrado consecutivo
# con la indexación lógica).
# deja que la variable track_list_count almacene el número de valores de la columna 'user_id' en track_list
# (igual al número de filas en track_list después de filtrar dos veces).
# permite que la función devuelva un número: el valor de track_list_count.

# La función cuenta las pistas reproducidas en un cierto día y ciudad.
# Primero recupera las filas del día deseado de la tabla,
# después filtra las filas de la ciudad deseada del resultado,
# luego encuentra el número de canciones en la tabla filtrada,
# y devuelve ese número.
# Para ver lo que devuelve, envuelve la llamada de la función en print().


# comienza a escribir tu código aquí
def number_tracks(day, city):
    track_list = df[(df['day'] == day) & (df['city'] == city)]
    track_list_count = len(track_list)
    return track_list_count


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[24]:


# El número de canciones reproducidas en Springfield el lunes
count_monday_springfield = number_tracks('Monday', 'Springfield')
display(count_monday_springfield)


# In[25]:


# El número de canciones reproducidas en Shelbyville el lunes
count_monday_shelbyville = number_tracks('Monday', 'Shelbyville')
display(count_monday_shelbyville)


# In[26]:


# El número de canciones reproducidas en Springfield el miércoles
count_wednesday_springfield = number_tracks('Wednesday', 'Springfield')
display(count_wednesday_springfield)


# In[27]:


# El número de canciones reproducidas en Shelbyville el miércoles
count_wednesday_shelbyville = number_tracks('Wednesday', 'Shelbyville')
display(count_wednesday_shelbyville)


# In[28]:


# El número de canciones reproducidas en Springfield el viernes
count_friday_springfield = number_tracks('Friday', 'Springfield')
display(count_friday_springfield)


# In[29]:


# El número de canciones reproducidas en Shelbyville el viernes
count_friday_shelbyville = number_tracks('Friday', 'Shelbyville')
display(count_friday_shelbyville)


# Utiliza `pd.DataFrame` para crear una tabla, donde
# * Los encabezados de la tabla son: `['city', 'monday', 'wednesday', 'friday']`
# * Los datos son los resultados que conseguiste de `number_tracks()`

# In[30]:


# Tabla con los resultados
data = {
    'city': ['Springfield', 'Shelbyville'],
    'monday': [count_monday_springfield, count_monday_shelbyville],
    'wednesday': [count_wednesday_springfield, count_wednesday_shelbyville],
    'friday': [count_friday_springfield, count_friday_shelbyville]
}

df_results = pd.DataFrame(data)
display(df_results)







# **Conclusiones**
# 
# `Comenta si la primera hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# Tras observar los datos, podemos concluir:
# 
# En Springfield escuchan más música que en Shelbyville los lunes y miércoles, pero esta tendencia se invierte los viernes. Los viernes, en Shelbyville reproducen más canciones que en Springfield.
# 
# Parece haber diferencias en la forma en que consumen música en ambas ciudades, pero estas diferencias no son constantes en todos los días de la semana.
# 
# Podríamos concluir que la primera hipótesis es parcialmente correcta. Hay diferencias en la forma en que se consume música en ambas ciudades, pero varían según el día de la semana. Por lo que no podemos llegar a una conclusión definitiva sin un análisis más detallado.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Muy buen trabajo en esta sección
# 
# </div>

# [Volver a Contenidos](#back)

# ### Hipótesis 2: música al principio y al final de la semana <a id='week'></a>

# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros diferentes a los que disfrutan los usuarios de Shelbyville.

# Cree dos tablas con los nombres proporcionados en los dos bloques de código siguientes:
# * Para Springfield — `spr_general`
# * Para Shelbyville — `shel_general`

# In[31]:


# cree la tabla spr_general a partir de las filas df
# donde el valor en la columna 'city' es 'Springfield'
spr_general = df[df['city'] == 'Springfield']


# In[32]:


# crea shel_general a partir de las filas df
# donde el valor en la columna 'city' es 'Shelbyville'
shel_general = df[df['city'] == 'Shelbyville']


# Escribe la función `genre_weekday()` con cuatro parámetros:
# * Una tabla para los datos (`df`)
# * El día de la semana (`day`)
# * La primera marca de tiempo, en formato (`time1`)
# * La última marca de tiempo, en formato (`time2`)
# 
# La función debería devolver información de los 15 géneros más populares de un día determinado en un período entre dos marcas de fecha y hora.
# Aplique la misma lógica de filtrado consecutivo, pero esta vez utilice cuatro filtros y luego cree una nueva columna con los respectivos recuentos de reproducción.
# Ordene el resultado de mayor a menor y devuélvalo.

# In[33]:


# 1) Deja que la variable genre_df almacene las filas que cumplen varias condiciones:
#    - el valor de la columna 'day' es igual al valor del argumento day=
#    - el valor de la columna 'time' es mayor que el valor del argumento time1=
#    - el valor en la columna 'time' es menor que el valor del argumento time2=
#    Utiliza un filtrado consecutivo con indexación lógica.

# 2) Agrupa genre_df por la columna 'genre', toma una de sus columnas,
#    y use el método size() para encontrar el número de entradas para cada una de
#    los géneros representados; almacena los Series resultantes en
#    la variable genre_df_count

# 3) Ordena genre_df_count en orden descendente de frecuencia y guarda el resultado
#    en la variable genre_df_sorted

# 4) Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted - los 15
#    géneros más populares (en un determinado día, en un determinado periodo de tiempo)

# Escribe tu función aquí
def genre_weekday(df, day, time1, time2):
    # Filtrado consecutivo
    # Cree la variable genre_df que almacenará solo aquellas filas df donde el día es igual a day=
    genre_df = df[(df['day'] == day) & (df['time'] > time1) & (df['time'] < time2)]# escribe tu código aquí

    genre_df_count = genre_df.groupby('genre')['genre'].count()# escribe tu código aquí

    # Ordene el objeto Serie resultante en orden descendente (para que los géneros más populares aparezcan primero en el objeto Series)
    genre_df_sorted = genre_df_count.sort_values(ascending=False) # escribe tu código aquí

    # Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted los 15 géneros más populares (en un día determinado, dentro de un período de timeframe)
    return genre_df_sorted[:15]


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~Puedes anidar las condiciones en una sola línea de código, te dejo una guía:~
#     
# ```python
# genre_df = condicion1 & condicion2 & condicion3
# ```
# También te recomiendo emplear ``.count()`` en lugar de ``.size()``   
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a><br>
# Esa solución se me ocurrió la primera vez que lo hice pero ya que estaba preescrito el código "genre_df =" 4 veces, asumí que la intención del proyecto no era hacer un filtrado consecutivo en una misma linea, sino uno despues de otro y lo realice siguiendo el código prefedinido. Seria bueno reportar esto y que sea modificado ya que se presta a confusión. He realizado la corrección sugerida.
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a><br>
# 
# Te entiendo Eduardo, hablaré con la persona encargada para que esto sea modificado. Recuerda emplear ``.count()`` en lugar de ``.size()``
#     
# </div>
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante #2</b> <a class="tocSkip"></a><br>
# Ya hice el cambio del .size() por el .count()
# </div>

# Compara los resultados de la función `genre_weekday()`para Springfield y Shelbyville el lunes por la mañana (de 7 a 11) y el viernes por la tarde (de 17:00 a 23:00). Utilice el mismo formato de 24 horas que el conjunto de datos (por ejemplo, 05:00 = 17:00:00):

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Importante
# ~Cuando introduces lo argumentos en la función en lugar de emplear ``df`` debes emplear ``spr_general`` y ``shel_general`` según el caso (aplica para toda la sección)~
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a><br>
# Es verdad no corregí eso, lo cual explica los resultados que obtenia. Ya lo he corregido.
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a><br>
# 
# Buen trabajo Eduardo!
#     
# </div>

# In[34]:


# llamando a la función para el lunes por la mañana en Springfield (utilizando spr_general en vez de la tabla df)
# Define las marcas de tiempo para el lunes por la mañana y el viernes por la tarde
lunes_manana_inicio = '07:00:00'
lunes_manana_fin = '11:00:00'
viernes_tarde_inicio = '17:00:00'
viernes_tarde_fin = '23:00:00'

springfield_lunes_manana = genre_weekday(spr_general, 'Monday', lunes_manana_inicio, lunes_manana_fin)
display(springfield_lunes_manana)


# In[35]:


# llamando a la función para el lunes por la mañana en Shelbyville (utilizando shel_general en vez de la tabla df)
shelbyville_lunes_manana = genre_weekday(shel_general, 'Monday', lunes_manana_inicio, lunes_manana_fin)
print(shelbyville_lunes_manana)


# In[36]:


# llamando a la función para el viernes por la tarde en Springfield
springfield_viernes_tarde = genre_weekday(spr_general, 'Friday', viernes_tarde_inicio, viernes_tarde_fin)
display(springfield_viernes_tarde)


# In[37]:


# llamando a la función para el viernes por la tarde en Shelbyville
shelbyville_viernes_tarde = genre_weekday(shel_general, 'Friday', viernes_tarde_inicio, viernes_tarde_fin)
display(shelbyville_viernes_tarde)


# **Conclusión**
# 
# `Comente si la segunda hipótesis es correcta o debe rechazarse. Explique su razonamiento.`
# 
# La segunda hipotesis dice que los lunes por la mañana (de 7 a 11), los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre los viernes por la noche (de 17:00 a 23:00). Se evaluan los resultaods de los generos más populares en ambos momentos para ambas poblaciones. 
# Si los géneros más populares difieren en las dos ciudades en los momentos específicos mencionados, se puede respaldar la hipótesis. Por otro lado, si los géneros más populares son en su mayoría los mismos en ambos lugares y momentos, la hipótesis se puede rechazar. 
# En conclusión comparando los resultados podemos ver que por la mañana en el horario estudiado escuchan los mismos generos músicales y de igual manera ocurre en la tarde por lo que podemos rechazar la segunda hipotesis. 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Tus conclusiones son precisas
# </div>

# [Volver a Contenidos](#back)

# ### Hipótesis 3: preferencias de género en Springfield y Shelbyville <a id='genre'></a>
# 
# Hipótesis: Shelbyville ama la música rap. A los residentes de Springfield les gusta más el pop.

# Agrupa la tabla `spr_general` por género y encuentra el número de canciones reproducidas de cada género con el método `count()`. Después, ordena el resultado en orden descendente y guárdalo en `spr_genres`.

# In[38]:


# Escribe una línea de código que:
# 1. agrupe la tabla spr_general por la columna 'genre';
# 2. cuente los valores 'genre' con count() en la agrupación;
# 3. ordene el Series resultante en orden descendente y lo guarde en spr_genres.
spr_genres = spr_general.groupby('genre')['user_id'].count().sort_values(ascending=False)


# Muestra las 10 primeras filas de `spr_genres`:

# In[39]:


# mostrar las 10 primeras filas de spr_genres
display(spr_genres.head(10))


# Ahora haz lo mismo con los datos de Shelbyville.
# 
# Agrupa la tabla `shel_general` por género y encuentra el número de canciones reproducidas de cada género. Después, ordena el resultado en orden descendente y guárdalo en la tabla `shel_genres`:
# 

# In[40]:


# Escribe una línea de código que:
# 1. agrupe la tabla shel_general por la columna 'genre';
# 2. cuente los valores 'genre' en el agrupamiento con count();
# 3. ordene el Series resultante en orden descendente y lo guarde en shel_genres.
shel_genres = shel_general.groupby('genre')['user_id'].count().sort_values(ascending=False)


# Muestra las 10 primeras filas de `shel_genres`:

# In[41]:


# Muestra las 10 primeras filas de shel_genres
print(shel_genres.head(10))


# **Conclusión**
# 
# `Comenta si la tercera hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`
# La tercera hipótesis plantea que los residentes de Shelbyville prefieren el rap, mientras que los de Springfield tienen una preferencia por el pop. 
# Observando los resultados en ambas ciudades (spr_genres y shel_genres), podemos notar que el pop es, el género más popular en Springfield, mientras que en Shelbyville, el rap no se encuentra entre los 10 generos mas populares. 
# En conclusión podemos aceptar parcialmente la hipotesis ya que con la información que tenemos no podemos afirmar que los habitantes de Shelbyville "aman" el rap o que los de Springfield "prefieren" el pop.

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre cada hipótesis.`
# Hipotesis 1:
# Con la evidencia que tenemos podemos aceptar parcialmente la hipotesis como correcta. Existen diferencias en la manera en que se escucha música en ambas localidades, pero permanecen en función del día de la semana. Por lo que para una conclusión definitiva se necesita un análisis más detallado.
# 
# Hipotesis 2:
# Con la evidencia que tenemos podemos rechazar la segunda hipotesis ya que comparando los resultados podemos ver que en el horario indicado por la mañana  ambas ciudades escuchan los mismos generos músicales y lo mismo ocurre en la tarde lo cual contradice totalmente l oque señala la segunda hipotesis.
# 
# Hipotesis 3:
# Con la evidencia que tenemos podemos aceptar parcialmente la hipotesis ya que no podemos afirmar que los habitantes de Shelbyville tengan una predilección por el genero del rap ni que los habitantes de Springfield lo tengan por el pop. Solo que uno de los generos mencionados es populares en la región que señala la hipótesis.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo eduardo 
# </div>

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General
#     
# ~Hola Eduardo.Te felicito por el desarrollo del proyecto hasta el momento, ahora bien, debes tener en cuenta los comentarios que he generado para la próxima entrega. Que estés bien!~
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #2
#     
# ~~Hola de nuevo eduardo, te queda una pequeña corrección, pronto terminaras tu proyecto. Keep working!~~
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #3
#     
# Buen trabajo Eduardo. Te felicito por la culminación del proyecto.</div>

# [Volver a Contenidos](#back)
