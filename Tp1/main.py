def contar_apariciones(intervalos):
    intervalos_todos = {}
    for j in range(len(intervalos)):
        t_i, e_i = intervalos[j][0], intervalos[j][1]
        if (t_i,e_i) not in intervalos_todos:
            intervalos_todos[(t_i,e_i)] = 0
        intervalos_todos[(t_i,e_i)] += 1
    return intervalos_todos


def comparar_datos(intervalos, transacciones):
    coincidencias = []
    intervalos_todos = contar_apariciones(intervalos)

    for i in range(len(transacciones)):
        s_i = transacciones[i]
        intervalo_i = ()
        min_fin = float('inf')

        for j in range(len(intervalos)):
            t_i, e_i = intervalos[j][0], intervalos[j][1]
            if intervalos_todos[((t_i,e_i))] <= 0:
                continue
            if (t_i-e_i) <= s_i <= (t_i+e_i) and (t_i + e_i) < min_fin:
                min_fin = t_i + e_i
                intervalo_i = (t_i, e_i)

        if not intervalo_i:
            return False, []
        
        intervalos_todos[intervalo_i] -= 1
        coincidencias.append((s_i, intervalo_i[0], intervalo_i[1]))
    
    return True, coincidencias


def main():
    n = int(input())
    intervalos = []
    transacciones = []

    for _ in range(n):
        linea = input()
        linea = linea.strip().split(",")
        t_i, e_i = int(linea[0]), int(linea[1])
        intervalos.append((t_i, e_i))
    
    for _ in range(n):
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