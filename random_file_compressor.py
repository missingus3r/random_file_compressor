import os

# Leer el archivo y convertir su contenido en una lista de enteros
with open('original_file.bin', 'rb') as file: #sharnd_challenge
    data = file.read()
    
data_as_ints = list(data)

# Calcular el tamaño total del array data_as_ints
tamanio_total = len(data_as_ints)

# Inicializar z y n
z = 0
n = 0

# Calcular z a partir de los n primeros bytes, de tal manera que z sea menor que tamanio_total
for byte in data_as_ints:
    z = (z << 8) | byte
    n += 1
    if z >= tamanio_total or n == len(data_as_ints):
        # Si z es mayor o igual que tamanio_total o no hay más bytes, retroceder un paso
        z >>= 8
        n -= 1
        break

# Quitar los n primeros bytes
data_as_ints = data_as_ints[n:]

# Separar el array en la posición z
parte1 = data_as_ints[:z]
parte2 = data_as_ints[z:]

# Guardar los bytes finales en un nuevo archivo
with open('original_file.bin.1', 'wb') as file:
    file.write(bytearray(parte1))
    
    # Guardar los bytes finales en un nuevo archivo
with open('original_file.bin.2', 'wb') as file:
    file.write(bytearray(parte2))
    

# DECOMP

# Leer el tamaño del primer archivo y calcular los bytes iniciales
tamanio_parte1 = os.path.getsize('original_file.bin.1')
bytes_iniciales = tamanio_parte1.to_bytes((tamanio_parte1.bit_length() + 7) // 8, 'big')

# Leer los archivos separados
with open('original_file.bin.1', 'rb') as file:
    parte1 = file.read()

with open('original_file.bin.2', 'rb') as file:
    parte2 = file.read()

# Combinar los contenidos
contenido_original = bytes_iniciales + parte1 + parte2

# Escribir el archivo original
with open('original_file_decomp.bin', 'wb') as file:
    file.write(contenido_original)