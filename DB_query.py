
import pyodbc


#à changer pour la librairie:
#SERVER_NAME 
#DATABASE_NAME
#en passant par MSSQL sur l'ordi du fond
DRIVER_NAME = "SQL SERVER"
SERVER_NAME = "MOSQSDESKTOP\CDL_API_EXP"
DATABASE_NAME = "CARREFOURDULIVRE"

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection = yes;
"""

def demande(demande):
    cnxn = pyodbc.connect(connection_string)
    
    cursor = cnxn.cursor()

    cursor.execute(f"SELECT COUNT(*) from v_ART_EnStock WHERE ARTCB = '{demande}'")

   
    for row in cursor:
         liste_en_stock = [elem for elem in row]

    cursor.close()
    cnxn.close()
    return liste_en_stock[0]
    

