from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):

		student_code = input("dame la matricula: ")
		student_name = input("dame el nombre: ")
		student_age = input("dame la edad: ")
		student_gender = input("dame el genero: ")
		student_carreer = input("dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		
		count = count + 1
	return list_students


def ordena_edades(list_students):
	list_students = [4,12,8,2,1]

for recorrido in range(1,len(list_students)):
	for posicion in range(len(list_students)-recorrido):
		if list_students[posicion] > list_students[posicion + 1]:
		temp= list_students[posicion]
		list_students[posicion] = list_students [posicion + 1]
		list_students[posicion + 1] = temp

print list_students

def separa_generos(list_students):
	list_students = [4,12,8,2,1]
	list_male=[]
	list_female=[]

for recorrido in range(1,len(list_students)):
	for posicion in range(len(list_students)-recorrido):
		if student_gender = 'male':
			list_male=list_students.genero
		  else list_female=list_students

print list_students


	print ("metodo vacio")

def main():
	
	options = 1
	list_stud = []

	while options != "0":
		options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")

		if options == "1":
			print("crea estudiantes")
			count_x = input("cuantos estudiantes daremos de alta: ")
			list_stud = crea_estudiantes(count_x)

		if options == "2":
			print("ordena edades")

		if options == "3":
			print("separa generos")

if __name__ == "__main__":
	main()
