<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/tietokantakaavio.png">

- Käyttäjä(User) käyttää sovellusta, jokaisella käyttäjällä on oma uniikki käyttäjätunnus(name), salasana(pwd) ja rekisteröinnin aika(addtime)

- Artikkelilla(Art) on otsikko(title),sisältö(text), lukejien ja komenttien määrä sekä lisäämisaika(addtime). Yksi elokuva kuuluu vain yheen kategoriaan(Tag), toisaalta yhdellä kategorialla voi olla useampaa artikkelia. 

- Käyttäjä kirjoittaa kometteja(Comment) artikkeleista. Komentilla on sisältö(content) ja muokkaamisaika(addtime). Yksi käyttäjä voi kirjoittaa useita komentteja useammasta artikkelista, yhdellä komentilla on vain yksi kirjoittaja.

- Käyttäjä voi tykätä artikkeleita(Artcol). Artikkeiden tykkäämisellä on tykkäyksen lisäämisaika. Yksi käyttäjä voi tykätä useampaa artikkelia ja yhdellä artikkelilla voi olla useampaa tykkääjää. 

- Sovelluksella on ylläpitäjä(Admin), ylläpitäjällä voi olla monta päiväkirjaa toiminnoistaan, mutta yksi päiväkirja liittyy vain yhteen ylläpitäjään. 

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
