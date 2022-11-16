
import pyodbc
from read_excel import isbn_file_read as fr
import pandas as pd


file = r"C:\Users\benai\Desktop\GLOVO.xlsx"

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
liste_en_stock = []
def demande(demande):
    global liste_en_stock
    cnxn = pyodbc.connect(connection_string)
    
    cursor = cnxn.cursor()

    #cursor.execute(f"SELECT COUNT(*) from v_ART_EnStock WHERE ARTCB = '{demande}'")
    cursor.execute(f"""SELECT ARTCB, ARTTIT1, ARTTIT2, STKQTEREEL
                    FROM ART INNER JOIN STK
                    ON(ART.ARTCOD = STK.ARTCOD)
                    WHERE ARTCB IN {demande}
""")
  
    for row in cursor:
        liste_en_stock.append(row)

    cursor.close()
    cnxn.close()
    
    return liste_en_stock
#dev (works  outputs list of tuples)


