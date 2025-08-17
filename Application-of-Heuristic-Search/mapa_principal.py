def mapa_para_matriz(mapa_str):
    matriz = []
    for linha in mapa_str.strip().split("\n"):
        row = []
        for cell in linha.split("\t"):
            if cell == "G":
                row.append(10)
            elif cell in ("S", "D"):
                row.append(20)
            elif cell == "F":
                row.append(100)
            elif cell == "M":
                row.append(150)
            elif cell == "A":
                row.append(180)
            elif cell in ("D", "W", "E"):
                row.append(10)
            else:
                row.append(9999)    
        matriz.append(row)
    return matriz

main_map_str = """ 
F	F	F	F	F	F	F	F	F	F	F	F	F	F	F	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M
F	G	E	F	G	F	G	F	G	G	G	G	G	G	G	M	M	M	M	M	M	M	S	S	D	S	S	M	M	M	M	M	M	S	S	S	S	M	M	M	M	M
F	G	G	F	G	G	G	F	G	F	G	G	G	G	G	G	G	M	M	M	M	S	S	S	S	S	S	S	M	M	M	M	S	S	S	S	S	S	M	M	M	M
F	G	F	F	G	F	G	F	G	F	G	G	F	G	G	G	G	M	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	S	M	M
F	G	G	G	G	F	G	F	G	F	G	G	F	G	G	G	G	M	S	M	M	S	S	S	S	S	S	S	M	M	M	M	S	S	S	S	S	S	M	M	M	M
F	G	F	F	G	F	W	F	G	F	G	F	F	F	G	G	G	M	S	M	M	M	S	S	S	S	S	M	M	M	M	A	M	S	S	S	S	M	A	M	M	M
F	G	F	F	G	F	G	G	G	F	G	G	G	G	G	G	G	M	S	M	M	M	M	M	M	M	M	M	M	M	M	A	M	M	M	M	M	M	A	M	M	M
F	G	F	F	F	F	G	F	F	F	G	G	G	G	G	G	G	M	S	M	M	M	M	M	M	M	M	M	M	M	M	A	M	M	M	M	M	M	A	M	G	M
F	G	G	F	G	G	G	G	G	F	G	G	A	G	G	G	G	M	S	S	S	S	S	S	S	S	S	S	S	M	M	A	M	M	M	M	M	M	A	M	G	M
F	F	F	F	G	F	F	F	G	G	G	A	A	A	G	G	G	M	S	M	M	M	M	M	S	M	M	M	S	M	M	A	M	M	M	M	M	M	A	M	G	M
F	G	G	F	G	G	G	G	G	G	A	A	A	A	A	G	G	M	M	M	F	F	F	M	M	M	F	F	F	F	F	A	G	G	M	M	G	G	A	G	G	M
F	G	G	F	G	G	F	G	G	G	G	A	A	A	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	A	A	A	A	A	A	A	A	A	G	G	M
F	G	G	F	G	G	F	G	G	G	G	G	A	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	A	G	G	F	G	G	G	G	G	F	G	M
F	G	G	F	G	G	F	G	G	G	G	G	G	G	G	G	G	F	F	F	G	G	G	F	F	F	F	G	G	G	A	G	G	G	G	G	G	F	G	F	G	M
F	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	A	G	F	G	F	G	F	F	G	F	G	M
F	G	F	F	F	F	F	G	F	F	F	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	A	G	G	G	G	G	G	G	G	G	G	M
F	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	A	A	A	A	A	A	A	A	A	A	G	G	G	G	G	M	M	M	M	M	M	M	M	M	M
F	G	G	G	G	G	G	G	G	A	G	G	F	G	F	G	G	A	G	G	G	G	G	G	G	G	A	G	G	G	A	G	M	S	S	S	S	S	S	D	S	M
F	G	F	G	G	F	G	G	G	A	G	G	G	G	G	G	G	A	G	F	G	G	G	G	F	G	A	A	A	A	A	G	M	S	M	S	S	M	S	S	S	M
F	G	F	G	G	F	G	G	G	A	G	G	F	G	F	G	G	G	G	G	G	G	G	G	G	G	A	G	G	G	G	G	M	S	M	M	M	M	M	M	M	M
F	G	F	G	G	F	G	G	G	A	G	G	G	G	G	G	G	A	G	G	G	G	G	G	G	G	A	G	G	G	M	G	M	S	S	S	S	S	S	S	S	M
F	G	F	G	G	F	G	G	G	A	G	F	F	F	F	G	G	A	G	F	G	G	G	G	F	G	G	G	G	G	M	G	M	S	M	M	M	M	S	M	M	M
F	G	G	G	G	G	G	G	G	A	G	G	G	G	G	G	G	A	G	G	G	G	G	G	G	G	A	G	M	G	M	G	M	S	S	S	S	S	S	S	S	M
F	G	G	G	G	G	G	G	G	G	G	F	F	F	F	G	G	A	A	A	A	G	G	A	A	A	A	G	M	G	M	G	M	M	M	S	S	M	M	M	M	M
F	F	F	F	F	F	F	G	G	F	F	F	F	F	F	F	F	F	G	G	G	G	G	G	G	G	A	G	M	G	M	G	G	G	G	G	G	G	G	G	G	M
F	F	F	F	F	F	G	G	F	F	F	F	F	G	F	F	F	F	F	G	F	F	F	G	G	G	A	G	M	G	G	G	G	G	G	G	G	G	G	G	G	M
F	G	F	G	F	G	G	G	F	F	F	F	G	G	G	F	F	F	F	G	F	F	F	G	G	G	A	G	M	G	G	G	M	M	M	M	M	M	M	M	M	M
M	G	G	G	F	G	G	G	F	F	F	G	G	G	G	G	F	F	F	G	G	G	G	G	L	G	A	G	G	G	G	G	G	G	G	M	G	G	G	G	G	M
M	G	G	G	F	G	G	G	F	F	F	F	G	G	G	F	F	F	F	G	F	G	G	G	G	G	A	G	G	G	G	G	G	G	G	M	G	G	G	G	G	M
M	G	G	G	G	G	G	G	G	F	F	F	F	G	F	F	F	F	G	G	F	G	G	G	G	G	A	A	A	G	A	A	A	A	G	M	G	M	M	M	M	M
M	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	A	G	G	G	G	G	G	G	M
M	M	M	M	M	M	M	M	M	G	G	G	G	M	M	M	M	M	M	M	G	G	M	M	M	M	G	G	G	G	G	G	G	A	M	M	M	M	M	M	G	M
M	S	S	S	S	D	S	S	M	G	G	G	G	M	G	G	G	G	G	G	G	G	G	G	G	M	G	G	G	G	G	G	G	A	M	M	M	M	M	M	M	M
M	S	M	M	S	S	S	S	M	G	G	G	G	M	G	G	G	G	G	G	G	G	F	G	G	M	G	G	A	A	A	A	A	A	A	A	M	M	A	A	M	M
M	S	M	M	S	S	S	S	M	G	G	G	G	M	G	F	G	G	A	A	G	G	F	G	G	M	G	G	A	A	M	A	A	A	A	A	M	M	A	A	M	M
M	S	S	S	S	S	S	S	M	G	G	M	G	M	G	G	G	G	A	A	G	G	F	G	G	M	G	G	A	A	A	A	M	M	A	A	M	M	A	A	M	M
M	S	S	S	S	S	S	S	M	G	G	M	G	G	G	G	G	G	G	G	G	G	G	G	G	M	G	G	A	A	A	A	M	M	A	A	M	M	A	A	M	M
M	S	S	S	S	S	S	M	M	M	M	M	G	G	F	G	G	G	G	G	F	F	F	G	G	M	G	G	A	A	A	A	A	A	A	A	M	M	A	A	M	M
M	S	S	S	S	S	S	S	S	M	M	M	G	G	F	G	A	A	A	G	G	F	G	G	G	M	G	G	A	A	A	A	A	A	A	A	M	M	A	A	M	M
M	S	S	S	S	S	S	S	S	M	M	M	G	G	F	G	G	G	G	G	G	F	G	G	G	M	G	G	A	A	A	A	A	A	A	A	A	A	A	A	M	M
M	S	S	S	S	S	S	S	S	S	G	G	G	G	G	G	G	G	G	G	G	G	G	G	G	M	M	M	A	A	A	A	A	A	A	A	A	A	A	A	M	M
M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M	M
"""

Hyrule = mapa_para_matriz(main_map_str)