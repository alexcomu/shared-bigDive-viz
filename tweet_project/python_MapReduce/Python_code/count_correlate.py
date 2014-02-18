file = open("../res1_hashCorrelati.txt","r")
lista = {}
for line in file.readline().split(','):
	l = line.split()
	nome = l[0][1:-2].lower()
	try:
		valore = int(l[1])
		if nome not in lista:
			lista[nome] = 0
		lista[nome] += valore
	except:
		pass

inizio = '''
{
 "name": "#Egypt",
 "size": 5000,
 "group": 1,
 "children": [
 '''
print inizio,
cont = 2
for a in lista:
	if lista[a] > 100:
		#print a, ': ',  lista[a]
		print '{"name": "',a,'","size":',lista[a]/5,',"group": ',cont,'},'
		cont += 1
print ']}'

