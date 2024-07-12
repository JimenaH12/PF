# Método numérico para la solución 

## Introducción 

Al considerar el modelo de tight binding, para el caso de un solo fermión en la grilla, la metodologı́a que permite una mejor manera para implementar la solución numérica, con una buena aproximación de la evolución temporal, se reduce al método numérico Runge-Kutta de 4$^{\rm to}$ Orden. No obstante, para comprender los argumentos númericos que permiten dicha solución se requiere comprender el funcionamiento del método.  

Ahora bien, al evaluar diferentes sistemas, desde los más sencillos, como resolver una ecuación diferencial o hasta nuestro caso, una matriz Hamiltoniana de dimensión N de carácter tridiagonal, se conocen diversos métodos numéricos para su resolución. El método numérico Runge-Kutta de 4$^{\rm to}$ Orden está diseñado para enfrentarse a sistemas de tamaño considerable, como dicha matriz. Asimismo, para entender su funcionanmiento, se debe regresar a lo simple y así ver como este se va complementando a partir métodos más sencillos, como el Método Euler. 

### Método Euler 

La expansión de Taylor nos proporciona una forma de entender cómo avanzar en el tiempo \( h \) utilizando la derivada de una función \( x(t) \):

$$ x(t+h) = x(t) + h\frac{dx}{dt} + \frac{h^2}{2}\frac{d^2x}{dt^2} + O(h^3) $$

Para avanzar en el tiempo por un paso \( h \), utilizamos la aproximación:

$$ x(t + h) = x(t) + hf(x,t). $$

El error asociado con esta aproximación está relacionado con la cantidad de pasos \( N \) que tomamos en el tiempo:

$$ \sum_{\text{errores}} = \sum_{k=0}^{N-1} \frac{h^2}{2} \left. \frac{d^2x}{dt^2} \right|_{x_k, t_k} \approx \frac{h}{2} \sum_{k=0}^{N-1} h \left. \frac{df}{dt} \right|_{x_k, t_k} \approx \frac{h}{2} [f_b - f_a]. $$

Donde asumimos \( N = \frac{b-a}{h} \) pasos temporales para llegar al punto final.

El error total de aproximación depende linealmente de \( h \) multiplicado por el intervalo de integración \( [a, b] \).

#### Algoritmo de Euler

El algoritmo para aplicar el método de Euler es el siguiente:

1. Empezamos con \( t = t_0 \) y \( x = x_0 \).
2. Discretizamos el tiempo en pasos de tamaño \( h \), donde cada punto en el tiempo está denotado por \( t_i \).
3. Para cada punto en el tiempo, calculamos \( x \) utilizando el resultado de la iteración anterior: \( x_i = x_{i-1} + hf(x_{i-1}) \).

Después de comprender el método Euler, el cual puede darnos una buena aproximación dependiendo del problema y de la cantidad de iteraciones que necesitamos en nuestra solución, se entiende que se requiere un método distinto. Esto se debe a que la solución de un sistema más complejo le tomaría muchos recursos computacionales, lo cual puede evitarse con la implementación de los métodos contenidos en la rama Runge-Kutta. 

### Método de Runge-Kutta

El método de Runge-Kutta es en realidad una familia de métodos de distinto orden que proveen una mejor aproximación sin la necesidad de considerar ordenes más altos en la expansión de Taylor del método de Euler. Este último punto se quiere evitar, dado que su complejidad es muy elevada para la situación presente. Por esta razón, se introducen los métodos Runge-Kutta 2$^{\rm do}$ Orden (RK2) y Runge-Kutta de 4$^{\rm to}$ Orden. 

### Método de Runge-Kutta 2$^{\rm do}$ Orden (RK2)

La idea del método RK2 es utilizar el punto medio para evaluar el método de Euler, como se indica en la figura. Mientras que el método de Euler se aplica en el punto $t$ para evaluar la derivada para aproximar la función en el punto $x = t + h$, el método RK2 utiliza el punto medio $t + h/2$. 

De esta forma, se alcanza una mejor aproximación para el mismo valor de $h$.

Para avanzar en el tiempo con el método de Runge-Kutta de segundo orden (RK2), aplicamos la serie de Taylor alrededor del punto medio \( t + \frac{h}{2} \):

\[ x(t + h) = x \left( t + \frac{h}{2} \right) + \frac{h}{2} \left. \frac{dx}{dt} \right|_{t + \frac{h}{2}} + \frac{h^2}{8} \left. \frac{d^2x}{dt^2} \right|_{t + \frac{h}{2}} + O(h^3) \]

De manera similar, para \( x(t) \), tenemos:

\[ x(t) = x \left( t + \frac{h}{2} \right) - \frac{h}{2} \left. \frac{dx}{dt} \right|_{t + \frac{h}{2}} + \frac{h^2}{8} \left. \frac{d^2x}{dt^2} \right|_{t + \frac{h}{2}} + O(h^3) \]

Al restar estas ecuaciones, obtenemos la expresión final del método RK2:

\[ x(t + h) = x(t) + h \left. \frac{dx}{dt} \right|_{t + \frac{h}{2}} + O(h^3) \]

Este método proporciona una aproximación con un error de orden \( O(h^3) \) en cada paso de tiempo, lo cual lo hace más preciso que el método de Euler para el mismo número de pasos temporales.

### Método de Runge-Kutta de 4$^{\rm to}$ Orden

La metodología anterior se puede aplicar aún a más puntos ubicados entre $x(t)$ y $x(t + h)$ realizando expansiones de Taylor. De esta forma se pueden agrupar términos de orden $h^3$, $h^4$, etc; para cancelar dichas expresiones. 

El problema de hacer esto es que las expresiones se vuelven más complicadas conforme incrementamos el orden de aproximación. En general, la regla de dedo es que el $4^{\rm to}$ orden corresponde al mejor compromiso entre complejidad y error de aproximación. Este método es el más utilizado comunmente para resolver diferentes sistemas.  

El álgebra para encontrar las ecuaciones de $4^{\rm to}$ orden es tediosa, pero el resultado final es
* $k_1 = hf(x, t)$,
* $k_2 = hf\left(x + \frac{k_1}{2}, t+\frac{h}2\right)$,
* $k_3 = hf\left(x + \frac{k_2}{2}, t+\frac{h}2\right)$,
* $k_4 = hf\left(x + k_3, t + h \right)$,
* $x(t+h) = x(t) + \frac{1}{6}(k_1 + 2 k_2 + 2k_3 + k_4)$.

Para la mayoría de aplicaciones, el método RK4 es el método de-facto para obtener soluciones. Es fácil de programar y devuelve resultados precisos. 

El error de aproximación es $O(h^5)$, mientras que el error global es aproximadamente del orden $O(h^4)$.

Finalmente, después de comprender el funcionamiento de los diferentes métodos de solución numérica, se puede observar que el método Runge-Kutta de 4$^{\rm to}$ Orden muestra una mejor presión, especialmente cuando se requiere alta precisión en la evolución temporal de la función en la ecuación de Schrödinger, además de su eficiencia computacional y facilidad de implementación. Proporciona resultados numéricos confiables y precisos para la evolución temporal de la función, cumpliendo con los requisitos exigidos por la física cuántica en este contexto.
