# Lastats
Frontend znajduje się pod: 
https://bartoszbugla.github.io/lastats


## Frontend
**Spis Treści**

- [Przygotowanie](#przygotowanie)
- [Instalacja projektu](#instalacja-projektu)
- [Serwer lokalny](#serwer-lokalny)
- [Budowa projektu](#budowa-projektu)
- [Produkcyjny podgląd](#produkcyjny-podgląd)
- [Stos Technologiczny](#stos-technologiczny)
- [Struktura projektu ](#struktura-projektu)
- [Zmienne środowiskowe](#zmienne-środowiskowe)



### Przygotowanie

Do poprawnego włączenia projektu niezbędne jest zainstalowanie Node na urządzeniu - [Node](https://nodejs.org/en)

### Instalacja projektu

```bash
git clone https://github.com/BartoszBugla/lastats.git

cd lastats/frontend

npm install
```

### Serwer lokalny 

```bash
npm run dev
```

Nastęonie wejdź http://localhost:8080 w przeglądarce.

### Budowa projektu:

```bash
npm run build
```

### Produkcyjny podgląd:

```bash
npm run preview
```

### Stos Technologiczny

> Wersje znajdują się w `package.json`
- **Typescript** 
- **Tanstack Query** - pobieranie danych
- **Svelte** - glówny framework - https://svelte.dev/
- **SvelteKit** - meta framework, serwer - https://kit.svelte.dev/
- **Tailwind css** - stylowanie -  https://tailwindcss.com/
- **Daisy ui** - gotowe style nakładka na tailwind css - https://daisyui.com/
- **Zod** - walidacja danych 


### Struktura projektu 

Kod źrodłowy znajduje 

- `/static` - Miejsce, w którym znajdują się wszystkie pliki statyczne projektu
- `/lib` - W tym folderze znajdują się wszystkie funkcje pomocnicze, komponenty oraz konfiguracja
- `/routes` - kazda podstrona w 



