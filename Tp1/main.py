def comparar_datos(intervalos, transacciones):
    intervalos_ord = sorted(intervalos, key=lambda x: (x[0]-x[1], x[0]))
    coincidencias = []

    for i in range(len(transacciones)):
        t_i,e_i = intervalos_ord[0][0], intervalos_ord[0][1]
        s_i = transacciones[i]
        menor_distancia = s_i - (t_i - e_i)
        j = 1
        while j < len(intervalos_ord) and s_i - (intervalos_ord[j][0] - intervalos_ord[j][1]) >= 0:
            d = s_i - (intervalos_ord[j][0] - intervalos_ord[j][1])
            if d < menor_distancia:
                menor_distancia = d
                t_i,e_i = intervalos_ord[j][0], intervalos_ord[j][1]
            j += 1
        

        if s_i < (t_i-e_i) or s_i > (t_i+e_i):
            return False, []
        
        coincidencias.append((s_i, t_i, e_i))
        intervalos_ord.remove((t_i,e_i))
    
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