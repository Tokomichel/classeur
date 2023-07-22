import os
import os.path as path


dossier_parent = 'C:/Users/hp/Downloads'

dossiers = os.listdir(dossier_parent)
# [print(item) for item in dossiers if item[(len(item ) - 3):] == 'mp4']
# os.rename(f'{dossier_parent}/eru.jpg', f'{dossier_parent}/zoko/eru.jpg')



for item in dossiers:
    if path.isfile(f'{dossier_parent}/{item}'): # On verifie que c'est un fichier
        
        avi = item[(len(item ) - 3):] == 'avi'
        mp4 = item[(len(item ) - 3):] == 'mp4'
        if mp4 or avi: # on verifie que c'est une video
            # on cree le dossier videos s'il nexiste pas
            if path.exists(f'{dossier_parent}/videos'):
                # Alors on ne le cree plus et on passe aux deplacements
                os.rename(f'{dossier_parent}/{item}', f'{dossier_parent}/videos/{item}')
            else:
                # dans le cas contraire on le cree avant de passer aux deplacements
                os.mkdir(f'{dossier_parent}/videos')
                os.rename(f'{dossier_parent}/{item}', f'{dossier_parent}/videos/{item}')
        else:
            print(f'{item}  n\'est pas une video')
            continue
    else:
        print(f'{item} est un dossier')
        continue
