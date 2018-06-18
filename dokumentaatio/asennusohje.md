`
# Asennusohje

## Hakemiston lataaminen
- Mene projektin [etusivulle](https://github.com/yumoL/learningProgramming) ja klikkaa painiketta Clone or downloads ja sitten painiketta Download Zip.
- Pura tiedostopakkauksen, jonka jälkeen saadaan hakemisto learningProgramming-master.

## Projektin lähettäminen herokuun
- Mene hakemiston sisälle komennolla
```
cd learningProgramming-master
```
- Luo hakemisto sisälle  Python-virtuaaliympäristö komennolla 
```
python3 -m venv venv
```
- Aktivoi python-ympäristön komennolla
```
source venv/bin/activate
```

- Asenna riippuvuudet virtuaaliseen ympäristöön
```
pip install -r requirements.txt
```
- Päivitä Flask uudempaan versioon komennolla
```
pip install --upgrade pip
```
- Kirjaudu sisään Herokuun komennolla, tai jos käyttäjätunnusta ei vielä ole, pitää mennä Herokun [etusivulle](https://id.heroku.com/login) rekisteröimään.
```
heroku login
```
- Luo sovellukselle paikan Herokuun komennolla (osoitteen nimen pitää olla uniikki, oletataan tässä, että osoitteen nimi on artikkelipalvelu)
```
heroku create artikkelipalvelu
```
- Luo projektikansiolle git-versionhallinta komennolla
```
git init
```

- Lisää projektin koodit versiohallintaan komennolla
```
heroku git:remote -a artikkelipalvelu
```
- Lähetä projektin Herokuun komennoilla
```
git add .
git commit -m"initial configuartion"
git push heroku master
```

