TAXRUNNER
==========================================================================================
* Author: Daniel Kvist
* E-mail: dk@danielkvist.net
* Python version: 2.7

1. Quick & dirty game
-------------------------------------------------------------------------------------------
1. Kör taxrunner.py
2. Styr med uppåtpilen
3. Enter tar dig snabbt genom menyer

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

