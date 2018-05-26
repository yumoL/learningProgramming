<img src="https://github.com/yumoL/moviesComment/blob/master/dokumentaatio/tietokantakaavio.png">

-Käyttäjä(User) käyttää sovellusta, jokaisella käyttäjällä on oma uniikki käyttäjätunnus(name), salasana(pwd) ja rekisteröinnin aika(addtime)

-Käyttäjä kirjoittaa arvoteluja(Art) jostain elokuvasta. Kirjoituksella on otsikko(title), kategoria(tag), sisältö(content) ja muokkaamisaika(addtime). Yksi käyttäjä voi kirjoittaa monta kirjoitusta, yhdellä kirjoituksella on vain yksi kirjoittaja.

-Käyttäjä voi kommentoida(Comment) muiden kirjoituksia. Jokaisella komentilla on sisältö(content) ja muokkaamisaika(addtime). Käyttäjällä voi olla monta kommentia, mutta yhdellä komentilla on vain yksi kirjoittaja. Yhdellä kirjoituksella voi olla monta komenttia, mutta yksi komentti vain liittyy yhteen kirjoitukseen.

-Yhdellä käyttäjällä voi olla monta kokoelmaa(Col) esim. artikkelin aiheen perusteella. Yhdessä kokoelmassa voi olla monta kirjoitusta, myös yksi kirjoitus voi kuulua eri käyttäjien kokoelmaan. 

-Sovelluksella on ylläpitäjä(Admin), ylläpitäjällä voi olla monta päiväkirjaa toiminnoistaan, mutta yksi päiväkirja liittyy vain yhteen ylläpitäjään. 
