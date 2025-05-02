import paho.mqtt.client as mqtt
import time

def ex1():
    print("------ Exercice 1 ------")
    print("Se connecter sur le port 22 du serveur : ssh ap4dbx13@10.34.164.21 -p 22")
    print("Ouverture de deux terminaux, un pour mosquitto_pub et un pour mosquitto_sub")
    print("Dans le terminal sub : mosquitto_sub -h 127.0.0.1 -t /UserXX/HW")
    print("Dans le terminal sub : mosquitto_pub -h 127.0.0.1 -t /UserXX/HW -m 'Hello world'")
    print("Reception du message.")
    print("Voir screenshot TP2-ex1.png dans le dossier screenshots.")
    
def ex2a():
    print("------ Exercice 2a ------")
    print("Aller sur le serveur Raspbian et lancer l'exercice, il se lancera dans tous les cas")
    def on_publish(client, userdata, mid):
        print("message published")
        client.disconnect()
    client = mqtt.Client()
    client.on_publish = on_publish
    client.connect("127.0.0.1", 1883)  # Le broker est local sur le Raspberry
    client.loop_start()
    client.publish("/UserXX/HW", "Hello world", qos=2)
    client.loop_stop()
    
def ex2b():
    print("------ Exercice 2b ------")
    print("Aller sur le serveur Raspbian et lancer l'exercice, il se lancera dans tous les cas")
    def on_subscribe(client, userdata, mes):
        msg=mes.payload.decode("utf-8")
        print("Received ", msg, " on topic ", mes.topic)
        client.loop_stop()
        client.disconnect()
    client = mqtt.Client()
    client.on_message = on_subscribe
    client.connect("127.0.0.1", 1883)
    client.subscribe("#", 2)
    client.loop_forever()

def ex3_debian():
    def on_publish(client, userdata, mid):
        print("Message publié !")

    client = mqtt.Client()
    client.on_publish = on_publish

    client.connect("mosquitto.junia.com", 1883)
    client.loop_start()
    client.publish("/UserXX/HW", "Hello world", qos=1)
    client.loop_stop()

def ex3_raspbian():
    def on_message(client, userdata, message):
        print("Message reçu :", message.payload.decode())

    client = mqtt.Client()
    client.on_message = on_message

    client.connect("mosquitto.junia.com", 1883)
    client.subscribe("/UserXX/HW", qos=1)
    client.loop_forever()
    
def ex4_debian():
    client = mqtt.Client()
    client.connect("mosquitto.junia.com", 1883)
    client.loop_start()

    # Envoi de trois températures
    client.publish("/Junia/UserXX/temp_piece", 23.5)
    time.sleep(1)
    client.publish("/Junia/UserXX/temp_chauff", 26.0)
    time.sleep(1)
    client.publish("/Junia/UserXX/temp_ext", 27.0)
    time.sleep(1)

    client.loop_stop()
    client.disconnect()

def ex4_raspbian():
    temp_piece = None
    temp_chauff = None
    temp_ext = None

    def on_message(client, userdata, message):
        global temp_piece, temp_chauff, temp_ext
        topic = message.topic
        value = float(message.payload.decode())
        
        if topic.endswith("temp_piece"):
            temp_piece = value
        elif topic.endswith("temp_chauff"):
            temp_chauff = value
        elif topic.endswith("temp_ext"):
            temp_ext = value

        # Dès qu’on a les trois températures, on prend des décisions
        if all(t is not None for t in [temp_piece, temp_chauff, temp_ext]):
            print(f"Températures reçues : pièce={temp_piece}, chauffage={temp_chauff}, ext={temp_ext}")

            # Réinitialiser pour attendre le prochain cycle
            piece = temp_piece
            chauff = temp_chauff
            ext = temp_ext
            temp_piece = temp_chauff = temp_ext = None

            if chauff > 25:
                client.publish("/Junia/UserXX/comm_chauff", "off")
                print("→ Chauffage coupé")

            if ext > piece:
                client.publish("/Junia/UserXX/act_fen", "open")
                print("→ Fenêtre ouverte")

    client = mqtt.Client()
    client.on_message = on_message

    client.connect("mosquitto.junia.com", 1883)
    client.subscribe("/Junia/UserXX/temp_piece")
    client.subscribe("/Junia/UserXX/temp_chauff")
    client.subscribe("/Junia/UserXX/temp_ext")

    print("En attente de messages...")
    client.loop_forever()
