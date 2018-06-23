# Sovelluksen rajoitteet ja puuttuvat ominaisuudet
## Sivutus
- Sovelluksessa on sivutus, mutta se sivunumero, jossa käyttäjä on, ei ole merkitty esim. toisella värillä, joten käyttäjä  voi olla vaikeus muistaa, missä sivussa hän on.
Sivunumero, jossa käyttäjä on, voisi merkitty seuraavasti: 
<img src="">
- Jos sivussa ei ole yhtään dataa(esim. tyhjässä kommenttisivussa ei ole yhtään kommenttia),painiketta "last page" klikatessa käyttäjä ohjataan 404-sivuunn.
Painikkeen "last page" pitäisi olla autimaattisesti pois käytöstä, jos sivussa ei ole yhtään dataa. 

## Artikkelin muokkaaminen
Artikkelin muokkaaminen on toteutettu sillä tavalla, että ylläpitäjä voi muokata muiden ylläpitäjien artikkeleita, mikä johtuu siitä, että 
artikkelin tietokantataulu art ei ole yhdistetty ylläpitäjän tietokantatauluun admin viiteavaimen admin_id kautta. Olisi hyvää, että vain artikkelin 
kirjoittajalla on oikeus muokata omaa artikkelia.

## Artikkelin kommentoiminen

