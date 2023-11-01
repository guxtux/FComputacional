def trapecio_recursiva(f, a, b, Ianterior, k):
    if k == 1: Inueva = (f(a) + f(b)) * (b - a)/2.0
    else:
        n = 2**(k - 2) # Numero de puntos nuevo
        h = (b - a)/n # Espaciamiento de los puntos nuevos
        x = a + h/2.0 # Coord. del primer punto
        sum = 0.0
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        Inueva = (Ianterior + h*sum)/2.0
    return Inueva

def romberg(f, a, b, tol=1.0e-6):
    
    def richardson(r, k):
        for j in range(k-1, 0, -1):
            const = 4.0**(k - j)
            r[j] = (const*r[j+1] - r[j])/(const - 1.0)
        return r

    r = np.zeros(21)
    r[1] = trapecio_recursiva(f, a, b, 0.0, 1)
    r_anterior = r[1]
    for k in range(2, 21):
        r[k] = trapecio_recursiva(f, a, b, r[k-1], k)
        r = richardson(r, k)
        if abs(r[1] - r_anterior) < tol*max(abs(r[1]),1.0):
            return r[1], 2**(k-1)
        r_anterior = r[1]
    print('La integracion de Romberg no converge')
