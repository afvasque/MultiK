import csv

#Pregunta, malas, buenas
report_list = {}
report_by_student = {}

with open('multik.log', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		# Ignorar excepciones loggeads
		if len(row) > 1:
			if "ANSWER" in row[1]:
				#Si la pregunta no esta en el reporte
				pregunta = row[3] + " " + row[2]
				if pregunta not in report_list:
					report_list[pregunta] = {"malas":0, "totales":0}
				if  "WRONG_ANSWER" in row[1]:
					report_list[pregunta]["malas"] += 1
				report_list[pregunta]["totales"] += 1
				
				#print(row[1])
				#print("Id alumno: ", row[0][row[0].find(" ") + 2:])
				#print("Pregunta: ", row[3])
				#count += 1
				#if "WRONG_ANSWER" in row[1]:
				#	print("Respuesta correcta: ", row[5])
				#	print("Respuesta ingresada: ", row[4])

for row in report_list:
	porcentaje_error = (report_list[row]["malas"]/float(report_list[row]["totales"]))
	report_list[row]["porcentaje_error"] = porcentaje_error

with open('results.csv', 'wb') as f:
	f.write("Pregunta,Malas,Totales,Porcentaje\n")
	for k in report_list:
		f.write(k + "," + str(report_list[k]["malas"]) + "," + str(report_list[k]["totales"]) + "," + str(report_list[k]["porcentaje_error"])  + "\n")


			
