# User story

## Käyttäjä
### Käyttäjä voi kirjautua sisään sovellukseen
- Käyttäjä, jolla on käyttäjätunnus, voi kirjautua sisään syöttämällä syöttökentillä oman käyttäjätunnuksen ja salasanan.
- Käyttäjä, jolla ei vielä ole käyttäjätunnusta, voi saada oman käyttäjätunnuksen rekisteröimisen jälkeen.

Tavoite: Käyttäjä pääsee sovellukseen.
```
SELECT FROM account WHERE name="syöttöentälle annettu nimi" ja pwd="syöttökentälle annettu salasana";
```

### Käyttäjä voi rekisteröidä
- Käyttäjä, jolla ei vielä ole käyttäjätunnusta, voi mennä rekisteröinnille.

Tavoite: Käyttäjä saada oman käyttäjätunnuksen kirjautuakseen sisään sovellukseen.
```
INSERT INTO account(name,pwd,addtime) VALUES("nimi","salasana","CURRENT_TIMESTAMP);
```

### Käyttäjä voi komentoida artikkeleita
- Käyttäjä, jolla on käyttäjätunnus, voi kirjauduttuaan kommentoida artikeleita

### Käyttäjä voi hakea artikkeleita
- Käyttäjä voi hakea elokuvia nimen perusteella. Lisäksi käyttäjä voi järjestellä artikkeleita lukejien ja komenttien määrän perusteella.

### Käyttäjä voi tykätä artikkeleita
- Käyttäjä voi tykätä artikkeleita ja pääsee kirjauduttuaan lukemaan tykättyjä artikkeleita.

## Ylläpitäjä
### Ylläpitäjä voi kirjautua sisään ylläpitokentälle.
- Ylläpitäjällä on oma käyttäjätunnus ja salasana päästäkeen ylläpitokentälle. Ylläpitäjä voi olla joko super-ylläpitäjä tai tavallinen ylläpitäjä.

Tavoite: Ylläpitäjä pääsee ylläpitämään sovellusta.

### Ylläpitäjä voi lisätä ja poistaa artikkeleita
- Ylläpitäjä voi lisätä uusia artikkeleita ja poistaa vanhoja artikkeleita.

### Ylläpitäjä voi määritellä aiheita
-  Vain super-ylläpitäjä voi määritellä aiheita,joiden perusteella artikkeleita luokitellaan.

### Ylläpitäjä voi poistaa komentteja ja käyttäjiä

- Super-ylläpitäjä voi poistaa komentteja, jotka rikkovat lakia tai ovat henkilökohtaisia hyökkäyksiä toisia käyttäjiä kohtaan.
- Super-ylläpitäjä voi myös poistaa käyttäjiä, jotka julkaistaa edellä mainittuja komentteja.
