# Struktura projekta

Ovaj dokument opisuje inicijalnu strukturu projekta. Ostala dokumentacija može se pronaći u direktoriju `docs/`.

```bash
.
├── backend
│   ├── src
│   │   ├── __init__.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── docs
│   ├── DEV_START.md
│   └── STRUKTURA_PROJEKTA.md
├── dokploy
│   ├── compose.yaml
│   └── .env.template
├── frontend
│   ├── public
│   │   └── vite.svg
│   ├── src
│   │   ├── assets
│   │   │   └── vue.svg
│   │   ├── components
│   │   │   └── HelloWorld.vue
│   │   ├── App.vue
│   │   ├── main.ts
│   │   └── style.css
│   ├── Dockerfile
│   ├── .gitignore
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── scripts
│   ├── install.sh
│   └── setup.sh
├── .github
│   ├── workflows
│   │   └── placeholder.yml
│   └── CODEOWNERS
├── .vscode
│   └── extensions.json
├── .gitignore
├── makefile
└── README.md
```

## Glavne komponente

Aplikacija se sastoji od backenda (`backend/`) pisanog u Pythonu ([3.13](https://www.python.org/downloads/release/python-3130/)) i frontenda (`frontend/`) pisanog u [TypeScriptu](https://www.typescriptlang.org/) koristeći [Vue.js](https://vuejs.org/).

U direktoriju svake od tih komponenti nalazi se direktorij `src/` namijenjen datotekama izvornog koda. Pored tog direktorija nalaze se potrebni konfiguracijski dokumenti te `Dockerfile`, budući da se aplikacija pušta u pogon koristeći [Docker Compose](https://docs.docker.com/compose/).

### `backend/`

```bash
backend/
├── Dockerfile
├── requirements.txt
└── src
    ├── __init__.py
    └── main.py
```

Backend je [FastAPI](https://fastapi.tiangolo.com/) aplikacija koja koristi port `8123`. `main.py` je minimalna implementacija FastAPI aplikacije.

```py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}
```

Dostupan je jedan API endpoint (`/`) koji vraća JSON `{'message': 'Hello World'}`. Pokreće se naredbom `make backend` (ili zajedno s frontendom koristeći `make dev`).

`requirements.txt` je popis vanskih Python modula potrebnih za funkcioniranje backenda (zasad `uvicorn` i `fastapi`). Moduli se instaliraju naredbom:

```bash
pip install -r backend/requirements.txt
```

Dostupan je `Dockerfile` koji opisuje build containera koji koristi python:3.13-alpine base image, instalira potrebne module koristeći naredbu iznad te pokreće aplikaciju naredbom

```bash
python -m uvicorn src.main:app --host 0.0.0.0 --port 8123
```

### `frontend/`

Frontend koristi framework [Vue.js](https://vuejs.org/) s podrškom za [TypeScript](https://www.typescriptlang.org/). Trenutni sadržaj direktorija je nepromijenjeni predložak Vue projekta stvoren naredbom

```bash
npm create vite@latest my-app -- --template vue-ts
```

`Dockerfile` koristi standardni [multi-stage build](https://docs.docker.com/build/building/multi-stage/) i `npm serve`.

## Pomoćni direktoriji i konfiguracije

Uz direktorije glavnih komponenti, `backend/` i `frontend/`.

### `.github/`

Svrha ovog direktorija su workflows za [GitHub Actions](https://github.com/features/actions) za automatsko puštanje u pogon i testiranje. To će omogućiti blokiranje neispravnog koda na produkcijskoj `main` grani nakon `git push origin main` ili pull requesta koji bi napravio sličnu stvar.

Trenutno je dostupan jedan workflow u `.github/workflows/placeholder.yml` - predložak koji ne radi ništa korisno i završava bez greške.

### `.vscode/`

Direktorij sadrži dijeljene konfiguracije razvojnog orkuženja VSCode specifične za ovaj projekt.

**`.vscode/extensions.json`:**

Datoteka sadrži popis preporučenih VSCode proširenja za razvoj korištenih tehnologija.

### `dokploy/`

Budući da se u produkciji aplikacija pušta u pogon koristeći [Dokploy](https://dokploy.com/), u direktoriju `dokploy/` nalazi se sve što je potrebno da bi se aplikacija pustila u pogon:

**`dokploy/compose.yaml`:**

Ova datoteka opisuje sve usluge potrebne za ispravan rad aplikacijskog poslužitelja.

Trenutno se u `compose.yaml` nalazi predložak koji ne radi ništa korisno i završava bez greške.

**`dokploy/.env.template`:**

U ovoj se datoteci nalaze sve tajne varijable koje koristi `compose.yaml`, tj. koje su potrebne za ispravan rad aplikacije.

Datoteka je trenutno potpuno prazna.

### `.gitignore`

Ovo je popis datoteka i direktorija koji se koriste za lokalni razvoj, ali nije potrebno ili poželjno slati ih na remote (GitHub). To mogu biti tajne datoteke (npr. `.env` datoteke sa stvarnim privatnim informacijama), cachevi (npr. `__pycache__/` koji se stvori kad se lokalno pokrene Python program), direktoriji s vanjskim ili uvezenim (importanim) modulima (npr. `.venv/`, `frontend/node_modules/`) ili rezultati build koraka (npr. `frontend/dist/`).

U projektu se nalaze dvije `.gitignore` datoteke:

**`.gitignore`:**

Ova datoteka se odnosi na cijeli projekt. Postavljena je tako da ignorira sve `.env` datoteke ili `.env` datoteke s nastavkom (npr. `.env.dev`), osim `.env.template` i `.env.example` u kojima se nikad ne bi trebale nalaziti tajne informacije (nego služe kao predložak koji programeri mogu dijeliti i sami upisivati tajne vrijednosti).

Također ignorira direktorij Pythonovog virtualnog orkuženja (`.venv/`) te cache koji se stvara lokalnim pokretanjem Python modula (`__pycache__/`).

**`frontend/.gitignore`:**

Datoteku stvara automatski inicijalizacijski postupak Vue.js projekta te nije mijenjana.

### `makefile`

[Make](https://en.wikipedia.org/wiki/Make_(software)) se koristi za olakšavanje pokretanja naredbi - u ovom slučaju za istovremeno pokretanje frontenda i backenda tijekom lokalnog razvoja (izvan Dockera).

Dostupne `make` naredbe:

- **`make setup`** - Osigurava da je sve potrebno instalirano, provjerava verzije i postavlja Python virtualno okruženje.
- **`make install`** - Postavlja Python virtualno okruženje, instalira Python i Node dependencies
- **`make backend`** - Pokreće backend FastAPI aplikaciju (koristeći Uvicorn server i objekt `app` iz modula `src.main`) na portu `8123`
- **`make frontend`** - Pokreće Vite server frontenda na portu `5173`
- **`make dev`** - Pokreće backend i frontend istovremeno
- **`make test`** - Pokreće testove (trenutno ispisuje tekst u konzolu)
