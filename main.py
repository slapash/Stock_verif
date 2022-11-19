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
        book_list = []
        f = request.files['file']
        liste_isbn = fr(f) #gets isbn list
        book_list = demande(liste_isbn)
        def last(n):
            return n[-1] 
  
        def sort(tuples):
            return sorted(tuples, key=last)
        book_list = sort(book_list)
        """"
        for i in range(len(liste_isbn)):
            book_list.append(demande(liste_isbn[i]))#list in list inner list --> [isbn, title 1, title 2, stock]
        """  
        """
        en_stock = []
        for i in range(len(liste_isbn)):
            if demande(liste_isbn[i]) == 1:
                en_stock.append(liste_isbn[i])
        non_en_stock = [x for x in liste_isbn if x not in en_stock ]
        """
        #return render_template('resultat.html', out_stock = non_en_stock)  
        
        return render_template('resultat.html', liste = book_list)



if __name__ == '__main__':
    app.run(debug=True)