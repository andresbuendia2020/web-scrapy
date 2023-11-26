import re
from colorama import Fore
import requests

website = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
website1 = "https://www.vulnhub.com"

resultado = requests.get(website1)
content = resultado.text

patron = r"/entry/[\w-]*"
maquinas_repetidas = re.findall(patron, str(content))
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []

for i in sin_duplicados:
	nombre_maquinas = i.replace("/entry/", "")
	maquinas_final.append(nombre_maquinas)
	print (nombre_maquinas)

	########################################################################

	maquina_noob = "noob-1"
	existe_noob = False

	for a in maquinas_final:
		if a == maquina_noob:
			existe_noob = True
			break

		color_verde = Fore.GREEN
		color_rojo = Fore.YELLOW

	if existe_noob == True:
		print ("\n" + color_rojo + "Maquinas existentes")
	else:
		print ("\n" + color_verde + "Maquina nueva!!!")
