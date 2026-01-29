# 📚 PyLibrary - Personal Function Archive

Un tool Python progettato per automatizzare l'estrazione e l'archiviazione di funzioni da progetti locali, creando una libreria personale consultabile e documentata.

## 🚀 Obiettivo
Il progetto nasce dall'esigenza di non "reinventare la ruota". **PyLibrary** scansiona le cartelle dei tuoi progetti, estrae il codice delle funzioni e le relative docstring, creando un indice per riutilizzarle velocemente in nuovi script.

## 📖 Logica di Funzionamento
Il sistema utilizza un approccio a tre stadi:
1. **Crawler**: Esplora ricorsivamente le directory ignorando cartelle di sistema (es. `__pycache__`, `.venv`).
2. **Parser**: Analizza il codice riga per riga identificando i blocchi `def`, estraendo il nome, la docstring (standard PEP 257) e l'intero corpo del codice.
3. **Exporter**: Organizza i dati in un archivio strutturato per una consultazione rapida.

## 🛠️ Roadmap del Progetto
- [x] **Fase 1: Scansione** - Navigazione nelle cartelle e identificazione file `.py`.
- [x] **Fase 2: Parsing** - Estrazione logica di nomi, docstring, corpo delle funzioni e mappatura dei percorsi file.
- [x] **Fase 3: Storage (JSON)** - Esportazione dell'intero archivio in formato JSON per portabilità e ricerca testuale.
- [ ] **Fase 4: Storage (Database)** - Implementazione SQLite per gestire grandi moli di dati (Oltre 10k file).
- [ ] **Fase 5: Interfaccia** - Strumento di ricerca e consultazione da riga di comando o GUI.

## 📊 Stato Attuale
L'ultimo test ha prodotto un database di circa **37.5 MB**, contenente le funzioni estratte da oltre 13.000 file sorgente.

## 📈 Versionamento
Questo progetto segue la filosofia del **Semantic Versioning**.
Per i dettagli sulle singole modifiche, consulta il [CHANGELOG.md](CHANGELOG.md).