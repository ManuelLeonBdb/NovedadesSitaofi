import pandas as pd


def main():
    # Ruta al archivo CSV
    ruta_csv = 'Novedades segmentación 31072024.csv'

    # Cargar el archivo CSV en un DataFrame
    data = pd.read_csv(ruta_csv, dtype=str)

    # Mostrar las primeras filas del DataFrame
    print(data.head())
    TABCNJ4(data)    
    TABNAL4(data)    
    TABOFI4(data)
    TABLOFI4(data)
    LCNOFI20(data)    
    LMEZON20(data)
    LCECIU20(data)
    LRANAL20(data)
    IMCIU020(data)


def LCNOFI20(data):
    print("Creando LCNOFI20.TXT....")
    # Leer el archivo de texto
    lineas = leer_txt("LCNOFI20.TXT")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[1:5]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                newparm = newparm + \
                          linea[0:14] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(27) + \
                          linea[41:77] + \
                          resultado['COD REGION COMERCIAL'].iloc[0].ljust(2) + \
                          resultado['COD ZONA COMERCIAL'].iloc[0][1:3].ljust(2) + \
                          linea[81:]
    else:
        print("No se pudo leer el archivo LCNOFI20.TXT")
    with open("newparms/LCNOFI20.TXT", 'w') as archivo:
        archivo.write(newparm)

def LMEZON20(data):
    print("Creando LMEZON20.TXT....")
    # Leer el archivo de texto
    lineas = leer_txt("LMEZON20.TXT")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[5:9]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                newparm = newparm + \
                          resultado['COD REGION COMERCIAL'].iloc[0].ljust(2) + \
                          resultado['COD ZONA COMERCIAL'].iloc[0].ljust(3) + \
                          linea[5:9] + \
                          resultado['NOMBRE REGION COMERCIAL'].iloc[0].ljust(20) + \
                          resultado['NOMBRE ZONA COMERCIAL'].iloc[0].ljust(20) + \
                          linea[49:]
    else:
        print("No se pudo leer el archivo LMEZON20.TXT")
    with open("newparms/LMEZON20.TXT", 'w') as archivo:
        archivo.write(newparm)        

def LCECIU20(data):
    print("Creando LCECIU20.TXT....")
    # Leer el archivo de texto
    lineas = leer_txt("LCECIU20.TXT")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[0:4]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                newparm = newparm + \
                          linea[0:4] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(20) + \
                          linea[24:] 
    else:
        print("No se pudo leer el archivo LCECIU20.TXT")
    with open("newparms/LCECIU20.TXT", 'w') as archivo:
        archivo.write(newparm)     

def LRANAL20(data):
    print("Creando LRANAL20.TXT....")
    # Leer el archivo de texto
    lineas = leer_txt("LRANAL20.TXT")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[1:5]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                newparm = newparm + \
                          linea[0:15] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(27) + \
                          linea[42:] 
    else:
        print("No se pudo leer el archivo LRANAL20.TXT")
    with open("newparms/LRANAL20.TXT", 'w') as archivo:
        archivo.write(newparm)     

def IMCIU020(data):
    print("Creando IMCIU020.TXT....")
    # Leer el archivo de texto
    lineas = leer_txt("IMCIU020.TXT")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[0:4]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                newparm = newparm + \
                          linea[0:4] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(37) + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(20) + \
                          linea[61:] 
    else:
        print("No se pudo leer el archivo IMCIU020.TXT")
    with open("newparms/IMCIU020.TXT", 'w') as archivo:
        archivo.write(newparm)    

def TABNAL4(data):
    print("Creando TABNAL4.SEC....")
    # Leer el archivo de texto
    lineas = leer_txt("TABNAL4.SEC")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[1:5]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                newparm = newparm + \
                          linea[0:15] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(27) + \
                          linea[42:78] + \
                          resultado['COD REGION COMERCIAL'].iloc[0].ljust(2) + \
                          resultado['COD ZONA COMERCIAL'].iloc[0][1:3].ljust(2) + \
                          linea[82:]
    else:
        print("No se pudo leer el archivo TABNAL4.SEC")
    with open("newparms/TABNAL4.SEC", 'w') as archivo:
        archivo.write(newparm)

def TABOFI4(data):
    print("Creando TABOFI4.SEC....")
    # Leer el archivo de texto
    lineas = leer_txt("TABOFI4.SEC")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[1:5]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                newparm = newparm + \
                          linea[0:15] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(27) + \
                          linea[42:78] + \
                          resultado['COD REGION COMERCIAL'].iloc[0].ljust(2) + \
                          resultado['COD ZONA COMERCIAL'].iloc[0][1:3].ljust(2) + \
                          linea[82:]
    else:
        print("No se pudo leer el archivo TABOFI4.SEC")
    with open("newparms/TABOFI4.SEC", 'w') as archivo:
        archivo.write(newparm)

def TABLOFI4(data):
    print("Creando TABLOFI4.SEC....")
    # Leer el archivo de texto
    lineas = leer_txt("TABLOFI4.SEC")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[1:5]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                newparm = newparm + \
                          linea[0:15] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(27) + \
                          linea[42:78] + \
                          resultado['COD REGION COMERCIAL'].iloc[0].ljust(2) + \
                          resultado['COD ZONA COMERCIAL'].iloc[0][1:3].ljust(2) + \
                          linea[82:]
    else:
        print("No se pudo leer el archivo TABLOFI4.SEC")
    with open("newparms/TABLOFI4.SEC", 'w') as archivo:
        archivo.write(newparm)

def TABCNJ4(data):
    print("Creando TABCNJ4.SEC....")
    # Leer el archivo de texto
    lineas = leer_txt("TABCNJ4.SEC")
    newparm = ''
    # Verificar si el archivo de texto se leyó correctamente
    if lineas is not None:
        for linea in lineas:
            colname = "COD OFICINA"
            query_str = f"`{colname}` == '{linea[1:5]}'"
            resultado = data.query(query_str)            
            if resultado.empty:
                newparm = newparm + linea
            else:
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                newparm = newparm + \
                          linea[0:15] + \
                          resultado['NOMBRE OFICINA'].iloc[0].ljust(27) + \
                          linea[42:]
    else:
        print("No se pudo leer el archivo TABCNJ4.SEC")
    with open("newparms/TABCNJ4.SEC", 'w') as archivo:
        archivo.write(newparm)



def leer_txt(ruta_txt):
    """Lee un archivo de texto y devuelve su contenido como una lista de líneas."""
    try:
        #with open(ruta_txt, 'r', encoding='utf-8') as file:
        with open(ruta_txt, 'r') as file:
            lineas = file.readlines()
        return lineas
    except FileNotFoundError:
        print(f"El archivo en la ruta {ruta_txt} no fue encontrado.")
        return None
    
if __name__ == "__main__":
    main()    