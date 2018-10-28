# -*- coding: utf-8 -*-

countries={
    'mexico':122,
    'colombia':49,
    'argentina': 43,
    'chile':18,
    'peru':31
    }


while True:
    country= str(input('Escribe el nombre del páis: ')).lower()
    try:
        print('La población de {} es: {} millones'.format(country,countries[country]))
    except KeyError:
        print('No tengo el dato del pais {}'.format(country))
