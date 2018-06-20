<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/tietokantakaavio.png">

-Käyttäjä(User) käyttää sovellusta, jokaisella käyttäjällä on oma uniikki käyttäjätunnus(name), salasana(pwd) ja rekisteröinnin aika(addtime)

Artikkelilla(Art) on otsikko(title),sisältö(text), lukejien ja komenttien määrä sekä lisäämisaika(addtime). Yksi elokuva kuuluu vain yheen kategoriaan(Tag), toisaalta yhdellä kategorialla voi olla useampaa artikkelia. 

-Käyttäjä kirjoittaa kometteja(Comment) artikkeleista. Komentilla on sisältö(content) ja muokkaamisaika(addtime). Yksi käyttäjä voi kirjoittaa useita komentteja useammasta artikkelista, yhdellä komentilla on vain yksi kirjoittaja.

-Käyttäjä voi tykätä artikkeleita(Artcol). Artikkeiden tykkäämisellä on tykkäyksen lisäämisaika. Yksi käyttäjä voi tykätä useampaa artikkelia ja yhdellä artikkelilla voi olla useampaa tykkääjää. 

-Sovelluksella on ylläpitäjä(Admin), ylläpitäjällä voi olla monta päiväkirjaa toiminnoistaan, mutta yksi päiväkirja liittyy vain yhteen ylläpitäjään. 
