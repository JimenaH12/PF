## ¿Como iniciar?
descargue el codigo del repositorio de este github en el mismo directorio que tu script de python.

    tu_proyecto/
    │
    ├── metodos/
    │   ├── __init__.py
    │   └── proyecto.py
    │
    └── tu_script.py

Dentro de `tu_script.py` ahora puedes importar las funciones como: `inicio()` funcion de `metodos.proyecto`
module:

    # tu_script.py
    from metodos.proyecto import inicio
    
    
Después de importar la función, se puede usar agregando los datos que solicita en este caso tres np.array el primero para los potenciales de t, el sugundo para los potenciales de epsilon y el tercero es para los puntos temporales para eso podemos utilizar la siguiente configuracion:

	#tu_script.py
	from metodos.proyecto import inicio
	N = 100                         # Tamaño de la grilla donde se ubicara el fermion
	epsilon_val = 0.5 * np.ones(N)  #valores de potencial 
	t_i_val = 1 * np.ones(N)        # valores relacionados a la probabilidad del movimiento para el fermion dentro de la grilla
	tiempos_val = np.linspace(0.0, 25, 200)  # puntos temporales en los que se desea evaluar la evolucion de la grilla

	s = inicio(t_i_val, epsilon_val, tiempos_val)
	
asi ya tenemos un np.array con la probabilidad de encontrar el fermion para cada uno de los puntos de la grilla.
si quisieras crear una animacion de la evolucion temporal para la probabilidad de encontrar el fermion en cada punto de la grila podrias usar el siguiente codigo:
	#tu_script.py
	from metodos.proyecto import inicio
	import matplotlib.pyplot as plt
	from matplotlib.animation import FuncAnimation 
	
	N = 100                         # Tamaño de la grilla donde se ubicara el fermion
	epsilon_val = 0.5 * np.ones(N)  #valores de potencial 
	t_i_val = 1 * np.ones(N)        # valores relacionados a la probabilidad del movimiento para el fermion dentro de la grilla
	tiempos_val = np.linspace(0.0, 25, 200)  # puntos temporales en los que se desea evaluar la evolucion de la grilla

	s = inicio(t_i_val, epsilon_val, tiempos_val)

	# Animación
	fig = plt.figure(figsize=(10, 6))
	ax = plt.axes(xlim=(0, N), ylim=(0, 0.5))
	line, = ax.plot([], [])
	# Texto estático para mostrar t y epsilon
	ax.text(0.02, 0.95, 't = {:.1f}'.format(t_i_val[0]), 		transform=ax.transAxes, fontsize=12, verticalalignment='top')
	ax.text(0.02, 0.90, 'epsilon = {:.1f}'.format(epsilon_val[0]), 	transform=ax.transAxes, fontsize=12, verticalalignment='top')
	# Función para la animación
	skip = 1
	def animate(frame):
    		x = np.arange(N)
   		y = s[frame * skip]
    		line.set_data(x, y)
    	# Actualizar texto con el tiempo actual
    	time_text.set_text('Tiempo = {:.1f}'.format(tiempos_val[frame * skip]))

    	return line, time_text

	# Añadir texto para mostrar el tiempo
	time_text = ax.text(0.85, 0.95, '', transform=ax.transAxes, color='blue')
	# Título de la animación y etiquetas de los ejes
	plt.title('Evolucion temporal de la probabilidad de encontrar el 		fermion para cada punto en la grilla')
	plt.xlabel('Distribucion espacial de los puntos de la grilla')
	plt.ylabel('Probabilidad de encontrar el fermion')
	anim = FuncAnimation(fig, animate, frames=len(s)//skip, interval=40)
	# Guardar la animación como archivo MP4
	anim.save('animacion.mp4', writer='ffmpeg')
	plt.close()
	
Con este codigo puedes generar una animacion de la evolucion temporal de probabilidad de encontrar el fermion para cada punto de la grilla y esta animacion se guardara en la carpeta donde ejecutes el script con formato de video de mp4
