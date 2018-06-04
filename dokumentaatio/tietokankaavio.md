<img src="https://github.com/yumoL/moviesComment/blob/master/dokumentaatio/tietokantakaavio.png">

-Käyttäjä(User) käyttää sovellusta, jokaisella käyttäjällä on oma uniikki käyttäjätunnus(name), salasana(pwd) ja rekisteröinnin aika(addtime)

Elokuvalla(Movie) on nimi(title),sen sisällön kuvaus(info),url-osoite(url), jonka kautta elokuva lähetettään palvelimelle. Lisäksi elokuvalla on katsojien määrä(playnum) ja komenttien määrä(commentnum),sekä alue(area),julkaisuaika(release_time),pituus(length) ja lisäämisaika(addtime). Yksi elokuva kuuluu vain yheen kategoriaan(Tag), toisaalta yhdellä kategorialla voi olla useampaa elokuvaa. 

-Käyttäjä kirjoittaa kometteja(Comment) elokuvista. Komentilla on sisältö(content) ja muokkaamisaika(addtime). Yksi käyttäjä voi kirjoittaa useita komentteja useammasta elokuvasta, yhdellä komentilla on vain yksi kirjoittaja.

-Käyttäjä voi tykätä elokuvia(Moviecol). Elokuvien tykkäämisellä on tykkäyksen lisäämisaika. Yksi käyttäjä voi tykätä useampaa elokuvaa ja yhdellä elokuvalla on olla useampaa tykkääjää. 

-Sovelluksella on ylläpitäjä(Admin), ylläpitäjällä voi olla monta päiväkirjaa toiminnoistaan, mutta yksi päiväkirja liittyy vain yhteen ylläpitäjään. 
