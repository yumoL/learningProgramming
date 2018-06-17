# Enjoy Movies

Sovellus toimii kurssin tietokantasovellus harjoitustyönä. Harjoitustyössä tehdään elokuvapalvelu, jossa käyttäjä pääsee katsomaan tietokantaan tallennetuja elokuvia ja komentoimaan elokuvia. Lisäksi käyttäjä voi halutessaan tykätä elokuvia.

Sovelluksen ylläpitäjällä on oma liittymä, jonka kautta hän pystyy ylläpitämään käyttäjien jäsentietoja, lisäämään ja poistamaan elokuvia sekä määrittelemään aiheita, joiden perusteella elokuvat luokitellaan.

Toimintoja: 
- Sisään ja ulos kirjautuminen
- Uuden käyttäjän rekisteri
- Kommentin lisääminen
- Elokuvien lisääminen ja poistaminen
- Elokuvien tykkääminen
- Elokuvien luokitus aiheen ja esiintymisajan perusteella
- Elokuvien järjestäytyminen katsojien määrän ja komenttien määrän perusteella


Heroku:

[käyttäjä](https://tsoha-python-elokuvaforuumi.herokuapp.com/1/)
käyttäjätunnus:aleksi salasana:123
               jussi           321

[ylläpitäjä](https://tsoha-python-elokuvaforuumi.herokuapp.com/admin/)
käyttäjätunnus:lym  salasana:123

[Hahmotelma tietokantakaaviosta](https://github.com/yumoL/moviesComment/blob/master/dokumentaatio/tietokankaavio.md)

[User story](https://github.com/yumoL/moviesComment/blob/master/dokumentaatio/userStory.md)

## Yhteenvetokyselyt:
- Yhteenvetokysely löytyy tiedoston [admin/views.py](https://github.com/yumoL/moviesComment/blob/master/application/admin/views.py) riviltä 299, joka on sama kuin"select art.title,account.name,comment.content,comment.addtime from art,account,comment where comment.art_id=art.id and comment.user_id=account.id order by comment.addtime desc;"
Tulos näkyy [herokun sivulta]( https://tsoha-python-elokuvaforuumi.herokuapp.com/admin/comment/list/1/)(siis login->comment list)
- Toinen yhteenvetokysely löytyy tiedoston [home/views.py](https://github.com/yumoL/moviesComment/blob/master/application/home/views.py) riveiltä 235-244, joka on sama kuin"select art.title from art,artcol,account where artcol.user_id=account.id and artcol.art_id=art.id order by artcol.addtime desc;"(account.id on siis sisään kirjautuneen käyttäjän id). Tulos näkyy [sivulta](https://tsoha-python-elokuvaforuumi.herokuapp.com/artcol/1/)(login->user center->liked).


