
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
- Luo sovellukselle paikan Herokuun komennolla (osoitteen pitää olla uniikki)
```
heroku create _osoite_
```

