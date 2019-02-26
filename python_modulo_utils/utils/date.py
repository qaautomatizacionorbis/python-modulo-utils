import pytz
from datetime import datetime

def getDate(region='America/Lima'):
    """RETORNA LA FECHA SEGUN LA REGION ENVIADA [for tz in pytz.all_timezones:print(tz)],CASO CONTRARIO RETORNA NONE"""
    fecha = None
    try:
        tz = pytz.timezone(region)
        fecha = datetime.now(tz)
    except:
        print("OCURRIO UN ERROR INESPERADO , VERIFICAR QUE SE TENGA INSTALADO LA LIBRERIA: 'pytz' ")
    return fecha

def getDateString(region='America/Lima'):
    """RETORNA LA FECHA EN FORMATO DIA-MES-ANO HORA:MINUTO:SEGUNDO SEGUN LA REGION ENVIADA [for tz in pytz.all_timezones:print(tz)] , CASO CONTRARIO RETORNA NONE"""    
    fecha = None
    try:
        tz = pytz.timezone(region)
        fecha = datetime.now(tz)
    except:
        print("OCURRIO UN ERROR INESPERADO , VERIFICAR QUE SE TENGA INSTALADO LA LIBRERIA: 'pytz' ")
    return fecha.strftime("%d-%m-%Y %H:%M:%S")