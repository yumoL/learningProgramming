<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/tietokantakaavio.png">

- Käyttäjä(User) käyttää sovellusta, jokaisella käyttäjällä on oma uniikki käyttäjätunnus(name), salasana(pwd) ja rekisteröinnin aika(addtime)

- Artikkelilla(Art) on otsikko(title),sisältö(text), lukijien ja komenttien määrä sekä lisäämisaika(addtime). Yksi artikkeli kuuluu vain yheen kategoriaan(Tag), toisaalta yhdellä kategorialla voi olla useampaa artikkelia. 

- Käyttäjä kirjoittaa kommentteja(Comment) artikkeleista. Komentilla on sisältö(content) ja muokkaamisaika(addtime). Yksi käyttäjä voi kirjoittaa useita kommentteja useammasta artikkelista, yhdellä kommentilla on vain yksi kirjoittaja.

- Käyttäjä voi tykätä artikkeleita(Artcol). Artikkeiden tykkäämisellä on tykkäyksen lisäämisaika. Yksi käyttäjä voi tykätä useampaa artikkelia ja yhdellä artikkelilla voi olla useampaa tykkääjää. 

- Sovelluksella on ylläpitäjä(Admin), ylläpitäjällä voi olla monta päiväkirjaa toiminnoistaan, mutta yksi päiväkirja liittyy vain yhteen ylläpitäjään. Ylläpitäjä voi olla super(is_super=1) tai tavallinen. Vaan super-ylläpitäjällä on oikeus aiheen lisäämiseen, muokkaamiseen ja poistamiseen, sekä kommentin ja käyttäjän poistamiseen.

## CREATE TABLE-lauseet

### Tag
CREATE TABLE tag (
id INTEGER NOT NULL, 
name VARCHAR(100), 
addtime DATETIME NOT NULL, 
PRIMARY KEY (id), 
UNIQUE (name)
);

### Art
CREATE TABLE art(
id INTEGER NOT NULL,
title varchar (255),
text TEXT,
readnum BIGINT,
commentnum BIGINT,
tag_id INTEGER NOT NULL,
addtime DATETIME NOT NULL,
PRIMARY KEY(id),
UNIQUE(title),
FOREIGN KEY(tag_id) REFERENCES tag (id)
);

### Oplog
CREATE TABLE oplog (
id INTEGER NOT NULL, 
admin_id INTEGER, 
reason VARCHAR(600), 
addtime DATETIME NOT NULL, 
PRIMARY KEY (id), 
FOREIGN KEY(admin_id) REFERENCES admin (id)
);

### Account
CREATE TABLE account(
id INTEGER NOT NULL,
name varchar(100),
pwd varchar(100),
addtime DATETIME NOT NULL,
PRIMARY KEY(id),
UNIQUE(name));

### Comment
CREATE TABLE comment (
id INTEGER NOT NULL, 
content TEXT, 
addtime DATETIME NOT NULL,
art_id INTEGER,
user_id INTEGER,
PRIMARY KEY(id),
FOREIGN KEY(art_id)REFERENCES art(id),
FOREIGN KEY(user_id) REFERENCES account(id));

### Admin
CREATE TABLE admin (
id INTEGER NOT NULL, 
name VARCHAR(100), 
pwd VARCHAR(100),
is_super Integer,
primary key(id));

## Artcol
CREATE TABLE artcol(
id integer not null,
art_id integer,
user_id integer,
addtime datetime,
primary key(id),
foreign key(art_id)references art(id),
foreign key(user_id)references account(id));

## Tietokannan normaalisointi
### Ensimmäinen normaaimuoto
Kaikki tietokantataulut ovat ensimmäisessä normaalimuodossa:
- Sarakkeen arvot eivät saa sisältää listoja.
- Taulun sarakkeet eivät muodosta toistuvia ryhmiä.
- Sarakkeen arvot ovat saman tyyppisiä.
- Jokaisen sarakkeen nimi on tietokantataulussa uniikki.
- Sarakkeiden järjestys ei vaikuttaa tietokantataulun toimintaan.
- Tietokantataulussa ei ole kahta täsmälleen samanlaista riviä.
- Rivien järjestys ei vaikuttaa tietokantataulun toimintaan.

### Toinen normaalimuoto
Kaikki tietokantaulut ovat toisessa normaalimuodossa:
- Taulut ovat ensimmäisessä normaalimuodossa ja niillä on yhden sarakkeen avulla määritelty pääavain(id), joten ne ovat automaattisesti toisessa normaalimuodossa. 

### Kolmas normaalimuoto
- Tietokantataulut Tag, Art, Account,Admin eivät ole kolmanessa normaalimuodossa:
Taulussa Tag on funktionaalinen riippuvuus addtime->name,eli aiheen lisäämisaika voidaan päätellä sen nimen perusteella,      samalla kaikki sarakkeet ovat selvitettävissä taulun pääavaimen(id) kautta, joten taulusta löytyy myös transitiivinen riippuvuus. Samalla muista tauluista löytyy sarakeita, jotka ovat transiivisesti riippuvaisia pääavimesta. 

### Perustelu normaalisoinnin puutteille
- Tag:
Aiheen nimen pitää olla uniikki. Ei ole järkevää, että kaksi artikkelia kuuluu erilaisiin kategorioihin, mutta silti samasta aiheesta. 
- Art:
Artikkelin otsikon pitää olla uniikki. Lukijan etusivussa näytetään vain artikkeleiden otsikot, jos eri artikelilla on sama otsikko, lukijalla ei voi päätellä otsikon perusteella kumpaa artikkelia hän haluaa lukea. 
- Account:
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/k%C3%A4ytt%C3%A4j%C3%A4/comment.png">
Käyttäjän nimen pitää olla uniikki. Kommenttilistassa näytetään kommentoijan nimi ja kommentin sisältö, jos eri käyttäjällä on sama nimi, muut eivät voi päätellä, kuka oli kirjoittanut jonkin kommentin. 
- Admin: 
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/admin/oplogList.png">
Samasta syystä ylläpitäjän nimen pitää olla uniikka, muuten muut ylläpitäjät eiväi voi päätellä, kuka oli tehnyt jonkin toimenpiteen.



