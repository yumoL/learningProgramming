# User story

## Käyttäjä
### Käyttäjä voi kirjautua sisään sovellukseen
- Käyttäjä, jolla on käyttäjätunnus, voi kirjautua sisään syöttämällä syöttökentillä oman käyttäjätunnuksen ja salasanan.
- Käyttäjä, jolla ei vielä ole käyttäjätunnusta, voi saada oman käyttäjätunnuksen rekisteröimisen jälkeen.

Tavoite: Käyttäjä pääsee sovellukseen.
```
SELECT*FROM account WHERE name="syöttöentälle annettu nimi" ja pwd="syöttökentälle annettu salasana";
```

### Käyttäjä voi rekisteröidä
- Käyttäjä, jolla ei vielä ole käyttäjätunnusta, voi mennä rekisteröinnille.

Tavoite: Käyttäjä saada oman käyttäjätunnuksen kirjautuakseen sisään sovellukseen.
```
INSERT INTO account(name,pwd,addtime) VALUES("nimi","salasana","CURRENT_TIMESTAMP);
```

### Käyttäjä voi kommentoida artikkeleita
- Käyttäjä, jolla on käyttäjätunnus, voi kirjauduttuaan kommentoida artikkeleita
```
INSERT INTO comment(content,addtime,art_id,user_id) values("kommenttikentälle syötetty sisältö", CURRENT_TIMESTAMP,artikkelin id,sisään kirjautuneen käyttäjän id)
```

### Käyttäjä voi hakea artikkeleita
- Käyttäjä voi hakea artikkelia otsikon perusteella. Lisäksi käyttäjä voi järjestellä artikkeleita lukijien ja kommenttien määrän perusteella.
- Artikkelin hakeminen otsikon perusteella:
```
SELECT*FROM art WHERE title LIKE "%avainsana";
```
- Artikkelin järjestäminen lukijien määrän perusteella:
```
SELECT*FROM art ORDER BY readnum desc;
```
-Artikkeli järjestäminen kommenttin määrän perusteella:
```
SELECT*FROM art ORDER BY commentnum desc;
```

### Käyttäjä voi tykätä artikkeleita
- Käyttäjä voi tykätä artikkeleita ja pääsee kirjauduttuaan lukemaan tykättyjä artikkeleita.
```
INSERT INTO artcol(art_id,user_id,addtime) VALUES(sisään kirjautuneen käyttäjän id,tykätyn artikkelin id,CURRENT_TIMESTAMP
```

### Käyttäjä voi halutessaan vaihtaa käyttäjätunnuksensa ja salasanansa.
- Käyttäjäntunnuksen vaihtamaminen
``` 
UPDATE account SET name="uusi nimi" WHERE id=sisäänkirjautuneen käyttäjän id;
```
-Salasanan vaihtaminen
``` 
UPDATE account SET name="uusi salasana" WHERE id=sisäänkirjautuneen käyttäjän id;
```
### Käyttäjä näkee omat kommentit ja tykätyt artikkelit
- Kommentin listaaminen
```
SELECT account.name,comment.content,art.title FROM account,comment,art WHERE account.id=sisään kirjautuneen käyttäjän id AND art.id=comment.art_id;
```
-Tykätyn artikkelin listaaminen
```
SELECT art.title FROM account,art,artcol WHERE account.id=sisään kirjautuneen käyttäjän id AND art.id=artcol.art_id;
```

## Ylläpitäjä
### Ylläpitäjä voi kirjautua sisään ylläpitokentälle.
- Ylläpitäjällä on oma käyttäjätunnus ja salasana päästäkeen ylläpitokentälle. Ylläpitäjä voi olla joko super-ylläpitäjä tai tavallinen ylläpitäjä.

Tavoite: Ylläpitäjä pääsee ylläpitämään sovellusta.
```
SELECT*FROM admin WHERE name="syöttöentälle annettu nimi" ja pwd="syöttökentälle annettu salasana";
```

### Ylläpitäjä voi lisätä, muokata ja poistaa artikkeleita
- Ylläpitäjä voi lisätä uusia artikkeleita ja poistaa vanhoja artikkeleita.
- Artikkelin lisääminen
```
INSERT INTO art(title,text,readnum,commentnum,tag_id,addtime) VALUES("otsikko","sisältö",0,0,valitun aiheen id,CURRENT_TIMESTAMP);
```
- Artikkelin muokkaaminen
```
UPDATE art SET title="uusi otsikko",text="uusi sisältö",tag_id=uuden auheen aihe WHERE id=muokattavan artikkelin id;
```
- Artikkelin listaaminen
```
SELECT*FORM art;
```
- Artikkelin poistaminen:
```
DELETE FROM art WHERE id=poistavan artikkelin id
```
### Ylläpitäjä voi määritellä aiheita
-  Vain super-ylläpitäjä voi lisätä, muokata ja poistaa aiheita,joiden perusteella artikkeleita luokitellaan.
- Aiheen lisääminen
```
INSERT INTO tag(name,addtime) VALUES ("aiheen nimi",CURRENT_TIMESTAMP);
```
- Aiheen muokkaaminen
```
UPDATE tag SET name="uusi nimi" WHERE id=muokattavan aiheen id;
```
- Aiheen listaaminen
```
SELECT*FORM tag;
```
- Aiheen poistaminen:
```
DELETE FROM tag WHERE id=poistavan aiheen id;
```

### Ylläpitäjä voi poistaa kommentteja ja käyttäjiä

- Super-ylläpitäjä voi poistaa komentteja, jotka rikkovat lakia tai ovat henkilökohtaisia hyökkäyksiä toisia käyttäjiä kohtaan.
- Super-ylläpitäjä voi myös poistaa käyttäjiä, jotka julkaistaa edellä mainittuja komentteja.
- Kommentin poistaminen
```
DELETE FROM comment where id=poistavan kommentin id;
```
- Käyttäjän poistaminen:
```
DELETE FRMO account WHERE id=postavan käyttäjän id;
```
Käyttäjän poistamiseen yhteydessä myös hänen kommentit postetetaan
```
DELETE FROM comment where user_id=poistavan käyttäjän id;
```
### Ylläpitäjä näkee kaikki kommentit
- Kommentin listaaminen
```
SELECT account.name,art.title,comment.content,comment.addtime FROM account,art,comment WHERE comment.user_id=account.id AND comment.art_id=art.id ORDER BY comment.addtime desc;
```
### Jokaisen ylläpitäjän toimienpiteet kirjataan ja ylläpitäjä näkee sekä oman että muiden ylläpitäjien toimenpiteet
- Päiväkirjan lisääminen esim.uuden aiheen lisäämisestä
```
INSETR INTO oplog(admin_id,reason,addtime) VALUES(ylläpitäjän id,"toimenpide",CURRENT_TIMESTAMP);
```
- Toimenpiteen listaaminen
```
SELECT*FROM oplog;
```
