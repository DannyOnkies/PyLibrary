# 📚 PyLibrary - Personal Function Archive

Un tool Python progettato per automatizzare l'estrazione e l'archiviazione di funzioni da progetti locali, creando una libreria personale consultabile e documentata.

## 🚀 Obiettivo
Il progetto nasce dall'esigenza di non "reinventare la ruota". **PyLibrary** scansiona le cartelle dei tuoi progetti, estrae il codice delle funzioni e le relative docstring, creando un indice per riutilizzarle velocemente in nuovi script.

## 📖 Logica di Funzionamento
Il sistema utilizza un approccio a due stadi:
1. **Crawler**: Esplora ricorsivamente le directory ignorando cartelle di sistema (es. `__pycache__`, `.venv`).
2. **Parser**: Analizza il codice riga per riga identificando i blocchi `def` e l'indentazione associata.

## 🛠️ Roadmap del Progetto
- [x] **Fase 1: Scansione** - Navigazione nelle cartelle e identificazione file `.py`.
- [ ] **Fase 2: Parsing** - Estrazione logica di nomi, docstring e corpo delle funzioni (**In corso**).
- [ ] **Fase 3: Storage** - Salvataggio in database SQLite o JSON.
- [ ] **Fase 4: Interfaccia** - Strumento di ricerca e consultazione.

## 📈 Versionamento
Questo progetto segue la filosofia del **Semantic Versioning** (Major.Minor.Patch).
Per i dettagli sulle singole modifiche, consulta il [CHANGELOG.md](CHANGELOG.md).