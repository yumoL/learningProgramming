# Yhteenvetokyselyt 
Yhteenvetokyselyt on toteutettu sovelluksessa eri tavoin kuin kurssin materialissa.
- Ensimmäinen yhteenvetokyely löytyy tiedoston [application/admin/views.py](https://github.com/yumoL/learningProgramming/blob/master/application/admin/views.py) riveiltä 292-293:
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/admin/yhteenvetokysely1.png">

Sen tulos näytetään tiedoston [application/templates/admin/comment_list.html](https://github.com/yumoL/learningProgramming/blob/master/application/templates/admin/comment_list.html) riveillä 17-33:
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/admin/tulos1.png">
eli<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/admin/commentList.png">
Yhteenvetokysely on sama kuin "SELECT account.name,art.title,comment.content,comment.addtime FROM account,art,comment WHERE comment.user_id=account.id AND comment.art_id=art.id ORDER BY comment.addtime desc;"

- Toinen yhteenvetokysely löytöö tiedoston [application/home/views.py](https://github.com/yumoL/learningProgramming/blob/master/application/home/views.py) riveiltä 241-250:
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/k%C3%A4ytt%C3%A4j%C3%A4/yhteenvetokysely2.png">

Sen tulos näytetään tiedoston  [application/templates/home/artcol.html](https://github.com/yumoL/learningProgramming/blob/master/application/templates/home/artcol.html) riveillä 10-21:
<img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/k%C3%A4ytt%C3%A4j%C3%A4/tulos2.png">
eli <img src="https://github.com/yumoL/learningProgramming/blob/master/dokumentaatio/pictures/k%C3%A4ytt%C3%A4j%C3%A4/tyk%C3%A4tyt%20artikkelit.png">
Yhteenvetokysely on sama kuin "SELECT art.title FROM account,art,artcol WHERE account.id=session["user_id"] AND art.id=artcol.art_id AND artcol.user_id=account.id ORDER BY artcol.addtime desc;"
