# Learning Programming

Sovellus toimii kurssin tietokantasovellus harjoitustyönä. Harjoitustyössä tehdään artikkelipalvelu, jossa käyttäjä pääsee lukemaan tietokantaan tallennetuja artikkeleita ohjelmoinnista ja komentoimaan artikkeleita. Lisäksi käyttäjä voi tykätä artikkeleita.

Sovelluksen ylläpitäjällä on oma liittymä, jonka kautta hän pystyy ylläpitämään käyttäjien jäsentietoja, lisäämään ja poistamaan artikkeleita sekä määrittelemään aiheita, joiden perusteella elokuvat luokitellaan.

Toimintoja: 
- Sisään ja ulos kirjautuminen
- Uuden käyttäjän rekisteri
- Kommentin lisääminen
- Artikkeleiden lisääminen ja poistaminen
- Artikeleiden tykkääminen
- Artikkeleiden luokitus aiheen perusteella
- Elokuvien järjestäytyminen lukejien ja komenttien määrän perusteella


Heroku:

[käyttäjä](https://tsoha-python-elokuvaforuumi.herokuapp.com/1/)
käyttäjätunnus:aleksi salasana:123
käyttäjätunnus:jussi  salasana:321

[ylläpitäjä](https://tsoha-python-elokuvaforuumi.herokuapp.com/admin/)
käyttäjätunnus:lym  salasana:123

## Dokumentaatio

[Hahmotelma tietokantakaaviosta](https://github.com/yumoL/moviesComment/blob/master/dokumentaatio/tietokankaavio.md)

[User story](https://github.com/yumoL/moviesComment/blob/master/dokumentaatio/userStory.md)

[Käyttöohje](https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

[Asennusohje](https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/asennusohje.md)

## Yhteenvetokyselyt:
- Yhteenvetokysely löytyy tiedoston [admin/views.py](https://github.com/yumoL/moviesComment/blob/master/application/admin/views.py) riviltä 299, joka on sama kuin"select art.title,account.name,comment.content,comment.addtime from art,account,comment where comment.art_id=art.id and comment.user_id=account.id order by comment.addtime desc;"
Tulos näkyy [herokun sivulta]( https://tsoha-python-elokuvaforuumi.herokuapp.com/admin/comment/list/1/)(siis login->comment list)
- Toinen yhteenvetokysely löytyy tiedoston [home/views.py](https://github.com/yumoL/moviesComment/blob/master/application/home/views.py) riveiltä 235-244, joka on sama kuin"select art.title from art,artcol,account where artcol.user_id=account.id and artcol.art_id=art.id order by artcol.addtime desc;"(account.id on siis sisään kirjautuneen käyttäjän id). Tulos näkyy [sivulta](https://tsoha-python-elokuvaforuumi.herokuapp.com/artcol/1/)(login->user center->liked).


