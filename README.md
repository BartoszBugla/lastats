# Lastats

Frontend znajduje się pod:   
https://bartoszbugla.github.io/lastats

```bash
git clone https://github.com/BartoszBugla/lastats.git
```

## Frontend

### Spis Treści

- [Przygotowanie](#przygotowanie)
- [Instalacja projektu](#instalacja-projektu)
- [Serwer lokalny](#serwer-lokalny)
- [Budowa projektu](#budowa-projektu)
- [Produkcyjny podgląd](#produkcyjny-podgląd)
- [Stos Technologiczny](#stos-technologiczny)
- [Struktura projektu ](#struktura-projektu)

### Przygotowanie

Do poprawnego włączenia projektu niezbędne jest zainstalowanie Node na urządzeniu - [Node](https://nodejs.org/en)

Do instalacji wszystkich zależności użyj komendy

```bash
npm run install
```

Przed rozpoczęciem nie zbędne jest włączenie backend'u ze względu na generowanie typów bezpośrednio z API, poprzez komendę

```bash
npm run swagger
```

Wykorzystana jest bilbioteka `swagger-typescript-api`

### Serwer lokalny

```bash
npm run dev
```

Następnie wejdź na stronę [http://localhost:8080](http://localhost:8080) w przeglądarce.

### Budowa projektu:

```bash
npm run build
```

### Produkcyjny podgląd:

```bash
npm run preview
```

### Stos Technologiczny

- `Typescript`
- `Tanstack Query` - biblioteka do pobierania danych
- `Svelte` - główny framework używany w projekcie
- `SvelteKit` - metaframework i serwer
- `Tailwiwnd CSS` - narzędzie do stylowania,
- `Daisy Ui` - zestaw gotowych styli dla Tailwind CSS
- `Zod` - biblioteka do walidacji danych

Przydatne linki:

https://kit.svelte.dev/

https://svelte.dev/

https://www.typescriptlang.org/

https://tanstack.com/query/latest/docs/svelte/overview

https://tailwindcss.com/

https://daisyui.com/

https://github.com/colinhacks/zod

### Struktura projektu

Kod źródłowy znajduje się w pliku `frontend/src`

- `/static` - Miejsce, w którym znajdują się wszystkie pliki statyczne projektu
- `/lib` - W tym folderze znajdują się wszystkie funkcje pomocnicze, komponenty oraz konfiguracja
- `/routes` - znajduje się w nim każda podstrona oraz główny (biznesowy) kod aplikacji

## Backend

### Zależności

Plik `requirements.txt` jest plikiem tekstowym, który zawiera listę wszystkich zależności (bibliotek) wymaganych do poprawnego działania aplikacji.

- `flask`: Framework webowy, który pozwala na tworzenie aplikacji internetowych w Pythonie.
- `flask_sqlalchemy`: Rozszerzenie Flaska, które zapewnia integrację z biblioteką SQLAlchemy, umożliwiającą pracę z bazami danych.
- `sqlalchemy`: Biblioteka Pythona służąca do obsługi różnych baz danych.
- `jsonpickle`: Biblioteka do serializacji i deserializacji obiektów Pythona w formacie JSON.
- `Flask-Migrate`: Rozszerzenie Flaska, które ułatwia zarządzanie migracjami baz danych.
- `flask-cors`: Rozszerzenie Flaska, które zapewnia obsługę żądań międzydomenowych (CORS).
- `flask_restx`: Rozszerzenie Flaska, które umożliwia tworzenie interfejsu API REST.
- `black`: Narzędzie do automatycznego formatowania kodu źródłowego w Pythonie.
- `python-dateutil`: Biblioteka do obsługi dat i czasu w Pythonie.

### Uruchomienie projektu

Aby uruchomić ten projekt, wykonaj następujące kroki:

1. Przejdź do katalogu głównego projektu.

```bash
cd backend
```

2. Utwórz i aktywuj wirtualne środowisko Pythona (opcjonalne, ale zalecane).

```bash
source venv/bin/activate
```

3. Zainstaluj wszystkie wymagane zależności.

Upewnij się, że masz zainstalowany menedżer pakietów `pip`, aby móc z powodzeniem zainstalować wymagane biblioteki.

```bash
pip install -r requirements.txt
```

4. Uruchom aplikację.

```bash
flask run -p 8080 --debug
```

6. Aplikacja będzie dostępna pod adresem `http://localhost8080`

@TODO

```console
docker compose up
```
