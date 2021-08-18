horaActual= int(input("Hora de inicio (horas): "))
minutosActuales = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

while horaActual > 23 and minutosActuales > 59:
    horaActual = int(input("Hora de inicio (horas): "))
    minutosActuales = int(input("Minuto de inicio (minutos): "))
    duracion = int(input("Duración del evento (minutos): "))
    

minutosFinales = minutosActuales + duracion
if minutosFinales > 59:
    conteoHoras = minutosFinales // 60
    horaFinal = horaActual + conteoHoras
    minutosFinales = minutosFinales - conteoHoras * 60
    
    
    print(horaFinal,":",minutosFinales)
    
elif minutosFinales < 59 and minutosFinales:
    print(horaActual,":",minutosFinales)


    
    