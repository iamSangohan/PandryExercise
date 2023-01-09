import random
import time
import threading

INTERVALMAX = 10 # temps maximum entre l'arrivée de deux clients en secondes
DUREETRAITEMENTMAX = 5 # durée maximum de traitement d'un client en secondes

nombre_clients = 0 # nombre de clients en attente

def arrivee_client():
    global nombre_clients
    global interval
    interval = random.randint(0, INTERVALMAX)
    time.sleep(interval) # attendre l'intervalle de temps en secondes
    nombre_clients += 1 # incrémenter le nombre de clients
    print(f"Nouveau client arrivé. Nombre de clients en attente : {nombre_clients}")

def traitement_client():
    global nombre_clients
    global duree
    # ne pas traiter de client s'il n'y en a pas en attente
    if nombre_clients == 0:
        return
    duree = random.randint(0, DUREETRAITEMENTMAX)
    time.sleep(duree) # attendre la durée de traitement en secondes
    nombre_clients -= 1 # décrémenter le nombre de clients
    print(f"Client traité. Nombre de clients en attente : {nombre_clients}")

def simuler():
    compteur_clients = 0 # compteur du nombre de clients traités
    temps_total = 0 # temps total passé dans la simulation en secondes
    duree = 0

    while True:
        # créer un thread pour simuler l'arrivée d'un client
        thread_arrivee = threading.Thread(target=arrivee_client)
        thread_arrivee.start()

        # simuler le traitement d'un client dans le thread principal
        traitement_client()

        compteur_clients += 1
        temps_total += interval + duree

simuler()
