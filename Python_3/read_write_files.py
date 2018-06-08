fw = open('test.txt', 'w')
fw.write('Writing some stuff in my text file 1.\n')
fw.write('Writing some stuff in my text file 2.\n')
fw.close()

fr = open('test.txt', 'r')
text = fr.read()
print(text)
fr.close()
