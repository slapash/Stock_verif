from flask import Flask, request, render_template
import os
from DB_query import demande
from read_excel import isbn_file_read as fr


#DOSSIER8UPLOAD à changer pour stocker le fichier excel
#pour le moment ce n'est pas utile mais ça pourrait l'être par la suite 
DOSSIER_UPLOAD = r'C:\Users\benai\Desktop\CDL_API\tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DOSSIER_UPLOAD

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/handler', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        liste_isbn = fr(f)
        en_stock = []
        for i in range(len(liste_isbn)):
            if demande(liste_isbn[i]) == 1:
                en_stock.append(liste_isbn[i])
        non_en_stock = [x for x in liste_isbn if x not in en_stock ]
        return render_template('resultat.html', out_stock = non_en_stock)  
    
    


if __name__ == '__main__':
    app.run(debug=True)