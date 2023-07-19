import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar micrófono y devolver audio como texto
def transformar_audio_en_texto():
    
    # almacenamos recognizer en una variable
    r = sr.Recognizer()
    # configurar micrófono
    with sr.Microphone() as origen:
        # tiempo de espera de micrófono
        r.pause_threshold = 0.8
        print("Ya puedes hablar")
        # guardar audio en variable
        audio = r.listen(origen)
        
        
        try:
            pedido = r.recognize_google(audio, language="es-co")
            print("Usuario: " + pedido)
            return pedido
        except sr.UnknownValueError:
            print("No entendí lo que dijiste")
            return "sigo esperando"
        except sr.RequestError:
            print("No hay servicio")
            return "sigo esperando"
        except:
            print("Error desconocido")

# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    engine = pyttsx3.init()
    engine.say(mensaje)
    engine.runAndWait()
    
    
# informar el dia de la semana

def pedir_dia():
    dia = datetime.date.today()
    dia_semana = dia.weekday()
    
    diccionario_dias = {0: 'Lunes', 
                        1: 'Martes', 
                        2:'Miércoles', 
                        3:'Jueves', 
                        4:'Viernes', 
                        5:'Sábado', 
                        6:'Domingo'}
    
    hablar(f'Hoy es {diccionario_dias[dia_semana]}')
    
    
# informar la hora   
def consultar_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} con {hora.minute}'
    hablar(hora)
    

def saludo_inicial():
    
    hora = datetime.datetime.now()
    
    if hora.hour < 5 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >=6 and hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"
    
    hablar(f"{momento}, soy Cortana, tu asistente personal. ¿En qué te puedo ayudar?")
    
    
    
def pedir_cosas():
    saludo_inicial()
    
    comenzar = True
    
    while comenzar:
        pedido = transformar_audio_en_texto().lower()
        
        if 'abrir youtube' in pedido:
            hablar('Abriendo YouTube')
            webbrowser.open('https://wwww.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Abriendo navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            consultar_hora()
            continue
        elif 'abrir twitter' in pedido:
            hablar('Abriendo Twitter')
            webbrowser.open('https://www.twitter.com')
            continue
        elif 'abrir Linkedin' in pedido:
            hablar('Abriendo Linkedin')
            webbrowser.open('https://www.linkedin.com')
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 2)
            hablar('Según Wikipedia')
            hablar(resultado)
            continue
        elif 'busca en google' in pedido:
            hablar("Buscando en Google")
            pedido = pedido.replace('busca en google','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'chiste' in pedido:
            hablar("¡Claro!")
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            hablar("Buscando en Yahoo Finance")
            accion = pedido.split('de')[-1].strip()
            cartera = {'appple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info('regularMarketPrice')
                hablar(f'El precio de la {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón, pero no la he encontrado.")
                continue
        elif 'reproducir' in pedido:
            hablar("reproduciendo")
            pywhatkit.playonyt(pedido)
            continue   
        elif 'adiós' in pedido:
            hablar("Adiós, me voy a descansar.")
            break
        
        
pedir_cosas()