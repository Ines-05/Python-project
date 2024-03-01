import csv

list_class=[]
matricules=[]


print("-------------------Bienvenue sur notre application de gestion de notes dans une classe ---------------")
nbr_etudiant=int(input("Quel est l'effectif de la classe : "))
nbr_remplir=int(input("Veuillez préciser le nombre d'etudiants à enregistrer : "))
nbr_matiere=int(input("Veuillez indiquez le nombre de matière : "))
def remplir_liste():
    print("**************Remplir la liste de la classe***********")
    for i in range(nbr_remplir):
        name= input("Veuillez entrez le nom et le prenom de l'etudiant : ")
        if name in list_class:
            print("Name already in the list")
        else:
            matricule=int(input("Veuiller entre le matricule de l'etudiant : "))
            if matricule in matricules:
                print("Ce matricule appartient deja à un autre etudiant.")
                matricule=int(input("Veuillez choisir un autre matricule : "))
            else:
                matricules.append(matricule)
                list_class.append(name)  
            
    list_sorted=sorted(list_class)
    return list_sorted,matricules

    
def saisir_note():
    notes_etu=[]
    
    for i in range(nbr_matiere):
        notes=[]
        for j in range(2):
            note=float(input(f"Veuillez entre la note {j+1} de l'etudiant pour la matière {i+1} : "))
            while (note <0 or note >20 ):
                note=float(input("La note entrer n'est pas valide. Veuillez retaper la note : "))
            notes.append(note)
        notes_etu.append(notes)
        print(notes_etu)
        # notes_etu.clear()
    
    return notes_etu

def calcul_mat(notes_etu):#calculer moyenne matiere
    matiere=[]
    for note in notes_etu:
        for i in range(0,len(note),2):
            som=0
            som=note[i]+note[i+1]
            moy_mat=som/2
        matiere.append(moy_mat)
    return matiere

def calculer_moyG(matiere):#calculer moyenne géneral
    s=0
    nbr_note=0
    for n in matiere:
        s+=n
        nbr_note+=1
    moy_G=s/nbr_note
    return moy_G



def mention(moy_g):
    if moy_g > 0 and moy_g < 10:
        return "Mention : Mediocre"
    
    elif (moy_g >=10 and moy_g <12):
        return "Mention : Insuffisant"

    elif (moy_g >=12 and moy_g <14):
        return "Mention : Assez-bien"
    
    elif (moy_g >=14 and moy_g <16):
            return "Mention : Bien"

    elif (moy_g >=16 and moy_g <18):
        return "Mention : Très-bien"
    else :
        return "Mention : Excellente"


def moyenne_classe_minmax(effectif,moyenne):
    Moyenne_min =min(moyenne)
    Moyenne_max=max(moyenne)
    for i in range(effectif):
        somme= sum(moyenne)
        M=somme/effectif
    return M,Moyenne_min ,Moyenne_max

import pandas as pd 
def remplir_information(list_class):
    student_dictionnary=[]
    for etudiant, matricule in zip(list_class[:nbr_remplir],matricules[:nbr_remplir]):
        note_list=saisir_note()
        moy_mat=calcul_mat(note_list)
        print(moy_mat)
        moy_G=calculer_moyG(moy_mat)
        print(moy_G)
        mentions=mention(moy_G)
    #creer un dictionnaire qui prend comme valeur le nom et le prenom de l'etudiant et comme valeur une liste de ces notes par matiere
        student_dictionnary.append({"Nom":etudiant,"Matricule":matricule,"Notes":note_list ,"Moyenne:":moy_G ,"Mention":mentions})
    return pd.DataFrame(student_dictionnary)



list_class , matricules=remplir_liste()

df = remplir_information(list_class)
print(df)

df.to_csv("notes_etudiants.csv",index=False)





# def ajouter_etu():
#     name=input("Entrer le nom et le prenom du nouvel étudiant : ")
#     matricule=input("Veuillez précisez le matricule de l'etudiant : ")
#     if matricule not in matricules:
#         matricules.append(matricule)
#     else:
#         print("Matricule already taken")
#     if name not in list_class:
#         list_class.append(name)
#         list_sorted=sorted(list_class)
#         return list_sorted
#     else:
#         return False

# n=[[12,14,5,8,10,17],[8,14,11,10,13,15],[8,14,17,20,19,19]]

# moy=calcul_mat(n)
# moy_G=calculer_moyG(moy)
#print(moy_G)

# for x in n:
#     moy=0
#     s=0
#     for i in range(0,len(x),2):
#         s= x[i]+x[i+1]
#         #print(s)
#         moy=s/2
#         print(moy)




    