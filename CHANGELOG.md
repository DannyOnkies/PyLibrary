# Changelog

Tutte le modifiche degne di nota a questo progetto saranno documentate in questo file.

## [1.1.0] - 2026-01-30
### Added
- **Parser Avanzato**: Implementata logica a doppio ciclo `while` per l'estrazione completa delle funzioni.
- **Metadata**: Aggiunta l'estrazione automatica del nome funzione e del percorso del file di origine (`path_file`).
- **Docstring Extraction**: Implementata logica di isolamento per documentazione racchiusa in tripli apici (`"""`).
- **Esportazione JSON**: Aggiunta funzione `salva_dati_json` per la persistenza dei dati su disco con supporto UTF-8.

### Fixed
- Risolto il bug che troncava i primi caratteri (`de`) della riga `def` in assenza di docstring.
- Ottimizzato il buffer di memoria nel Main tramite l'uso di `extend()` invece di `append()` per l'unione dei dizionari.
- Corretto l'incremento dell'indice riga per evitare il salto della prima riga dei file analizzati.

## [1.0.0] - 2026-01-21
### Added
- Inizializzazione del repository Git.
- Implementazione del **Crawler** (Fase 1): navigazione ricorsiva delle cartelle e filtraggio file `.py`.
- Creazione struttura documentale (README e CHANGELOG).