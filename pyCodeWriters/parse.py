fileR = open('misc.txt', 'r')
f = open('parseF.txt', 'a')
lastStrVal= ''
while 1:
	line = fileR.readline()
	if not line:
		break	
	lineW = line.strip()	
	lineS = lineW.split('|')
	i = 0
	for item in lineS:
		i = i+1
	f.write("\n\nCLLocationCoordinate2D %sLocs[%d];\n" %(lineS[0], i-1))
	j =0
	for itemS in lineS:
		if(j==0):
			pass
		else:
			itemSSpl = itemS.split(',')
			if (itemSSpl[0]!=''):
				f.write("\n%sLocs[%d].longitude=%s;" %(lineS[0], (j-1), itemSSpl[0]))
				f.write("\n%sLocs[%d].latitude=%s;" %(lineS[0], (j-1), itemSSpl[1]))	
		j=j+1
	lastStrVal = '\nMKPolygon *pol%s = [MKPolygon polygonWithCoordinates:%sLocs count:%d];\n[mapView addOverlay:pol%s];\n'%(lineS[0], lineS[0], (i-1), lineS[0]) + lastStrVal
f.write(lastStrVal)	
f.close()					
fileR.close()	
	#f = open('parse.txt', 'a')
	

'''
textSp1 = text.split('|')
j=0
for item in textSp1:
	textSp2 = item.split(',') 
	i =0
	for itemS in textSp2:
		if(i==0):
			f.write("\nuanaLocs[%d].latitude=%s;" %(j,itemS))
		if(i==1):
			f.write("\nuanaLocs[%d].longitude=%s;" %(j,itemS))	
		i=i+1
	j=j+1
f.write("\nMKPolygon *polUana = [MKPolygon polygonWithCoordinates:uanaLocs count:];\n[mapView addOverlay:polUana];")		
'''
exit()