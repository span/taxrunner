*******************************************************************************************
* TAXRUNNER
*******************************************************************************************
* Author: Daniel Kvist
* E-mail: danielkvist81@gmail.com
* Python version: 2.7
* OS: OS X
*******************************************************************************************

*********************
* Innehåll
*********************
1. Quick & dirty game
2. Introduktion
3. Storyline
4. Lösning
5. Lärdomar
6. Vidare

1. Quick & dirty game
-------------------------------------------------------------------------------------------
1. Kör taxrunner.py
2. Styr med uppåtpilen
3. Enter tar dig snabbt genom menyer

2. Introduktion
-------------------------------------------------------------------------------------------
Den här filen beskriver lösningen övergripande tillsammans med nyttiga lärdomar som
dragits under utvecklingen av spelet. Den avslutas med tankar kring hur en vidareutveckling
skulle kunna ha sett ut.

3. Storyline
-------------------------------------------------------------------------------------------
Den är den typiska skattefuskarren har du fuskat sitt sista fusk; skattmasen är ute efter 
att ta dig! Därför gäller det att samla på sig så mycket kosing man bara kan innan man
åker dit!

Not:
Ursprungstanken var även att storyn skulle ha en djupare tanke där spelaren egentligen var
infiltratör för internationell polis som bekämpade skattefusk. Tyvärr så har spelmotorn
tagit så pass mycket tid i att utveckla så det har inte funnits tid till att implementera
detta. I framtiden dock så kanske... ;)

4. Övergripande beskrivning av lösningen
-------------------------------------------------------------------------------------------
Spelet startas genom att köra filen 'taxrunner.py'. Denna fil importerar sedan klassen
'Game' och startar spelet. När spelet startas så körs ett obligatorisk intro som laddas
från 'Intro' klassen. När intro klassen returnerar till Game klassen så börjar spelet.

Game klassen sköter det övergripande för spelet så som beräkning av poäng med hjälp av
klassen 'Score', navigering i menyer med hjälp av 3e parts klassen 'Menu'. Game laddar
även in en 'Level' som innehåller alla delarna i spelet.

'Level' klassen använder sig av flera klasser som är 'Sprite'-klasser. Dessa klasser
har alla en 'update' method som anropas vid varje spel-tick i game loopen. Då uppdateras
varje enskild sprite's position.

Om spelaren 'Player' ramlar ner mellan platformarna så är omgången i spelet slut. Det
görs då en koll om spelaren satt en high score eller inte och spelaren får isåfall skriva
in sitt namn innan spelet återgår till en meny där man kan välja att starta spelet igen
eller avsluta.

Highscore läses från en textfil som ligger i 'data' mappen.

Animerade sprites ligger i 'actions' mappen.

Statiska bilder ligger i 'world' mappen.

5. Nyttiga lärdomar
-------------------------------------------------------------------------------------------
Efter att ha tillverkar flera spel i Flash och ActionScript sedan tidigare så var det
relativt enkelt att komma igång med Pygame. Att animera sprites och spela ljud var inga
problem. Däremot så kunde väldigt 'enkla' saker så som att rita ut text var väldigt besvärligt,
framförallt om man ville få texten på flera rader eftersom stöd för '\n' saknas.

Därför använder high score listan sig av eztext som är ett 3e-parts skript.

Jämför man med att koda spel i C++ så är det naturligtvis mycket enklare i Python eftersom
man inte behöver ägna lika stor tid åt minneshantering på olika sätt. Därför verkar det som
att Python och Pygame lämpar sig ganska bra för enklare spel men vill man ha riktigt hög
prestanda kanske det inte är aktuellt. Jag har dessutom sett flera exempel på personer som
laddat in sina Python-spel på Android-telefoner, jag har tyvärr inte haft tid att testa
på min egen.

6. Vidare...
-------------------------------------------------------------------------------------------
Vidare utveckling av spelet är naturligtvis möjligt. Jag gillar fortfarande min idé om storyn
och kommer fortsätta ägna den tankar. För att kunna bygga ut med fler monster, banor, hinder
och andra händelser så krävs dock en del arbete. Låt gå för att Python är snabbt att utveckla
i men det tar ändå sin tid när man arbetar själv och inte har 100% koll på hur allting fungerar.

Några självklara features som jag önskat att jag hunnit med är:
* Tydligare poängräkning med '+5000' och '-2000' i stor text när man tar pengar
* Fler 'monster' och 'hinder', aggresivare 'taxman'
* Mer komplex bakgrund med parallax-effekter
* Bättre layoutad high-score lista med egen skärm
* Mer variation på 'banan'
* Att kunna komma i mål på 'banan'
* Träffa andra karaktärer för att måla storyn bättre

Det har iallafall varit en trevlig kurs och jag har äntligen fått tid att lära mig Python,
tack för det!

