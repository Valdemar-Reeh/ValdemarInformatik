# Billedbehandling med p5js
Samling af js programmer til undervisningsbrug i billedmanipulation, eller billedbehandling. Programmerne kan køres med live-server gennem `index.html` filen ved at henvise til den rigtige js fil.

Filerne er lavet med js biblioteket P5.js.

# slides til undervisningen
[Billedmanipulation1 slides](https://drive.google.com/open?id=1wM5pYU8eP08tujXp0M8mXqXdc9tLOkgLNUVAJqtBMC8)

[Billedmanipulation2 slides](https://drive.google.com/open?id=1fPLhh2m5WEBlbgeCrJ2RMZLczG5zBS4olBct83mYDsc)

[Billedmanipulation3 slides](https://drive.google.com/open?id=1BeQpWCXfe0y37lRzftKbN7Sgs3_KrUnRzLoD5M9uwK4)


# Projektbeskrivelse - Billedmanipulation
Med udgangspunkt i følgende case, skal du udvikle en del af en løsning.
 
Alle ved at billeder af hvordan verden, og især os selv, ser ud er dybt uinteressante. For at ændre på dette skal I lave et billedbehandlingsprogram.


I skal derfor udvikle et program, der
* Kan redigere et billede ved manipulation på pixelniveau.
* Kan tilføje effekter.
 
I den forbindelse skal I have fokus på brugeren hvor I skal
* Bestemme hvad der er kerne- og sekundære-faciliteter.
* Udføre en brugertest og en tilretning af projektet.

I logbogen skal I dokumentere arbejdsprocessen og produktet undervejs.



# Eksterne links
[Verden første biograffilm, renset med neurale netværk](https://www.digg.com/2020/arrival-train-la-ciotat-upscaled?fbclid=IwAR3bCpLX0sIkNvhxPS7i8quwEmbEHXKBScwYMc5FR-L-sOh3lbNUwr_k4r0)


# JS fil gennem index.html
Vi bruger biblioteket p5.js, og kører vores js fil gennem en html side. Nedenunder er index filen som også ligger på github siden.
```
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>p5.js example</title>
    <style> body {padding: 0; margin: 0;} </style>
    <script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script>
    <script src="JSfiler/generalFilterSharpening.js"></script>
  </head>
</html>
```
De to vigtige linjer er,
```<script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script> ```, hvor p5.js biblioteket indlæses og
```     <script src="JSfiler/generalFilterSharpening.js"></script> ```, hvor js filen ```generalFilterSharpening.js```indlæses.


## Øvelse
* Download JSfiler folderen og åben den som projekt VS-Code.
* Ret ```<script src="JSfiler/generalFilterSharpening.js"></script> ``` så det er ```HelloWorld.js``` filen som bruges.
* Brug liveserver til at se resultatet, det virker vist ikke med Prewiew HTML.

## Opsætning af Teletype

Hvis man vil samarbejde om samme dokument, kan man bruge Teletype. Efter en har delt sit dokument kan det gemmes og køres lokalt.

Gå ind på:

Præferencer -> install -> Teletype og enable den.

Klik nederst på "radiotårnet" og følge linket til en token.

Del filen med på "radiotårnet" og send link til de andre.

# Programmet online på Github

I kan bruge Github til at køre jeres programmer online. Index.html filen skal indeholde reference til js filen og så skal den gøres tilgængelig.

på Github skal I gå in i:
index.html -> Settings -> options -> Github pages.

Denne siden kan ses på
[https://mpsteenstrup.github.io/Billedmanipulation/](https://mpsteenstrup.github.io/Billedmanipulation/)

Indsæt selv brugernavn og repository
 `https://username.github.io/repository/`

# Programoversigt
## simple programmer til introduktion
* `HelloWorld.js`
* `simpleImageLoad.js`
* `sortHvis.js`, brug af indbygget filter

## Loade og genne billeder i programmet
* `loadImage.js`
* `saveImage.js`

## forståelse af pixels, i,j
* `loopIJColors.js`, 4x4 pixels
* `getPixelValue.js`, pixelværd
* `getPixelValueFast.js`, implementering af hurtig læsning af pixelværdier, ved brug af liste.

## manuelle filtre
* `generalFilter.js`
* `generalFilterSharpening.js`
* `posterFilter.js`
* `blurFilter.js`
* `gradientFilter.js`
* `KantdetektionFilterManuel.js`
* `pixelate.js`

## flere filtre hvor man opdaterer pixelværdierne under vejs
* `filterSaveUpdatePixelValues.js`

# opgaver til nogle af programmerne

## colorFilterManuel
fill((c[0]+c[1]+c[2])/3);

* undersøg hvad c indeholder
* undersøg hvordan billedet ser ud med c[i], i=0,1,2
* Hvordan laver man et farvefilter?

## Gradient farvefilter
fill((c[0]+c[1]+c[2])/(3)-j);

* Kør filtret og se hvad det gør
* lav en forbedring så det ser ordentligt ud

## Kantdetektion

* Undersøg hvad koden gør

## Billedbehandling i GIMP
I GIMP vælg: Filters -> Generic -> convolution matrix.

Generelle regler for foldning.

Hvis samme fortegn giver det en udglatning

Hvis modsat fotegn giver det en tydeligere kant.

## Hvorfor blur filtre ofte er forkerte
her er en lille video som forklare det, (https://www.youtube.com/watch?v=LKnqECcg6Gw)[https://www.youtube.com/watch?v=LKnqECcg6Gw].
