# Sovelluksen rajoitteet ja puuttuvat ominaisuudet
## Kokonaisuus
### Sivutus
- Sovelluksessa on sivutus, mutta se sivunumero, jossa käyttäjä on, ei ole merkitty esim. toisella värillä, joten käyttäjä  voi olla vaikeus muistaa, missä sivussa hän on.
Sivunumero, jossa käyttäjä on, voisi merkitty seuraavasti: 
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/sivutuksenIdea.jpg">
- Jos sivussa ei ole yhtään dataa(esim. tyhjässä kommenttisivussa ei ole yhtään kommenttia),painiketta "last page" klikatessa käyttäjä ohjataan 404-sivuun.
Painikkeen "last page" pitäisi olla autimaattisesti pois käytöstä, jos sivussa ei ole yhtään dataa. 

### Aikaformaatti ja aikavyöhyke
Aikaformaatti näyttää normaalilta paikalisessa Sqlitessä, mutta kun siirrytään PostgreSQL:ään aiakformaatti on muodossa"2018-06-24 13:00:12.266359", joka näyttää vähän sekavalta. Myös PostgreSQL:ään tallennuttu aika on aina kolme tuntia myöhemmin kuin paikallista aikaa johtuen kenties siitä, että PostgreSQL:ässä käytetään paikallisen ajan sijaan palvelimen aikaa. 


## Ylläpitäjä
### Artikkelin muokkaaminen
Artikkelin muokkaaminen on toteutettu sillä tavalla, että ylläpitäjä voi muokata muiden ylläpitäjien artikkeleita, mikä johtuu siitä, että artikkelin tietokantataulu art ei ole yhdistetty ylläpitäjän tietokantatauluun admin viiteavaimen admin_id kautta. Olisi hyvää, että vain artikkelin kirjoittajalla on oikeus muokata omaa artikkelia.

### Ylläpitäjän autorisointi
Sovelluksen ylläpitäjällä on kaksi roolia, super-ylläpitäjä ja tavallinen ylläpitäjä. Ylläpitäjän tietokantataulun attribuutin is_super perusteella voidaan päätellä, onko kirjautuneena oleva super-ylläpitäjä ja tavallinen ylläpitäjä. Ylläpitäjän roolit kannattaisi tallentaa erillisenä tietokantauluna.

### Ylläpitäjän lisääminen ja salasanan suojaaminen
Ylläpitäjä lisätään suoraan tietokantaan kommentorivillä, jonka seurauksena ylläpitäjän salasana on selkolielinen eikä ole suojautu esim. hajautustaulun avulla. 

## Käyttäjä
### Artikkelin kommentoiminen
Artikkelin kommentoiminen vaatii käyttäjän sisäänkirjautumista. Kirjautumisen jälkeen käyttäjä ohjataan uudestaan etusivuun eikä siihen sivuun, jossa kommentoitava artikkeli on, jolloin käyttäjä joutuu etsimään artikkelia uudestaan. Tämä voi olla työlästä erityisesti silloin, kun artikkeleita on paljon. Samalla kun käyttäjä menee uudestaan artikkelin lukemissivuun kirjautumisen jälkeen, artikkelin lukijien määrä kasvaa yhdellä, mikä ei ole järkevää. Lukeminen, joka tapahtuu ennen kirjautumista ja kirjautumisen jälkeen, pitää laskea samaksi lukemiskerraksi. 

### Linkki artikkelissa
Artikkelin muokkaamisessa voidaan lisätä linkkejä, mutta linkit eivät toimi käyttäjän lukemissivussa. 
