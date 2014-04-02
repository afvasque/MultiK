import csv

alumno_nombre = {}

#Curso va en mayusculas, ej: 3A
def obtener_lista(curso):
	print("Leyendo lista")
	filepath = "ListasCSV/"+ curso + ".csv"
	with open(filepath, 'rb') as csvfile:
		lenguajereader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
		
		for row in lenguajereader:
			alumno_nombre[row[0]] = row[1]
		
	# Agregamos numeros con nombres aleatorios por si no se encuentran en la lista
	for i in range(90,100):
		alumno_nombre[str(i)] = "estudiante"

	return alumno_nombre
		