def comparar_datos(intervalos, transacciones):
    intervalos_ord = sorted(intervalos, key=lambda x: (x[0]-x[1], x[0]+x[1]))
    coincidencias = []

    for i in range(len(intervalos_ord)):
        t_i,e_i = intervalos_ord[i][0], intervalos_ord[i][1]
        s_i = transacciones[i]

        if s_i < (t_i-e_i) or s_i > (t_i+e_i):
            return False, []
        
        coincidencias.append((s_i, t_i, e_i))
    
    return True, coincidencias


def main():
    n = int(input())
    intervalos = []
    transacciones = []

    for i in range(n):
        linea = input()
        linea = linea.strip().split(",")
        t_i, e_i = int(linea[0]), int(linea[1])
        intervalos.append((t_i, e_i))
    
    for i in range(n):
        linea = input()
        linea = linea.strip()
        s_i = int(linea)
        transacciones.append(s_i)
    
    es_rata, coincidencias = comparar_datos(intervalos, transacciones)

    if es_rata:
        for c in coincidencias:
            print(c[0],"-->",c[1],"±",c[2])
    else:
        print("No es el sospechoso correcto")

main()