import sqlite3

        
class todo:
    def __init__(self,db_file = 'todo.db'):
        self.db_file= db_file
        
    def ajout(self,tache):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                         CREATE TABLE IF NOT EXISTS tache( id_tache INTEGER PRIMARY KEY AUTOINCREMENT, tache TEXT)
                         ''')
            cursor.execute('INSERT INTO tache(tache) VALUES(?)', (tache,))
            conn.commit()
            
        print('La tâche a été ajoutée avec syccès !')
        
    def suppr(self,num):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tache WHERE id_tache = ? ',(num,))
            conn.commit()
            
        print(f'la tâche numero {num} a été supprimé !')
        
    def liste(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                         CREATE TABLE IF NOT EXISTS tache( id_tache INTEGER PRIMARY KEY AUTOINCREMENT, tache TEXT)
                         ''')
            cursor.execute('SELECT * FROM tache')
            resultats = cursor.fetchall()
        
        for resultat in resultats:
            print(f'{resultat[0]}- {resultat[1]}')
            
            
            
def main():
    tache = todo()
    while True:
        choix = input('''
                      
    Veuillez tapez le numero de l'action que vous voulez efectuer:
    1-Lister les tâches
    2-Ajouter une tâche
    3-Supprimer une tâche
    4-Quitter l'application 
    \n''')
        match choix:
            case '1':
                tache.liste()
            case '2':
                tac = input('''
    Veuillez entrer la tâche que vous voulez ajouter
    >''')
                tache.ajout(tac)
            case '3':
                num = int(input('''
    Veuillez entrer le numero de la tâche que vous voulez supprimer
    >'''))
                tache.suppr(num)
            case '4':
                print('Au revoir :) ')
                exit()
                
            case _:
                print('Veuillez entrer une option valide')
                

main()