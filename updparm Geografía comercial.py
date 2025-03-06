import pandas as pd


def main():
    # Ruta al archivo CSV
    ruta_csv = 'Archivo Manuel Host y Red.csv'

    # Cargar el archivo CSV en un DataFrame
    data = pd.read_csv(ruta_csv, dtype=str)

    # Mostrar las primeras filas del DataFrame
    print(data.head())
    TABCNJ4(data)     
    TABLOFI4(data)    
    TABOFI4(data)        
    TABNAL4(data)      
    IMCIU020(data)      
    LCECIU20(data)        
    LRANAL20(data)        
    LMEZON20(data)    
    LCNOFI20(data)  
  
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
                newparm = newparm + \
                          linea[0:15] 
                if resultado['NUEVO NOMBRE OFICINA'].iloc[0] != "No Aplica":
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:27].ljust(27)
                else:    
                    newparm = newparm + \
                            linea[15:42]                                                                                
                newparm = newparm + \
                          linea[42:] 
    else:
        print("No se pudo leer el archivo TABCNJ4.SEC")
    with open("newparms/TABCNJ4.SEC", 'w') as archivo:
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
                newparm = newparm + \
                          linea[0:78]
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                if pd.isna(resultado['NUEVO COD REGION COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[78:80]                      
                else:
                     newparm = newparm + \
                              resultado['NUEVO COD REGION COMERCIAL'].iloc[0].ljust(2) 
                if pd.isna(resultado['NUEVO COD ZONA COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[80:82]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO COD ZONA COMERCIAL'].iloc[0][1:3]
                newparm = newparm + \
                          linea[82:]   
    else:
        print("No se pudo leer el archivo TABLOFI4.SEC")
    with open("newparms/TABLOFI4.SEC", 'w') as archivo:
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
                newparm = newparm + \
                          linea[0:78]
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                if pd.isna(resultado['NUEVO COD REGION COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[78:80]                      
                else:
                     newparm = newparm + \
                              resultado['NUEVO COD REGION COMERCIAL'].iloc[0].ljust(2) 
                if pd.isna(resultado['NUEVO COD ZONA COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[80:82]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO COD ZONA COMERCIAL'].iloc[0][1:3]
                newparm = newparm + \
                          linea[82:]      
    else:
        print("No se pudo leer el archivo TABOFI4.SEC")
    with open("newparms/TABOFI4.SEC", 'w') as archivo:
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
                newparm = newparm + \
                          linea[0:78]
                #aqui esta con 'COD ZONA COMERCIAL' de 2 pos y no de 3!!!              
                if pd.isna(resultado['NUEVO COD REGION COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[78:80]                      
                else:
                     newparm = newparm + \
                              resultado['NUEVO COD REGION COMERCIAL'].iloc[0].ljust(2) 
                if pd.isna(resultado['NUEVO COD ZONA COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[80:82]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO COD ZONA COMERCIAL'].iloc[0][1:3]
                newparm = newparm + \
                          linea[82:]                      
    else:
        print("No se pudo leer el archivo TABNAL4.SEC")
    with open("newparms/TABNAL4.SEC", 'w') as archivo:
        archivo.write(newparm)

def IMCIU020(data):
    print("Creando IMCIU020....")
    # Leer el archivo de texto
    lineas = leer_txt("IMCIU020")
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
                          linea[0:4] 
                if resultado['NUEVO NOMBRE OFICINA'].iloc[0] != "No Aplica":
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:37].ljust(37) + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:20].ljust(20)                    
                else:    
                    newparm = newparm + \
                            linea[4:41] + \
                            linea[41:61]                                                                                
                newparm = newparm + \
                          linea[61:] 
    else:
        print("No se pudo leer el archivo IMCIU020")
    with open("newparms/IMCIU020", 'w') as archivo:
        archivo.write(newparm) 

def LCECIU20(data):
    print("Creando LCECIU20....")
    # Leer el archivo de texto
    lineas = leer_txt("LCECIU20")
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
                          linea[0:4] 
                if resultado['NUEVO NOMBRE OFICINA'].iloc[0] != "No Aplica":
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:20].ljust(20)                                               
                else:
                    newparm = newparm + \
                              linea[4:24]                      
                newparm = newparm + \
                          linea[24:]                    
    else:
        print("No se pudo leer el archivo LCECIU20")
    with open("newparms/LCECIU20", 'w') as archivo:
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
                          linea[0:15]
                if resultado['NUEVO NOMBRE OFICINA'].iloc[0] != "No Aplica":
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:27].ljust(27)                                               
                else:
                    newparm = newparm + \
                              linea[15:42]                      
                newparm = newparm + \
                          linea[42:]    
    else:
        print("No se pudo leer el archivo LRANAL20")
    with open("newparms/LRANAL20", 'w') as archivo:
        archivo.write(newparm)      
def LMEZON20(data):
    print("Creando LMEZON20....")
    # Leer el archivo de texto
    lineas = leer_txt("LMEZON20")
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
                if pd.isna(resultado['NUEVO COD REGION COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[0:2]                      
                else:
                     newparm = newparm + \
                              resultado['NUEVO COD REGION COMERCIAL'].iloc[0].ljust(2) 
                if pd.isna(resultado['NUEVO COD ZONA COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[2:5]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO COD ZONA COMERCIAL'].iloc[0][0:3]
                newparm = newparm + \
                          linea[5:9]                      
                if pd.isna(resultado['NUEVO NOMBRE REGION COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[9:29]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE REGION COMERCIAL'].iloc[0][0:20].ljust(20) 
                if pd.isna(resultado['NUEVO NOMBRE ZONA COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[29:49]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE ZONA COMERCIAL'].iloc[0][0:20].ljust(20)                     
                if resultado['NUEVO NOMBRE OFICINA'].iloc[0] != "No Aplica":
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:20].ljust(20)                                               
                else:
                    newparm = newparm + \
                              linea[49:69]                      
                newparm = newparm + \
                          linea[69:]                     

    else:
        print("No se pudo leer el archivo LMEZON20")
    with open("newparms/LMEZON20", 'w') as archivo:
        archivo.write(newparm)        

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
                newparm = newparm + \
                          linea[0:14] 
                if resultado['NUEVO NOMBRE OFICINA'].iloc[0] != "No Aplica":
                    newparm = newparm + \
                              resultado['NUEVO NOMBRE OFICINA'].iloc[0][0:27].ljust(27) + \
                              linea[41:77] 
                else:
                    newparm = newparm + \
                              linea[14:77] 
                if pd.isna(resultado['NUEVO COD REGION COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[77:79]                      
                else:
                     newparm = newparm + \
                              resultado['NUEVO COD REGION COMERCIAL'].iloc[0].ljust(2) 
                if pd.isna(resultado['NUEVO COD ZONA COMERCIAL'].iloc[0]):    
                    newparm = newparm + \
                              linea[79:81]                      
                else:
                    newparm = newparm + \
                              resultado['NUEVO COD ZONA COMERCIAL'].iloc[0][1:3]
                newparm = newparm + \
                          linea[81:]                          
    else:
        print("No se pudo leer el archivo LCNOFI20")
    with open("newparms/LCNOFI20", 'w') as archivo:
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