def calc(crist):
    return (55 - (55 * (10 * crist) / 100))

crist = int(input('Ingresar cantidad de cristales: '))

print(f'La potencia final con la pérdida calculada es {calc(crist)}')