# Sovelluksen rajoitteet ja puuttuvat ominaisuudet
## Kokonaisuus
### Sivutus
- Sovelluksessa on sivutus, mutta se sivunumero, jossa käyttäjä on, ei ole merkitty esim. toisella värillä, joten käyttäjä  voi olla vaikeus muistaa, missä sivussa hän on.
Sivunumero, jossa käyttäjä on, voisi merkitty seuraavasti: 
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/sivutuksenIdea.jpg">
- Jos sivussa ei ole yhtään dataa(esim. tyhjässä kommenttisivussa ei ole yhtään kommenttia),painiketta "last page" klikatessa käyttäjä ohjataan 404-sivuun.
Painikkeen "last page" pitäisi olla autimaattisesti pois käytöstä, jos sivussa ei ole yhtään dataa. 

### Ajan formaatti ja aikavyöhyke


## Ylläpitäjä
### Artikkelin muokkaaminen
Artikkelin muokkaaminen on toteutettu sillä tavalla, että ylläpitäjä voi muokata muiden ylläpitäjien artikkeleita, mikä johtuu siitä, että artikkelin tietokantataulu art ei ole yhdistetty ylläpitäjän tietokantatauluun admin viiteavaimen admin_id kautta. Olisi hyvää, että vain artikkelin kirjoittajalla on oikeus muokata omaa artikkelia.

### Ylläpitäjän autorisointi
Sovelluksen ylläpitäjällä on kaksi roolia, super-ylläpitäjä ja tavallinen ylläpitäjä. Ylläpitäjän tietokantataulun attribuutin is_super perusteella voidaan päätellä, onko kirjautuneena oleva super-ylläpitäjä ja tavallinen ylläpitäjä. Ylläpitäjän roolit kannattaisi tallentaa erillisenä tietokantauluna.

### Ylläpitäjän lisääminen ja salasanan suojaaminen

## Käyttäjä
### Artikkelin kommentoiminen
Artikkelin kommentoiminen vaatii käyttäjän sisäänkirjautumista. Kirjautumisen jälkeen käyttäjä ohjataan uudestaan etusivuun eikä siihen sivuun, jossa kommentoitava artikkeli on, jolloin käyttäjä joutuu etsimään artikkelia uudestaan. Tämä voi olla työlästä erityisesti silloin, kun artikkeleita on paljon. Samalla kun käyttäjä menee uudestaan artikkelin lukemissivuun kirjautumisen jälkeen, artikkelin lukijien määrä kasvaa yhdellä, mikä ei ole järkevää. Lukeminen, joka tapahtuu ennen kirjautumista ja kirjautumisen jälkeen, pitää laskea samaksi lukemiskerraksi. 
