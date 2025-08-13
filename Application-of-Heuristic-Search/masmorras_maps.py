def mapa_para_matriz(mapa_str):
    matriz = []
    for linha in mapa_str.strip().split("\n"):
        row = []
        for cell in linha.strip().split("\t"):
            if cell == "X":
                row.append(9999)
            elif cell in ("P", "E"):
                row.append(1)
            else:
                row.append(10)
        matriz.append(row)
    return matriz

masmorra1_str = """
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
X				X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X				X	X	X	X
X				X	X	X	X	X	X	X	X				X	X	X	X	X	X				X	X	X	X
X	X		X	X	X	X							P		X	X	X	X	X	X				X	X	X	X
X	X		X	X	X	X		X	X	X	X				X	X	X	X	X	X	X		X	X	X	X	X
X	X							X	X	X	X	X	X	X	X	X	X	X	X	X	X		X	X	X	X	X
X	X		X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X		X	X	X	X	X
X	X		X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X								X	X
X	X		X	X	X	X	X	X	X	X						X	X	X								X	X
X	X							X	X	X						X	X	X								X	X
X	X	X		X	X	X		X	X	X						X	X	X								X	X
X	X	X		X	X	X		X	X	X	X	X		X	X	X	X	X	X	X	X		X	X	X	X	X
X	X				X	X		X	X	X	X	X		X	X	X	X	X	X	X	X		X	X	X	X	X
X	X				X	X		X	X	X	X	X		X	X	X	X	X	X	X	X						X
X	X				X	X		X	X	X	X	X		X	X	X	X	X	X		X	X	X		X	X	X
X	X	X	X	X	X	X															X	X	X		X	X	X
X	X	X	X	X	X	X		X	X	X	X	X	X	X	X	X	X	X	X		X	X	X		X	X	X
X	X	X	X	X	X	X		X	X	X	X	X	X	X	X	X	X	X	X		X	X	X		X	X	X
X	X				X	X		X	X				X	X	X	X	X					X	X		X	X	X
X	X												X	X	X	X	X					X	X		X	X	X
X	X				X	X		X	X				X	X	X	X	X					X	X		X	X	X
X	X	X	X	X	X	X		X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X		X	X	X
X	X	X	X	X	X	X		X	X	X	X	X	X												X	X	X
X	X	X	X	X	X					X	X	X	X		X	X	X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X					X	X	X	X		X	X	X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X					X	X						X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X	X	X	X	X	X	X			E			X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
"""

masmorra2_str  = """
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
X	X						X	X	X	X	X				X	X	X	X	X	X	X	X	X	X	X	X	X
X	X									X	X		P		X	X	X					X	X	X	X	X	X
X	X						X	X		X	X				X	X	X	X	X	X		X	X	X	X	X	X
X	X	X	X		X	X	X	X		X	X	X		X	X	X	X	X	X	X		X					X
X	X	X	X		X	X	X	X											X	X							X
X	X	X	X		X	X	X	X	X	X	X	X		X	X	X	X		X	X	X	X					X
X	X						X	X	X	X	X	X	X	X	X	X	X		X	X	X	X					X
X	X																		X	X	X	X	X	X		X	X
X	X						X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X		X	X
X	X	X	X		X	X	X	X	X	X	X	X	X									X	X	X		X	X
X	X	X	X		X	X	X	X	X	X	X	X	X									X	X	X		X	X
X	X	X	X		X	X						X	X									X	X	X		X	X
X	X														X	X	X		X	X	X	X	X	X		X	X
X	X	X	X	X	X	X						X	X	X	X	X	X		X	X	X	X	X	X		X	X
X	X	X	X		X	X	X	X		X	X	X	X	X	X						X	X	X	X		X	X
X	X	X	X		X	X	X	X		X	X	X	X	X	X											X	X
X	X	X	X		X	X	X	X						X	X						X	X	X	X		X	X
X	X					X	X	X		X	X	X		X	X	X	X		X	X	X	X	X	X		X	X
X	X		X	X		X	X	X		X	X	X		X	X	X	X		X	X	X	X	X	X		X	X
X	X		X	X		X	X																			X	X
X	X		X	X	X	X	X	X	X	X	X	X	X	X	X	X	X		X	X	X	X		X	X	X	X
X	X							X	X													X		X	X	X	X
X	X		X	X				X	X		X	X		X	X	X	X		X	X	X	X		X	X	X	X
X	X		X	X				X	X		X	X		X	X	X	X		X	X						X	X
X	X		X	X							X		E		X	X	X									X	X
X	X	X	X	X	X	X	X	X	X	X	X				X	X	X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
""".strip()

masmorra3_str = """
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
X	X	X																							X	X	X
X	X	X		X	X	X	X	X	X	X	X	X	X	X		X	X	X	X	X	X	X	X		X	X	X
X	X	X		X	X	X	X	X	X	X	X	X	X	X		X	X	X	X	X	X	X	X		X	X	X
X	X	X		X	X				X				X				X				X	X	X		X	X	X
X	X	X		X	X								X				X				X	X	X		X	X	X
X	X	X		X	X				X				X				X				X	X	X		X	X	X
X	X	X		X	X	X	X	X	X	X		X	X	X		X	X	X		X	X	X	X		X	X	X
X	X	X		X	X				X	X		X	X	X		X	X	X		X			X		X	X	X
X	X	X																					X		X	X	X
X	X	X		X	X				X	X		X	X	X	X	X	X	X		X			X		X	X	X
X	X	X		X	X	X		X	X	X		X	X	X	X	X	X	X		X	X	X	X		X	X	X
X	X	X		X	X				X				X				X				X	X	X		X	X	X
X	X	X		X	X				X								X				X	X	X		X	X	X
X	X	X		X	X				X				X				X				X	X	X		X	X	X
X	X	X		X	X	X		X	X	X	X	X	X	X		X	X	X	X	X	X	X	X		X	X	X
X	X	X		X	X				X	X	X	X						X	X				X		X	X	X
X	X	X		X	X				X	X	X	X			P			X	X				X		X	X	X
X	X	X		X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X		X	X		X	X	X
X	X	X																							X	X	X
X	X	X	X	X	X		X	X	X	X	X	X	X		X	X	X	X	X	X		X	X	X	X	X	X
X	X	X	X	X	X		X	X	X	X	X	X	X		X	X	X	X	X	X		X	X	X	X	X	X
X	X	X	X						X	X	X						X	X						X	X	X	X
X	X	X	X						X	X	X			E			X	X						X	X	X	X
X	X	X	X						X	X	X						X	X						X	X	X	X
X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X	X
"""

masmorra1 = mapa_para_matriz(masmorra1_str)
masmorra2 = mapa_para_matriz(masmorra2_str)
masmorra3 = mapa_para_matriz(masmorra3_str)