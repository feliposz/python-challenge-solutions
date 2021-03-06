import gzip,difflib
deltas=gzip.GzipFile('deltas.gz', 'rb').read().decode()
deltas=deltas.splitlines()
left,right,png=[],[],['','','']
for row in deltas:
    left.append(row[:53])
    right.append(row[56:])
diff = list(difflib.ndiff(left,right))

for row in diff:
    bytes = [chr(int(byte,16)) for byte in row[2:].split()]
    if row[0]=='-': png[0]+=''.join(bytes)
    elif row[0]=='+': png[1]+=''.join(bytes)
    elif row[0]==' ': png[2]+=''.join(bytes)

for i in range(3):
    open('18_%d.png' %i,'wb').write(png[i].encode("latin_1"))
