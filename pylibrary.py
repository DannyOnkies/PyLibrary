#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
==========================================================
 Nome File : pylibrary.py
 Autore    : Daniele
 Data      : 12/01/2026
 Scopo     : Crea una libreria di funzioni
 Note      : Riutilizza le funzioni scritte nei progetti
==========================================================
"""

# ==============================
#  SEZIONE IMPORT
# ==============================
import os
import json

# import sys
# import math


# ==============================
#  SEZIONE COSTANTI & VARIABILI
# ==============================
VERSIONE = "0.4"
dir_progetti_python = r'C:\Users\danie\Desktop\PythonCode'


# ==============================
#  SEZIONE FUNZIONI
# ==============================

def trova_progetti(path):
    """
    La funzione elenca tutte le cartelle contenute nella cartella dei progetti

    Il presupposto è che si abbia una cartella principale dentro cui vi
    siano le cartelle dei progetti. Le cartelle il cui nome inizi con un punto ('.'),
    oppure con 2 underscore ('__') vengono ignorate. Inoltre se nella cartella principale
    sono presenti file di qualsiasi tipo, anche di python, non vengono aggiunti alla lista

    Args: 'path' è il percorso della cartella principale

    Returns: 'lista_cartelle' è una lista che contiene i nomi di tutte le cartelle
    """
    lista_cartelle = []
    for dirpath, dirnames, filenames in os.walk(path):
        # Rimuovi in-place le directory che iniziano con '.' o contengono '__'
        # qui sotto anche la versione LIST COMPREHENSION della procedura
        # dirnames[:] = [d for d in dirnames if not d.startswith('.') and '__' not in d]
        nuova_dirnames = []
        for d in dirnames:
            if not d.startswith('.') and '__' not in d:
                nuova_dirnames.append(d)
        dirnames[:] = nuova_dirnames

        nomedir = os.path.basename(dirpath)
        if not nomedir.startswith('.') and '__' not in nomedir:
            lista_cartelle.append(dirpath)
    return lista_cartelle


def elenca_file_python(nome_cartella):
    """
    La funzione elenca tutti i file python contenuti nella cartella passata come argomento

    Il percorso passato alla funzione deve essere completo

    Args: 'nome_cartella' è il percorso assoluto della cartella da controllare

    Returns: 'lista_file' è una lista che contiene i nomi completi di path dei file python trovati
    """
    lista_file = []
    elenco_file = os.listdir(nome_cartella)
    for i in elenco_file:
        path_completo_file = os.path.join(nome_cartella, i)
        if os.path.isfile(path_completo_file):
            nome, ext = os.path.splitext(path_completo_file)
            if ext == '.py':
                lista_file.append(path_completo_file)
    return lista_file


def leggi_codice_file(file_py):
    """
    Legge il file *.py e lo trasforma in una lista

    Apre il file in modalità lettura e restituisce
    una lista dove ogni elemento è una riga del file.
    Serve a estrai_funzioni

    Args: file_py - una stringa col percorso del file *.py

    Returns: contenuto - lista di righe
    """
    with open(file_py,'r',encoding='utf-8') as f:
        lista_file_py = f.readlines()
    # ListComprehension: elimina le righe vuote
    new_lista_file_py = [riga for riga in lista_file_py if riga != '\n']
    return new_lista_file_py


def estrai_funzioni(file_py_lista, path_originale):
    """
    Estrae le funzioni dal file di codice python

    Il file convertito in lista  da leggi_codice_file viene
    analizzato con un parser a 2 cicli while, che mediante
    filtratura estrae le righe comprese tra il
    def nomefunzione(attr) e l'ultima riga della funzione.

    Args: file_py_lista - è il file python convertito in lista

    Returns: lista di dizionari con una struttura di questo tipo
    [
        {'nome': 'mia_funz', 'codice': '...', 'docstring': '...'},
        {...}
    ]
    """
    # questa lista conterrà i dizionari
    lista_finale = []
    # stringa globale conterrà il codice della funzione
    #stringa_codice = ''
    i = -1
    while i < len(file_py_lista)-1:
        i += 1
        #if 'def ' in file_py_lista[i] and file_py_lista[i][0] == 'd':
        if file_py_lista[i].startswith('def '):
            # stringa globale conterrà il codice della funzione
            stringa_codice = ""
            #aggiungo subito il nome della funzione alla stringa
            stringa_codice += file_py_lista[i]
            # creo un dizionario che conterrà i dati della funzione
            info_funzione = {}
            # estrae dalla riga con il tag "def" solo il nome della funzione
            nome_funzione_pulito = file_py_lista[i].split('(')[0].split()[1]
            # aggiungo il nome della funzione al dizionario
            info_funzione['nome'] = nome_funzione_pulito
            # aggiungo il path del file che contiene la funzione al dizionario
            info_funzione['path_file'] = path_originale
            # condizioni affinchè il ciclo interno prosegua:
            # 1 - l'incremento di linea deve essere minore del numero di righe totale
            # 2 - l'inizio della riga deve essere uno spazio perche significa che siamo dentro a una funzione
            # 3 - può essere presente una linea vuota
            while (i + 1 < len(file_py_lista)) and (file_py_lista[i+1].startswith(' ') or file_py_lista[i+1].strip() == ''):
                i += 1
                # leggo una riga e l'aggiungo alla stringa globale del codice
                stringa_codice += file_py_lista[i]

            # il secondo while ha terminato il suo ciclo
            # aggiungo la documentazione al dizionario
            info_funzione['docstring'] = estrai_docstring(stringa_codice)
            # aggiungo il codice al dizionario
            info_funzione['codice'] = estrai_codice(stringa_codice)
            # il dizionario è completo e lo aggiungo alla lista
            lista_finale.append(info_funzione)
    return lista_finale

def estrai_docstring(stringa_unica):
    """
    La funzione estrae il testo compreso tra i triplici doppi apici

    find restituisce la posizione della prima istanza
    rfind la posizione della seconda istanza

    Args: la stringa da controllare

    Returns: la parte compresa tra i doppi apici
    """
    if stringa_unica.find('"""') != -1:
        step1 = stringa_unica.find('"""') + 3
        step2 = stringa_unica.rfind('"""')
        return stringa_unica[step1:step2]
    else:
        return 'Nessuna documentazione presente'

def estrai_codice(stringa_unica):
    """
    La funzione estrae il codice python

    Il codice si trova al termine della docstring

    Args: la stringa da controllare

    Returns: la parte successiva a i doppi apici
    """
    if stringa_unica.find('"""') != -1:
        step = stringa_unica.rfind('"""') + 3
        return stringa_unica[step:]
    else:
        return stringa_unica



def salva_dati_json(lista_dati, nome_file="archivio_pylibrary.json"):
    """
    Salva la lista di dizionari in un file formato JSON

    Integrato controllo per evitare problmi con caratteri
    speciali come le lettere accentate o i backslash dei
    percorsi Windows

    Args: intera lista di dizionari delle funzioni estratte

    Returns: non restituisce nulla
    """
    try:
        with open(nome_file, 'w', encoding='utf-8') as f:
            # ensure_ascii=False serve per leggere bene i path Windows e le accentate
            json.dump(lista_dati, f, indent=4, ensure_ascii=False)
        print(f"\n✅ Archivio salvato con successo in: {nome_file}")
    except Exception as e:
        print(f"\n❌ Errore durante il salvataggio: {e}")


# ==============================
#  SEZIONE MAIN
# ==============================
def main():
    lista_cartelle = trova_progetti(dir_progetti_python)

    # creo un unica lista con tutti i file .python
    lista_file_pyton = []
    for cartella in lista_cartelle:
        lista_file_pyton = lista_file_pyton + elenca_file_python(cartella)

    print(f'Nella cartella {dir_progetti_python} ci sono {len(lista_cartelle)} cartelle')
    print(f'Ho trovato {len(lista_file_pyton)} file con estensione *.py')

    archivio_totale = []
    for file_py in lista_file_pyton:
        righe = leggi_codice_file(file_py)
        funzioni_py = estrai_funzioni(righe, file_py)
        archivio_totale.extend(funzioni_py)

    # salvo tutte le funzioni in un archivio globale
    salva_dati_json(archivio_totale)


    num_stampa_func = 10
    print('\n=====================================================================')
    print(f' Stampo i dati delle prime {num_stampa_func} funzioni con documentazione presente')
    print('======================================================================')
    counter=0
    for funzione in archivio_totale:
        if funzione['docstring'] != "Nessuna documentazione presente":
            print('\n=================================================')
            print('Path file *.py: ',funzione['path_file'])
            print('Nome funzione: ',funzione['nome'])
            print('💼 Documentazione:')
            print(funzione['docstring'].strip())
            print('💾 Codice:')
            print(funzione['codice'].strip())
            counter+=1
        if counter >= num_stampa_func:
            break
# ==============================
#  PUNTO DI INGRESSO
# ==============================
if __name__ == "__main__":
    main()
