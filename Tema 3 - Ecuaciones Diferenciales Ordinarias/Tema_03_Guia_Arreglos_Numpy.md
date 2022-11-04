# Definición de un arreglo.

Las estructuras de datos que hemos visto (listas, tuplas, diccionarios) hasta ahora permiten manipular datos de manera muy flexible. Ya sea combinándolas y/o anidándolas, es posible organizar información de manera estructurada para representar sistemas del mundo real.

En física para resolver problemas, más importante que la organización de los datos, es la capacidad de hacer muchas operaciones a la vez sobre grandes conjuntos de datos numéricos de manera eficiente.

Algunos ejemplos de problemas que requieren manipular grandes secuencias de números son: la predicción del clima, simulación, graficación de modelos, la construcción de edificios, y el análisis de indicadores financieros entre muchos otros.

## El arreglo en python.

La estructura de datos que sirve para almacenar estas grandes secuencias de números (generalmente de tipo *float*) es el **arreglo**.

Los arreglos tienen algunas similitudes con las listas:
1. Los elementos tienen un orden y se pueden acceder mediante su posición.
2. Los elementos se recorren usando un ciclo <code>for</code>.

Sin embargo, también tienen algunas restricciones:
1. Todos los elementos del arreglo deben ser del mismo tipo.
2. En general, el tamaño del arreglo es fijo (no van creciendo dinámicamente como las listas).
3. Se ocupan principalmente para almacenar datos numéricos.

Los arreglos son los equivalentes en programación a las matrices y vectores en matemáticas. Precisamente, una gran motivación para usar arreglos es que hay mucha teoría detrás de ellos que puede ser usada en el diseño de algoritmos para resolver problemas verdaderamente interesantes.

# Usando numpy.array

## Creando un arreglo.

El módulo y la función que provee las estructuras de datos y las funciones para trabajar con arreglos es <code>numpy.array</code>

import numpy as np

El tipo de datos de los arreglos se llama <code>array</code>. Para crear un arreglo nuevo, se puede usar la función <code>np.array</code> pasándole como parámetro la lista de valores que deseamos agregar al arreglo:

x = np.array([6, 1, 3, 9, 8])

x

## Atributos del arreglo.

Al ser un objeto de python, el arreglo tiene una serie de atributos con los que podemos apoyarnos cuando se requiera conocer cierta información del mismo.

Para revisar una lista completa de los atributos, podemos hacerlo con la instrucción <code>help(np.ndarray)</code>

| Atributo | Descripcion                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------|
| shape    | Es una tupla que contiene el número de elementos (la longitud) para cada dimensión (eje) del arreglo. |
| size     | El número del total de elementos en el arreglo.                                                       |
| ndim     | El número de dimensiones (ejes)                                                                       |
| nbytes   | El número de bytes utilizados para almacenar los datos.                                               |
| dtype    | El tipo de dato de los elementos del arreglo.                                                         |

Todos los elementos del arreglo **tienen exactamente el mismo tipo**. Para crear un arreglo con números de tipo flotante, basta con que uno de los valores lo sea:

y = np.array([6.0, 1, 3, 9, 8])

y

y.shape

y.size

y.ndim

y.nbytes

y.dtype

## Modificar el tipo de dato del arreglo.

Otra opción es convertir el arreglo a otro tipo usando el método <code>astype</code>:

w = np.array([2, 6, 1, 12, 9])
z = np.array([7, 0, 9, 2])

w.astype(float)

z.astype(complex)

## Arreglos predefinidos.

Vamos a encontrar situaciones en donde será necesario ocupar arreglos, pero podemos aprovechar que existe una base para manejar los arreglos en python a partir de arreglos **predefinidos**.

A continuación enlistamos algunos de esos arreglos:

1. <code>np.zeros(n)</code> crea un arreglo de $n$ elementos, a cada uno se le asigna el valor de $0$ (cero).
2. <code>np.ones(n)</code> crea un arreglo de $n$ elementos, a cada uno se le asigna el valor de $1$ (uno).
3. <code>np.arange(a, b, c)</code>  crea un arreglo de forma similar a la función <code>range</code> , con las diferencias que $a$, $b$ y $c$ pueden ser reales, y que el resultado es un arreglo y no una lista.
4. <code>np.linspace(a, b, n)</code> crea un arreglo de $n$ valores equiespaciados entre $a$ y $b$, el valor por defecto es $n = 50$, pero se puede modificar.

a = np.zeros(6)

b = np.ones(5)

c = np.arange(3.0, 9.0)

d = np.linspace(1, 2, 5)

## Dimensiones del arreglo.

Debemos de hacer énfasis en señalar que hasta el momento, se han presentado arreglos unidimensionales. Más adelante veremos que es posible crear, manejar y utilizar arreglos con dos o tres dimensiones.

# Operación con arreglos.

Las limitaciones que tienen los arreglos respecto de las listas son compensadas por la cantidad de operaciones convenientes que permiten realizar sobre ellos.

**Punto importante:** Las operaciones aritméticas entre arreglos *se aplican elemento a elemento*


a = np.array([55, 21, 19, 11,  9])

b = np.array([12, -9,  0, 22, -9])


Veamos entonces algunas operaciones entre estos arreglos:

a + b

0.1 * a

a - 9.0

## Consideración sobre las operaciones.

Nótese que si quisiéramos hacer estas operaciones usando listas, necesitaríamos usar un ciclo <code>for</code> para hacer las operaciones elemento a elemento. Con los arreglos se simplifica bastante las operaciones entre los elementos.


## Operaciones relacionales.

Las operaciones relacionales también se aplican elemento a elemento, y devuelven un arreglo de valores booleanos:

a = np.array([5.1, 2.4, 3.8, 3.9])

b = np.array([4.2, 8.7, 3.9, 0.3])

c = np.array([5, 2, 4, 4]) + np.array([1, 4, -2, -1])/10.0

a < b

a == c


## Comparación con un solo resultado.

En una operación relacional es posible reducir el arreglo de booleanos a un único valor, con el uso de las funciones <code>any</code> y <code>all.any</code>.

La función <code>any</code> devuelve <code>True</code> si **al menos uno de los elementos es verdadero**, mientras que <code>all</code> devuelve <code>True</code> sólo si **todos los elementos son verdaderos**:

any(a < b)

any(a == b)

all(a == c)


# Funciones con arreglos.

El módulo <code>numpy<\code> provee muchas funciones matemáticas (recordemos que extiende al módulo <code>math</code>) que también operan elemento a elemento.


x = np.linspace(0, np.pi/2, 9)

x

## Evaluando con una función.

Cuando usamos una función y queremos evaluar los elementos de ésta, con el arreglo tendremos esta tarea en un solo paso:

np.sin(x)


## Ventaja de los arreglos.

Se hace evidente otra de las ventajas de los arreglos: al mostrarlos en la terminal, los valores aparecen perfectamente alineados. Con las listas, esto no ocurre:

list(np.sin(x))


# Valores aleatorios.

El modulo <code>numpy</code> contiene a su vez otras librerías que proveen funcionalidad adicional a los arreglos y funciones básicos.

La librería <code>numpy.random</code> provee funciones para generar números aleatorios (es decir, generados al azar, este tema lo abodaremos con mayor extensión en el Tema 5), de las cuales la función más usada es <code>random</code>, que entrega un arreglo de números al azar distribuidos uniformemente entre $0$ y $1$:

from numpy.random import random


random(3)

random(3)


# Funciones de utilidad.

Los arreglos proveen algunas funciones útiles que conviene conocer, para explorar el contenido de los mismos.

## Funciones para valores mínimos y máximos.

Las funciones <code>min</code> y <code>max</code>, devuelven respectivamente el valor mínimo y el máximo de los elementos del arreglo.

Considera que al usar arreglos todos los elementos son del mismo tipo de dato, podemos usar las funciones que operan con listas, pero debemos de garantizar que los datos son del mismo tipo.

a = np.array([4.1, 2.7, 8.4, np.pi, -2.5, 3, 5.2])

a.min()

a.max()

## Funciones que devuelven índices.

Las funciones <code>argmin</code> y <code>argmax</code> entregan respectivamente el índice en donde se ubica el elemento que es el mínimo del arreglo, así como el índice del elemento que es el máximo del arreglo:

a.argmin()

a.argmax()

## Funciones que operan sobre el arreglo.

Las funciones <code>sum</code> y <code>prod</code> devuelven respectivamente la suma y el producto de los elementos del arreglo:

a.sum()

a.prod()


# Productos entre arreglos.

## Producto vector - vector.

Recordemos que computacionalmente un arreglo es un sinónimo de un vector en una dimensión. Mientras que un arreglo en dos dimensiones sería el equivalente a una matriz.

El producto entre dos vectores se obtiene usando la función <code>numpy.dot</code>:

a = np. array([-2.8 , -0.88,  2.76,  1.3 ,  4.43])

b = np.array([ 0.25, -1.58,  1.32, -0.34, -4.22])

np.dot(a, b)

## El producto escalar.

Recordemos la definición de producto escalar:
$$
\begin{align*}
\overrightarrow{a} \cdot \overrightarrow{b} = \vert a \vert \, \vert b \vert \, \cos(\overrightarrow{a}, \overrightarrow{b})
\end{align*}
$$
Que es la definición el producto escalar utilizada para calcular el coseno del ángulo entre dos vectores.

El producto escalar se obtiene de:
$$
\begin{align*}
\overrightarrow{a} \cdot \overrightarrow{b} = a_{1} \, b_{1} + a_{2} \, b_{2} + a_{3} \, b_{3}
\end{align*}
$$

x = np.array([1, 2, 3])

y = np.array([-7, 8, 9])

producto = np.dot(x,y)

xmodulo = np.sqrt((x*x).sum())

ymodulo = np.sqrt((y*y).sum())

cos_angulo = producto / xmodulo / ymodulo

angulo = np.arccos(cos_angulo)

angulo

angulo * 360/2/np.pi

## Producto interno.

Aunque la función <code>dot</code> realiza el producto elemento con elemento de los arreglos, podemos utilizar propiamente la función <code>np.inner</code>, que evalúa el producto interno entre dos vectores.

a = np.array([1, 2, 3])

b = np.array([0,1,0])

np.inner(a, b)

## Diferencia entre <code>dot</code> e <code>inner</code>.

Si estamos manejando arreglos en una dimensión, las funciones <code>dot</code> e <code>inner</code> son las mismas.

Lo interesante es que con la función <code>dot</code> se puede operar **tensores**, claro en arreglos n-dimensionales.

## Producto externo.

El producto externo (producto cruz) es una operación binaria entre dos vectores en el espacio 3D. El resultado es un vector perpendicular a los dos vectores que se multiplican, además es normal al plano que contiene a aquéllos.

El producto cruz de los vectores $\overrightarrow{a}$ y $\overrightarrow{b}$ se define por:
$$
\begin{align*}
\overrightarrow{a} \times \overrightarrow{b} = \vert a \vert \, \vert b \vert \, \sin(\overrightarrow{a}, \overrightarrow{b}) \, \vert \overrightarrow{n} \vert
\end{align*}
$$
donde $\overrightarrow{n}$ es el vector unitario perpendicular al plano que contiene a los vectores $\overrightarrow{a}$ y $\overrightarrow{b}$, en la dirección dada por la regla de la mano derecha.

x = np.array([0., 0., 1.])

y = np.array([0., 1., 0.])

np.cross(x, y)

np.cross(y, x)

## Producto matriz - vector.

El producto matriz - vector es el **vector de los productos internos**. El producto matriz - vector puede ser visto simplemente como varios productos internos calculados de una sola vez.

Esta operación también es obtenida usando la función <code>np.dot</code> entre las filas de la matriz y el vector:

a = np.array([[-0.6,  4.8, -1.2],
            [-2. , -3.6, -2.1],
            [ 1.7,  4.9,  0. ]])

x = np.array([-0.6, -2. ,  1.7])

np.dot(a, x)

## Producto matriz - matriz.

El producto matriz - matriz es la matriz de los productos internos entre las filas de la primera matriz (de $m \times n$) y las columnas de la segunda (de $n \times p$).

El resultado es un arreglo de tamaño $m \times p$.


a = np.array([[ 2,  8],
            [-3,  7],
            [-8, -5]])

b = np.array([[-3, -5, -6, -3],
            [-9, -2,  3, -3]])

np.dot(a, b)

La multiplicación de matrices puede ser vista como varios productos matriz - vector (usando como vectores todas las filas de la segunda matriz), calculados de una sola vez.

## Resumen de operaciones.

En resumen, al usar la función <code>np.dot</code>, la estructura del resultado depende de cuáles son los parámetros que se utilizan:
1. <code>np.dot</code> (vector, vector) $\rightarrow$ número.
2. <code>np.dot</code> (matriz, vector) $\rightarrow$ vector.
3. <code>np.dot</code> (matriz, matriz) $\rightarrow$ matriz.

# Matrices como arreglos.

Las matrices o arreglos en 2D son importantes en el cómputo científico, <code>numpy</code> proporciona funciones que generan matrices predefinidas:

1. La función <code>np.identity</code>.
2. La función <code>np.eye</code>.
3. La función <code>np.diag</code>.

## La función <code>np.identity</code>.

La función <code>np.identity(n)</code> genera una matriz cuadrada de $n \times n$, los elementos de la diagonal son $1$ y los demás son $0$:

np.identity(4)

## La función <code>np.eye</code>.

La función <code>np.eye(n, k)</code> genera matrices cuadradas de $n \times n$ con elementos en la diagonal que valen $1$, permitiendo un desplazamiento (*offset*) sobre la diagonal: $k$.

El valor por defecto del desplazamiento es $k = 0$.

# Desplazamiento positivo

np.eye(3, k = 1)

# Desplazamiento negativo

np.eye(3, k = -1)

## La función <code>np.diag</code>.

Para crear una matriz con un arreglo unidimensional arbitrario en la diagonal, podemos utilizar la función <code>np.diag(v, k)</code>, que cuenta con un argumento opcional $k$ de desplazamiento sobre la diagonal, el valor por defecto es $k = 0$. Usa $k > 0$ para diagonales por arriba de la diagonal principal, con $k < 0$ para diagonales por debajo de la diagonal principal.

np.diag(np.arange(0, 20, 5))

np.diag(np.arange(0, 20, 5), 1)

np.diag(np.arange(0, 20, 5), -1)

# La librería <code>np.linalg</code>

Será necesario apoyarnos con la librería <code>np.linalg</code> para el manejo y operación tanto de arreglos como de matrices.

Se recomienda que revises la documentación oficial de python, para consultar las otras funciones que no manejaremos explícitamente en las presentaciones.

## Funciones para productos de matrices y vectores.

1. <code>dot</code>.
2. <code>vdot</code>.
3. <code>inner</code>.
4. <code>outer</code>.
5. <code>tensordot</code>.

## Descomposiciones para matrices.

1. <code>cholesky</code>.
2. <code>qr</code>.
3. <code>svd</code>.

Valores propios
\\
\bigskip
Funciones: <code>eig}, <code>eigh} (matriz Hermitiana o real), <code>eigs}, etc.
\end{frame}
\begin{frame}
\frametitle{Contenido de \texttt{np.linalg}}
Normas y otros valores
\\
\bigskip
Funciones: <code>norm}, <code>cond}, <code>det}, <code>matriz\_rank}, <code>trace}, etc.
\end{frame}
\begin{frame}
\frametitle{Contenido de \texttt{np.linalg}}
Solución de sistemas e inversión de matrices
\\
\bigskip
Funciones:  <code>solve}, <code>inv}, <code>tensorsolve}, <code>inv}, etc.   
\end{frame}

# Propiedades de las matrices.

## El determinante de una matriz.

El determinante de una matriz se calcula mediante la función <code>det</code>:

import numpy.linalg as nla


a = np.array([[ 3, -5, 8], [-1, 2, 3], [-5, -6, 2]])

nla.det(a)


## La traza de una matriz.

La traza de un arreglo o de una matriz se calcula con la función <code>np.trace</code>:

np.trace(a)

# Se hace un desplazamiento unitario por arriba de la diagonal principal.
np.trace(a, 1)

## La Matriz Inversa.

La matriz inversa se calcula con la función <code>linalg.inv</code>:

nla.inv(a)

## La matriz transpuesta.

La matriz transpuesta se obtiene con la función <code>matriz.T</code> o <code>matriz.transpose()</code>:

a.T


a.transpose()

# Solución de sistemas algebraicos.

Un sistema de ecuaciones algebraico se puede expresar en términos de un arreglo matricial:
$$
\begin{align*}
\begin{aligned}
a_1 \: x + b_1 \: y + c_1 \: z = d_1 \\
a_2 \: x + b_2 \: y + c_2 \: z = d_2 \\
a_3 \: x + b_3 \: y + c_3 \: z = d_3 
\end{aligned}
\Longrightarrow
\begin{pmatrix}
a_1 & b_1 & c_1 \\ 
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3 
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix} = 
\begin{pmatrix}
d_{1} \\
d_{2} \\
d_{3}
\end{pmatrix}
\end{align*}
$$

Existen métodos y funciones con python para resolver sistemas de ecuaciones algebraicas.

Tomemos en cuenta que:
1. La solución de sistemas matriciales es computacionalmente una tarea intensa.
2. Veremos algunos métodos para resolver estas ecuaciones.
3. Estos métodos están contenidos en la librería <code>np.linalg</code>.

## La función <code>linalg.solve</code>.

Esta función utiliza la matriz de coeficientes y el vector del lado derecho de la igualdad como argumentos, devuelve un vector con la solución.

Consideremos el siguiente sistema:

$$
\begin{align*}
4 \: x - 5 \: y + 8 \: z &= 4 \\
2 \: x - 8 \: y + 7 \: z &= 0 \\
-5 \: x - 8 \: y &= 4
\end{align*}
$$

a = np.array([[4, -5, 8], [2, -8, 7], [-5, 8, 0]])

b = np.array([4, 0, -5])

x = nla.solve(a, b)

## Comprobando la solución.

Para revisar que el vector $x$ es solución del sistema de ecuaciones, realizamos la siguiente instrucción.


np.allclose(np.dot(a, x), b)

## Consideración importante.

La matriz de coeficientes debe de ser **no singular**, es decir, el determinante de esa matriz debe de ser distinto de cero:

a2 = np.array([[4, -5, 8], [8, -10, 16], [-5, 8, 0]])

b2 = array([4, 8, -5])

nla.det(a2)

# Esta instrucción nos devolverá un error

x2 = nla.solve(a2, b2)


## Sistemas algebraicos grandes.

Los sistemas algebraicos con un número muy grande de ecuaciones, implican una carga computacional elevada para resolverlo. Existen varios métodos especializados para resolver eficientemente esos grandes sistemas de ecuaciones.

**¿Qué es un número grande?**

La pregunta que nos planteamos es: ¿en qué momento se considera que ya tenemos un número grande para un sistema de ecuaciones?

Vamos a considerar un *sistema de ecuaciones grande*, cuando el tamaño de la matriz sea mayor o igual a $50 \times 50$.

# Para practicar.

Utilizando las funciones que se revisaron en este Notebook:

## Matrices singulares.

Identifica cuáles de las siguientes matrices son singulares:

$$
\mathbf{A_{1}} =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 3 & 4 \\
3 & 4 & 5
\end{pmatrix}$$


$$\mathbf{A_{2}} =
\begin{pmatrix}
2.11 & -0.80 & 1.72 \\
-1.84 & 3.03 & 1.29 \\
-1.57 & 5.25 & 4.30
\end{pmatrix}$$

$$\mathbf{A_{3}} =
\begin{pmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2
\end{pmatrix}$$

$$ \mathbf{A_{4}} =
\begin{pmatrix}
4 & 3 & -1 \\
7 & -2 & 3 \\
5 & -18 & 13
\end{pmatrix}$$ 

## Elaborando una matriz.

Considera una matriz $M$ de $4 \times 3$:
$$
\begin{align*}
M = 
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
10 & 11 & 12
\end{bmatrix}
\end{align*}
$$

Construye esta matriz usando la función <code>array</code>. Claramente tendrás que ingeniártelas para ello, no esperamos una solución trivial (escribirla a mano), deberás de usar una estrategia  con las funciones vistas en la presentación para obtenerla.

## Solución de sistemas de ecuaciones.

Resuelve los siguientes sistemas de ecuaciones, debiendo revisar la respectiva propiedad de no singularidad y demostrar que la solución obtenida es consistente con $A \, x =  b$.

$$
\begin{align*}
2 \, x_{1} + x_{2} - 3 \, x_{3} &= -1 \\
-x_{1} + 3 \, x_{2} + 2 \, x_{3} &= 12 \\
3 \, x_{1} + x_{2} - 3 \, x_{3} &= 0
\end{align*}
$$

$$
\begin{align*}
0.1 \, x_{1} - 0.6 \, x_{2} + x_{3} &= 0 \\
-2 \, x_{1} + 8 \, x_{2} + 0.3 \, x_{3} &= 1 \\
x_{1} + 6 \, x_{2} + 4 \, x_{3} $= 2
\end{align*}
$$

$$
\begin{align*}
4 \, x + y - z &= 9 \\
3 \, x + 2 \, y - 6 \, z &= -2 \\
x - 5 \, y + 3 \, z &= 0
\end{align*}
$$

## Operando matrices

Calcula:
1. $C \equiv A + B$,
2. $D \equiv A - B$,
3. $E \equiv A \, B$,

donde:
$$
\begin{align*}
A = \begin{bmatrix}
1 & 2 & 3 \\
0 & 1 & 4 \\
3 & 0 & 2
\end{bmatrix}
\end{align*}
$$

$$
\begin{align*}
B = \begin{bmatrix}
4 & 1 & 2 \\
3 & 2 & 1 \\
0 & 1 & 2
\end{bmatrix}
\end{align*}
$$

## Matriz de Hilbert.


La matriz $A$ es la **matriz de Hilbert** de $5 \times 5$ dada por:
$$
\begin{align*}
A = [a_{i, j}] \quad \text{donde} \quad a_{i, j} = \dfrac{1}{i + j -1}
\end{align*}
$$
Con un código genera la matriz de Hilbert y calcula:
1. $A^{-1}$
2. $A^{-1} \, A$
3. $(A^{-1})^{-1} \, A^{-1}$
