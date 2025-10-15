# Upute za postavljanje razvojnog okruženja

Ovo je vodič za postavljanje razvojnog okruženja. Ove upute podržavaju **Linux** (Debian distribucije poput Ubuntu) i **Windows** (koristeći WSL).

> [!IMPORTANT]
> **Windows korisnici:** Svi razvojni alati (Docker, Python, Node.js, Make) moraju biti instalirani **unutar WSL-a**, ne na Windowsu. Samo VS Code i Git mogu biti instalirani na Windowsu.

---

## Quickstart

Ako su svi preduvjeti instalirani:

```bash
# Klonirajte repozitorij
git clone git@github.com:progi-2025-g8-1/daily-speak-up.git progi
cd progi

# (u Linux terminalu) Instalirajte dependencies projekta
make install

# Pokrenite razvojnu aplikaciju
make dev
```

---

## Postavljanje od nule

### Korak 1: Specifično za platformu

Odaberite svoj operacijski sustav:

<details>
<summary><b>🪟 Windows korisnici (kliknite za proširenje)</b></summary>

#### 1.1 Instalirajte WSL (Windows Subsystem for Linux)

**Na Windowsu (PowerShell kao Administrator):**

```powershell
# Instalirajte WSL2 s Ubuntuom
wsl --install

# Ponovno pokrenite računalo kada vas sustav upita
```

Nakon restarta, Ubuntu će se pokrenuti automatski. Kreirajte korisničko ime i lozinku kada vas sustav upita.

#### 1.2 Instalirajte Visual Studio Code

**Na Windowsu:**

1. Preuzmite [VS Code](https://code.visualstudio.com/download)
2. Instalirajte sa zadanim postavkama
3. Otvorite VS Code i instalirajte **WSL ekstenziju**:
   - Pritisnite `Ctrl+Shift+X`
   - Potražite "WSL"
   - Instalirajte službenu "WSL" ekstenziju od Microsofta

#### 1.3 Instalirajte Git (opcionalno, ali preporučeno)

**Na Windowsu:**

Preuzmite i instalirajte [Git za Windows](https://git-scm.com/download/win) kako biste koristili Git iz Windows File Explorera.

**Unutar WSL-a:**

Git je obično unaprijed instaliran. Provjerite sa:

```bash
git --version
```

#### 1.4 Konfiguriranje Gita

**Unutar WSL-a:**

```bash
git config --global user.name "Ime Prezime"
git config --global user.email "ime.prezime@fer.unizg.hr"
```

**Sljedeći koraci:** Nastavite od [Koraka 2](#korak-2-kloniranje-repozitorija) **unutar WSL terminala**.

</details>

<details>
<summary><b>🐧 Linux korisnici (kliknite za proširenje)</b></summary>

#### 1.1 Instalirajte Visual Studio Code

**Na Ubuntu/Debian:**

```bash
# Preuzmite i instalirajte VS Code
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg

sudo apt update
sudo apt install code
```

Ili preuzmite `.deb` paket sa [VS Code stranice](https://code.visualstudio.com/download).

#### 1.2 Instalirajte Git

```bash
sudo apt update
sudo apt install git
```

#### 1.3 Konfiguriranje Gita

```bash
git config --global user.name "Ime Prezime"
git config --global user.email "ime.prezime@fer.unizg.hr"
```

**Sljedeći koraci:** Nastavite od [Koraka 2](#korak-2-kloniranje-repozitorija).

</details>

---

### Korak 2: Kloniranje repozitorija

> [!NOTE]
> **Windows korisnici:** Izvršite ovaj korak **unutar WSL-a**. Otvorite WSL upisivanjem `wsl` u PowerShell ili otvorite "Ubuntu" iz Start izbornika.

```bash
# Kreirajte direktorij za repozitorije (ako ne postoji)
mkdir -p ~/repos
cd ~/repos

# Klonirajte repozitorij
git clone git@github.com:progi-2025-g8-1/daily-speak-up.git progi
cd progi
```

**Za Windows korisnike koji koriste VS Code:**

```bash
# Otvorite VS Code u WSL načinu rada iz direktorija projekta
code .
```

Ovo će automatski povezati VS Code (na Windowsu) sa WSL okruženjem.

---

### Korak 3: Automatsko postavljanje

Nudimo automatiziranu skriptu za postavljanje koja će instalirati sve potrebne alate:

- `make`
- Docker Engine
- Python 3.13
- Node.js 22

> [!IMPORTANT]
> **Windows korisnici:** Pokrenite ovo **unutar WSL-a**, ne na Windowsu!

#### 3.1 Pokrenite skriptu za postavljanje

```bash
cd ~/repos/progi

bash scripts/setup.sh
```

Skripta će:

1. Provjeriti koji alati su već instalirani
2. Zatražiti potvrdu prije instalacije bilo čega
3. Instalirati alate koji nedostaju (zahtijeva `sudo` lozinku)
4. Kreirati Python virtualno okruženje
5. Instalirati sve dependencies projekta (Python paketi i npm paketi)

**Ako je Docker instaliran:**

- Možda će biti potrebno odjaviti se i ponovno prijaviti, ili pokrenuti: `newgrp docker`
- Ili jednostavno ponovno pokrenite WSL: `wsl --shutdown` (na Windowsu), zatim ponovo otvorite WSL

---

### Korak 4: Konfiguriranje VS Code (preporučeno)

Kada otvorite projekt u VS Codeu, bit ćete upitani da instalirate preporučene ekstenzije. Kliknite **"Install All"** kako biste dobili:

- Python podršku sa Pylanceom
- Vue.js podršku
- Docker podršku
- Jinja code highlighting
- ESLint, Prettier itd.

---

### Korak 5: Pokretanje aplikacije za razvoj

```bash
make dev
```

Ovo će:

- Pokrenuti FastAPI backend poslužitelj
- Pokrenuti Vue.js frontend razvojni poslužitelj

**Pristup aplikaciji:**

- Frontend: `http://localhost:5173` (ili port prikazan u terminalu)
- Backend API: `http://localhost:8123` (ili port prikazan u terminalu)

---

## Dostupne naredbe

| Naredba | Opis |
|---------|------|
| `make setup` | Instalira sistemske alate (Docker, Python, Node.js, Make) + dependencies projekta |
| `make install` | Instalira/ažurira samo ovisnosti projekta (pip i npm paketi) |
| `make dev` | Pokreće razvojne poslužitelje (backend + frontend) |
| `make backend` | Pokreće samo backend |
| `make frontend` | Pokreće samo frontend |
| `make test` | Pokreće testove |

---

## Ručno postavljanje (alternativa automatskoj skripti)

<details>
<summary><b>Ako preferirate ručno instaliranje alata</b></summary>

### Instalacija Make

```bash
sudo apt update
sudo apt install build-essential
```

### Instalacija Dockera

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Dodajte svog korisnika u docker grupu
sudo usermod -aG docker $USER

# Odjavite se i ponovno prijavite, ili pokrenite:
newgrp docker
```

### Instalacija Python 3.13

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13 python3.13-venv python3.13-dev
```

### Instalacija Node.js 22

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Instalacija ovisnosti projekta

```bash
bash scripts/install.sh
```

</details>
