`
# Asennusohje

## Hakemiston lataaminen
- Mennään projektin [etusivulle](https://github.com/yumoL/learningProgramming) ja klikataan painiketta Clone or downloads ja sitten painiketta Download Zip.
- Puretaan tiedostopakkauksen, jonka jälkeen saadaan hakemisto learningProgramming-master.

## Projektin lähettäminen herokuun
- Mennään hakemiston sisälle komennolla
```
cd learningProgramming-master
```
- Luodaan hakemisto sisälle  Python-virtuaaliympäristö komennolla 
```
python3 -m venv venv
```
- Aktivoidaan python-ympäristön komennolla
```
source venv/bin/activate
```

- Asennetaan riippuvuudet virtuaaliseen ympäristöön
```
pip install -r requirements.txt
```
- Päivitetään Flask uudempaan versioon komennolla
```
pip install --upgrade pip
```
- Kirjaudutaan sisään Herokuun komennolla, tai jos käyttäjätunnusta ei vielä ole, pitää mennä Herokun [etusivulle](https://id.heroku.com/login) rekisteröimään.
```
heroku login
```
- Luodaan sovellukselle paikan Herokuun komennolla (osoitteen nimen pitää olla uniikki)
```
heroku create "nimi"
```
- Luodaan projektikansiolle git-versionhallinta komennolla
```
git init
```

- Lisätään projektin koodit versiohallintaan komennolla
```
heroku git:remote -a "nimi"
```
- Lähetetään projektin Herokuun komennoilla
```
git add .
git commit -m"initial configuartion"
git push heroku master
```
- Lisätään seuraavaksi sovelluksen käyttöön tieto siitä, että sovellus on Herokussa
```
heroku config:set HEROKU=1
```
- Lisätään Herokuun tietokanta. 
```
heroku addons:add heroku-postgresql:hobby-dev
```
Nyt sovellus on Herokussa ja sen osoite on 
### https://"nimi".herokuapp.com/1/
