import pandas as pd


def main():
    # Ruta al archivo CSV
    ruta_csv = 'Ajustes plaza canje tp100.csv'

    # Cargar el archivo CSV en un DataFrame
    data = pd.read_csv(ruta_csv, dtype=str)

    # Mostrar las primeras filas del DataFrame
    print(data.head())
    LCNOFI20(data)        
    LIMTCC20(data)    
    LRANAL20(data)    
    TABNAL4(data)    
    TABOFI4(data)    
    TABLOFI4(data)    
    TABCNJ4(data)    







def LCNOFI20(data):
    print("Creando LCNOFI20....")
    # Leer el archivo de texto
    lineas = leer_txt("LCNOFI20")
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
                #print(resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4))
                newparm = newparm + \
                          linea[0:53] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[57:] 
    else:
        print("No se pudo leer el archivo LCNOFI20")
    with open("newparms/LCNOFI20", 'w') as archivo:
        archivo.write(newparm)

def LIMTCC20(data):
    print("Creando LIMTCC20....")
    # Leer el archivo de texto
    lineas = leer_txt("LIMTCC20")
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
                          linea[0:66] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[70:] 
    else:
        print("No se pudo leer el archivo LCNOFI20")
    with open("newparms/LIMTCC20", 'w') as archivo:
        archivo.write(newparm)

def LRANAL20(data):
    print("Creando LRANAL20....")
    # Leer el archivo de texto
    lineas = leer_txt("LRANAL20")
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
                          linea[0:53] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[57:] 
    else:
        print("No se pudo leer el archivo LRANAL20")
    with open("newparms/LRANAL20", 'w') as archivo:
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
                          linea[0:54] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[58:]
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
                          linea[0:54] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[58:]
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
                          linea[0:54] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[58:]
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
                          linea[0:54] + \
                          resultado['NUEVA PLAZA TP CANJE'].iloc[0].ljust(4) + \
                          linea[58:]
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