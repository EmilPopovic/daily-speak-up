# Upute za razvoj

U ovom se dokumentu nalaze upute za postavljanje radnog orkuženja za razvoj projekta. Ove upute su temeljene na Linux operacijskim sustavima [baziranim na debianu](https://distrowatch.com/search.php?basedon=Debian) (npr. [Ubuntu](https://ubuntu.com/)) i razvojnom alatu Visual Studio Code. Korisnici Windows sustava moraju razvijati unutar [WSL](https://learn.microsoft.com/en-us/windows/wsl/about)-a. Pretpostavlja se da korisnici razvojnog okruženja koje nije VSCode (npr. neovim ili Pycharm) mogu snaći u svom alatu.

## Preduvjeti

Prije početka razvoja na projektu, potrebno je ispuniti sljedeće zahtjeve:

1. Instaliran [WSL](https://learn.microsoft.com/en-us/windows/wsl/about) na Windows sustavima (`wsl --install`)
2. Instalirano razvojno okruženje [Visual Studio Code](https://code.visualstudio.com/download) (ili drugo po izboru)
3. Instaliran [Docker Engine](https://docs.docker.com/engine/install/)
4. Instaliran [Python 3.13](https://www.python.org/downloads/release/python-3133/) (naredba `python3 --version` vraća `Python 3.13.x`)
5. Instaliran [Node 22](https://nodejs.org/en/download) (naredba `node --version` vraća `v22.xx.x`)
6. Instaliran [git](https://git-scm.com/downloads)
7. Instaliran [Make]() (`sudo apt-get install build-essential`)

> [!WARNING]
> Ako se za razvoj koristi Windows, Docker Engine, Python 3.13, Node 22 i Make moraju biti instalirani u Linux virtualnom stroju **unutar WSL-a, ne na Windows host stroju**. Preporuča se da git bude instaliran na oba sustava.

## Inicijalizacija lokalnog projekta

### 1. Kloniranje repozitorija

Potrebno je klonirati repozitorij u lokalni direktorij (npr. `~/repos/`). U odabranom direktoriju izvesti naredbu

```bash
git clone git@github.com:EmilPopovic/progi-2025-8.1.git progi
```

Nakon toga se može ući i direktorij i pokrenuti razvojno orkuženje (ili kroz File -> Open Folder... sučelje u VSCode-u)

```bash
cd progi && code .
```


