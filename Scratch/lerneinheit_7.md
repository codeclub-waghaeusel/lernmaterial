# Einheit 7 - Eigene Blöcke und Klone: Das Weltraum-Spiel

**Kategorie:** Fortgeschritten · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 6

---

## Lernziel

Du baust eigene Blöcke, die du überall wiederverwenden kannst, und benutzt Klone, um viele gleiche Objekte zu erzeugen. Am Ende hast du ein Weltraum-Spiel programmiert: Du steuerst ein Raumschiff, schießt auf Gegner und sammelst Punkte.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift für die Aufgaben in Phase 1

---

## Phase 1 · Einstieg: Einmal aufschreiben, oft benutzen *(20 min)*

### Schritt 1 – Das Aufwärmprogramm *(8 min)*

Ein Fußballtrainer macht vor jedem Training dasselbe Aufwärmprogramm: **5 Minuten joggen, 10 Hampelmänner, 5 Minuten dehnen.** Dann folgt die Übung des Tages. Seine Trainingsplan-Zettel für drei Tage sehen so aus:

| Tag | Plan ohne Abkürzung |
| --- | ------------------- |
| Montag | 5 Minuten joggen, 10 Hampelmänner, 5 Minuten dehnen, Pass-Übung |
| Mittwoch | 5 Minuten joggen, 10 Hampelmänner, 5 Minuten dehnen, Elfmeterschießen |
| Freitag | 5 Minuten joggen, 10 Hampelmänner, 5 Minuten dehnen, Trainingsspiel |

Der Trainer hat eine Idee: Er gibt dem Aufwärmprogramm den Namen „Aufwärmen". Auf dem Plan steht dann nur noch „Aufwärmen". Einmal, ganz oben, erklärt er, was „Aufwärmen" bedeutet.

Schreibe den Plan für Montag mit dem Namen des Aufwärmprogramms auf:

`_____________________________________________________________`

Beantworte dann:

| Frage | Deine Antwort |
| ----- | ------------- |
| Der Trainer will statt 10 Hampelmännern lieber 20. An wie vielen Stellen muss er **ohne** Abkürzung etwas ändern? | |
| An wie vielen Stellen muss er **mit** Abkürzung etwas ändern? | |

> 💡 **Merke:** Wenn du mehrere Schritte oft brauchst, gibst du ihnen einen **Namen**. Du erklärst den Namen einmal und benutzt ihn dann überall. In Scratch heißt das: ein **eigener Block**. Ändern musst du nur an einer einzigen Stelle etwas.

### Schritt 2 – Vorlage und Kopien *(7 min)*

Beim Plätzchenbacken gibt es eine Form zum Ausstechen. Mit ihr entstehen viele Plätzchen, die alle gleich aussehen. Verbinde mit einer Linie, was zusammengehört:

| Backen | Was es bedeutet |
| ------ | --------------- |
| Die Ausstechform (die Vorlage) | Du isst ein Plätzchen auf. Die Kopie ist weg. |
| Ein einzelnes Plätzchen (die Kopie) | Jedes Plätzchen bekommt andere Streusel. |
| Etwas, das bei jeder Kopie anders sein darf | Gibt vor, wie alle Plätzchen aussehen. |
| Eine Kopie loswerden | Eines von vielen Plätzchen, das aus der Form entstanden ist. |

> Tipp: Die rechte Spalte ist bewusst durcheinander. Lies jede Zeile genau!

> 💡 **Merke:** In Scratch heißen solche Kopien **Klone**. Eine Figur ist die Vorlage, und sie kann beliebig viele Klone erzeugen. Alle Klone folgen derselben Bauanleitung, aber jeder Klon kann an einer anderen Stelle sein.

### Schritt 3 – Die Pizza-Bestellung *(5 min)*

Eine Pizzeria hat den Namen „Pizza backen" für ihr Rezept: Teig ausrollen, Soße verteilen, Belag drauf, backen. Der **Belag** ist aber jedes Mal ein anderer. Ergänze die Lücken:

- Max bestellt: „Pizza mit _______________"
- Lena bestellt: „Pizza mit _______________"

Was ist bei jeder Bestellung **gleich**? ____________________________________________

Was ist bei jeder Bestellung **anders**? ____________________________________________

> 💡 **Merke:** Die Lücke, die du bei jeder Benutzung anders füllst, heißt **Parameter**. Ein eigener Block kann so einen Parameter haben, zum Beispiel „hüpfen (Höhe)".

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor deine Antworten aus den Schritten 1 bis 3.

---

## Phase 2 · Eigene Blöcke und Klone testen *(20 min)*

### Schritt 1 – Neues Projekt öffnen *(2 min)*

Öffne ein **neues Scratch-Projekt**. Behalte die Katze. Dieses Projekt ist nur zum Ausprobieren – dein Spiel baust du danach in einem weiteren neuen Projekt.

### Schritt 2 – Der eigene Block „hüpfen" *(9 min)*

Klicke in der Blockpalette links auf die Kategorie **Meine Blöcke** (rosa). Klicke auf **Neuen Block erstellen**, gib ihm den Namen `hüpfen` und klicke auf **Fertig**.

Es erscheint ein Block „Definiere hüpfen". Baue darunter:

```text
[Definiere hüpfen]                       ← Meine Blöcke (rosa)
    [ändere y um 40]                     ← Bewegung (blau)
    [warte 0.2 Sekunden]                 ← Steuerung (orange)
    [ändere y um -40]                    ← Bewegung (blau)
```

Dein neuer Block `hüpfen` liegt jetzt in der Kategorie **Meine Blöcke**. Baue zwei Skripte, die ihn benutzen:

```text
[Wenn Taste Leertaste gedrückt wird]     ← Ereignisse (gelb)
[hüpfen]                                 ← Meine Blöcke (rosa)

[Wenn diese Figur angeklickt wird]       ← Ereignisse (gelb)
[hüpfen]                                 ← Meine Blöcke (rosa)
```

**Teste:** Drücke die Leertaste und klicke dann auf die Katze. Hüpft sie beide Male gleich hoch? Ändere danach in „Definiere hüpfen" beide Zahlen (`40` und `-40`) auf `80` und `-80`. Teste noch einmal: Hast du an den beiden Skripten mit `hüpfen` etwas ändern müssen?

Jetzt kommt der **Parameter**. Rechtsklick auf „Definiere hüpfen" → **Bearbeiten**. Klicke auf **Zahl- oder Textargument hinzufügen**, nenne es `Höhe` und klicke auf **Fertig**. Ziehe das runde `Höhe` in die beiden `ändere y`-Blöcke. Für das Runterfallen brauchst du den grünen Block „ ... - ... " aus **Operatoren**:

> 💡 **So liest du die Skripte ab jetzt:** Zeilen mit **+** sind neu, die baust du ein. Zeilen mit **-** nimmst du heraus. **⋮** steht für Blöcke, die bleiben, wie sie sind. Alle anderen Zeilen hast du schon.

```diff
- [Definiere hüpfen]                       ← Meine Blöcke (rosa)
+ [Definiere hüpfen (Höhe)]                ← Meine Blöcke (rosa)
-     [ändere y um 80]                     ← Bewegung (blau)
+     [ändere y um (Höhe)]                 ← Bewegung (blau)
      [warte 0.2 Sekunden]                 ← Steuerung (orange)
-     [ändere y um -80]                    ← Bewegung (blau)
+     [ändere y um (0 - (Höhe))]           ← Bewegung (blau) / Operatoren (grün)
```

Der Block `hüpfen` hat jetzt ein Feld. Schreibe in den beiden Skripten eine Zahl hinein:

```diff
  [Wenn Taste Leertaste gedrückt wird]     ← Ereignisse (gelb)
- [hüpfen]                                 ← Meine Blöcke (rosa)
+ [hüpfen 20]                              ← Meine Blöcke (rosa)

  [Wenn diese Figur angeklickt wird]       ← Ereignisse (gelb)
- [hüpfen]                                 ← Meine Blöcke (rosa)
+ [hüpfen 100]                             ← Meine Blöcke (rosa)
```

**Teste:** Drücke die Leertaste und klicke dann auf die Katze. Welcher Hüpfer ist höher?

> 💡 **Merke:** Der eigene Block steht **einmal** da (in „Definiere"). Du benutzt ihn, so oft du willst. Mit einem Parameter kann jede Benutzung ein bisschen anders sein.

Hake ab:

- [ ] Die Katze hüpft bei Leertaste **und** bei Klick
- [ ] Nach der Änderung in „Definiere" hüpft sie in beiden Fällen höher, ohne dass ich die anderen Skripte angefasst habe
- [ ] Mit dem Parameter hüpft die Katze bei der Leertaste niedriger als beim Klick

### Schritt 3 – Klone erzeugen *(9 min)*

Klicke auf **Figur wählen** und füge einen **Ball** hinzu (oder eine andere kleine Figur). Klicke den **Ball** an und baue:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[verstecke dich]                         ← Aussehen (lila)

[Wenn ich als Klon starte]               ← Steuerung (orange)
[zeige dich]                             ← Aussehen (lila)
[gehe zu zufälliger Position]            ← Bewegung (blau)
[wiederhole 10 mal]                      ← Steuerung (orange)
    [drehe dich ↻ um 15 Grad]            ← Bewegung (blau)
    [warte 0.1 Sekunden]                 ← Steuerung (orange)
[lösche diesen Klon]                     ← Steuerung (orange)
```

Klicke dann die **Katze** an und baue:

```text
[Wenn Taste k gedrückt wird]              ← Ereignisse (gelb)
[erzeuge Klon von Ball]                   ← Steuerung (orange)
```

> 💡 **Tipp:** Im Block „erzeuge Klon von" steht zuerst **mir selbst**. Klicke auf das kleine Dreieck ▼ und wähle **Ball** aus. Genauso wählst du im gelben Block die Taste **k** aus.

**Teste:** Klicke die grüne Flagge. Der Ball ist jetzt versteckt. Drücke dann die Taste **k** dreimal schnell hintereinander. Wie viele Bälle siehst du? Was passiert nach einer Sekunde mit jedem Ball?

> 💡 **Merke:** Die Vorlage bleibt versteckt. Jeder Klon muss sich selbst zeigen. Und jeder Klon muss sich am Ende wieder **löschen**, sonst bleibt er für immer und das Spiel wird langsam.

Hake ab:

- [ ] Bei jedem Druck auf **k** erscheint ein neuer Ball an einer anderen Stelle
- [ ] Alle Bälle drehen sich und verschwinden dann wieder
- [ ] Ich kann erklären, warum der Ball am Anfang versteckt ist

---

## Phase 3 · Das Weltraum-Spiel bauen *(35 min)*

### Schritt 1 – Das Raumschiff mit eigenem Block *(7 min)*

Öffne ein **neues Scratch-Projekt** und lösche die Katze.

1. Wähle einen **Hintergrund** (zum Beispiel „Stars" oder „Space").
2. Füge die Figur **Rocketship** hinzu und nenne sie `Raumschiff`.
3. Lege zwei Variablen an: **Punkte** und **Leben** (jeweils für alle Figuren).

Klicke das **Raumschiff** an. Erstelle einen eigenen Block `steuern` und baue:

```text
[Definiere steuern]                      ← Meine Blöcke (rosa)
    [falls <Taste Pfeil rechts gedrückt?> dann] ← Steuerung (orange) / Fühlen (hellblau)
        [ändere x um 10]                 ← Bewegung (blau)
    [falls <Taste Pfeil links gedrückt?> dann] ← Steuerung (orange) / Fühlen (hellblau)
        [ändere x um -10]                ← Bewegung (blau)

[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[gehe zu x: 0 y: -140]                   ← Bewegung (blau)
[setze Punkte auf 0]                     ← Variablen (orange-rot)
[setze Leben auf 3]                      ← Variablen (orange-rot)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [steuern]                            ← Meine Blöcke (rosa)
```

> 💡 **Tipp:** Das Raumschiff soll nach oben zeigen. Zeigt deine Figur in eine andere Richtung, drehe das Kostüm im Reiter „Kostüme", bis es nach oben zeigt.

**Teste:** Starte das Spiel mit der grünen Flagge. Kannst du das Raumschiff mit den Pfeiltasten nach links und rechts bewegen?

Hake ab:

- [ ] Hintergrund und Raumschiff sind in der Szene
- [ ] Die Variablen `Punkte` und `Leben` gibt es
- [ ] Das Raumschiff lässt sich mit den Pfeiltasten steuern, und der Block `steuern` wird benutzt

### Schritt 2 – Schüsse als Klone *(8 min)*

Füge eine kleine Figur als Schuss hinzu (zum Beispiel „Ball" oder eine andere kleine Figur) und nenne sie `Schuss`. Klicke den **Schuss** an und baue:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[verstecke dich]                         ← Aussehen (lila)

[Wenn ich als Klon starte]               ← Steuerung (orange)
[gehe zu Raumschiff]                     ← Bewegung (blau)
[zeige dich]                             ← Aussehen (lila)
[wiederhole bis <(y-Position) > 150>]    ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
    [ändere y um 10]                     ← Bewegung (blau)
[lösche diesen Klon]                     ← Steuerung (orange)
```

Klicke danach das **Raumschiff** an und ergänze ein weiteres Skript:

```text
[Wenn Taste Leertaste gedrückt wird]     ← Ereignisse (gelb)
[erzeuge Klon von Schuss]                ← Steuerung (orange)
[warte 0.3 Sekunden]                     ← Steuerung (orange)
```

> 💡 **Tipp:** Im Block „gehe zu" wählst du aus dem Menü das **Raumschiff** aus. Im Block „erzeuge Klon von" wählst du den **Schuss** aus.

**Teste:** Starte das Spiel mit der grünen Flagge. Bewege das Raumschiff und drücke die Leertaste. Kommt der Schuss aus dem Raumschiff? Drücke die Leertaste mehrmals, auch während du das Schiff bewegst. Fliegen mehrere Schüsse gleichzeitig? Was passiert mit jedem Schuss am oberen Rand?

Hake ab:

- [ ] Bei jedem Druck auf die Leertaste fliegt ein Schuss los
- [ ] Mehrere Schüsse sind gleichzeitig auf der Bühne
- [ ] Jeder Schuss verschwindet am oberen Rand

### Schritt 3 – Gegner als Klone *(8 min)*

Füge eine Figur als Gegner hinzu (zum Beispiel „Ghost" oder „Bat") und nenne sie `Gegner`. Klicke den **Gegner** an und baue:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[verstecke dich]                         ← Aussehen (lila)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [erzeuge Klon von mir selbst]        ← Steuerung (orange)
    [warte 1 Sekunden]                   ← Steuerung (orange)

[Wenn ich als Klon starte]               ← Steuerung (orange)
[gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
[zeige dich]                             ← Aussehen (lila)
[wiederhole bis <(y-Position) < -150>]   ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
    [ändere y um -4]                     ← Bewegung (blau)
    [falls <wird Schuss berührt?> dann]  ← Steuerung (orange) / Fühlen (hellblau)
        [ändere Punkte um 1]             ← Variablen (orange-rot)
        [lösche diesen Klon]             ← Steuerung (orange)
[ändere Leben um -1]                     ← Variablen (orange-rot)
[lösche diesen Klon]                     ← Steuerung (orange)
```

**Teste:** Starte das Spiel mit der grünen Flagge. Schieße auf einen Gegner und schau auf den Punktestand auf der Bühne. Lass danach einen anderen Gegner unten ankommen und schau auf `Leben`. Was passiert mit den beiden Variablen?

Hake ab:

- [ ] Jede Sekunde erscheint ein neuer Gegner oben an einer anderen Stelle
- [ ] Wenn ein Schuss einen Gegner trifft, verschwindet der Gegner und `Punkte` steigt um 1
- [ ] Wenn ein Gegner unten ankommt, verschwindet er und `Leben` sinkt um 1

### Schritt 4 – Ein eigener Block mit Parameter *(6 min)*

Das Fallen des Gegners soll ein eigener Block werden, damit du die Geschwindigkeit leicht ändern kannst. Klicke den **Gegner** an. Erstelle einen eigenen Block `fliegen` mit dem Parameter `Tempo`. **Lösche** das alte Skript „Wenn ich als Klon starte" des Gegners und baue stattdessen diese beiden Skripte:

```text
[Definiere fliegen (Tempo)]              ← Meine Blöcke (rosa)
    [wiederhole bis <(y-Position) < -150>] ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
        [ändere y um (0 - (Tempo))]      ← Bewegung (blau) / Operatoren (grün)
        [falls <wird Schuss berührt?> dann] ← Steuerung (orange) / Fühlen (hellblau)
            [ändere Punkte um 1]         ← Variablen (orange-rot)
            [lösche diesen Klon]         ← Steuerung (orange)

[Wenn ich als Klon starte]               ← Steuerung (orange)
[gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
[zeige dich]                             ← Aussehen (lila)
[fliegen 4]                              ← Meine Blöcke (rosa)
[ändere Leben um -1]                     ← Variablen (orange-rot)
[lösche diesen Klon]                     ← Steuerung (orange)
```

**Teste:** Starte das Spiel und spiele ein paar Sekunden. Ändere dann `fliegen 4` auf `fliegen 8` und starte das Spiel noch einmal. Was ist anders?

Hake ab:

- [ ] Das Spiel funktioniert genauso wie vorher
- [ ] Mit `fliegen 8` fallen die Gegner schneller als mit `fliegen 4`
- [ ] Ich musste für die Geschwindigkeit nur eine einzige Zahl ändern

### Schritt 5 – Gewonnen und Game Over *(6 min)*

Bisher läuft das Spiel für immer. Klicke das **Raumschiff** an und ergänze im Flaggen-Skript **in der Schleife**, unter `steuern`, zwei Bedingungen:

```diff
  [Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
  [gehe zu x: 0 y: -140]                   ← Bewegung (blau)
  [setze Punkte auf 0]                     ← Variablen (orange-rot)
  [setze Leben auf 3]                      ← Variablen (orange-rot)
  [wiederhole fortlaufend]                 ← Steuerung (orange)
      [steuern]                            ← Meine Blöcke (rosa)
+     [falls <(Punkte) = 10> dann]         ← Steuerung (orange) / Operatoren (grün) / Variablen (orange-rot)
+         [sage "Gewonnen!" für 2 Sekunden]    ← Aussehen (lila)
+         [stoppe alles]                   ← Steuerung (orange)
+     [falls <(Leben) < 1> dann]           ← Steuerung (orange) / Operatoren (grün) / Variablen (orange-rot)
+         [sage "Game Over!" für 2 Sekunden]   ← Aussehen (lila)
+         [stoppe alles]                   ← Steuerung (orange)
```

**Teste:** Spiele das Spiel zweimal: einmal, bis du 10 Punkte hast, und einmal, bis du alle Leben verloren hast. Wo auf der Bühne siehst du jeweils die Nachricht?

Hake ab:

- [ ] Bei 10 Punkten erscheint „Gewonnen!" und das Spiel stoppt
- [ ] Bei 0 Leben erscheint „Game Over!" und das Spiel stoppt
- [ ] Ein neuer Start mit der Flagge setzt Punkte und Leben zurück

> 🌟 **Bonusaufgabe:** Mach das Spiel abwechslungsreicher! Benutze `fliegen (zufallszahl von 2 bis 8)`, damit jeder Gegner ein anderes Tempo hat. Oder baue im Gegner-Block eine zweite Bedingung ein: Berührt ein Gegner das Raumschiff, verlierst du ein Leben, und der Gegner verschwindet.

---

## Phase 4 · Abschluss & Reflexion *(15 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 7 – mein Weltraum-Spiel`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Wozu ist ein eigener Block gut? Was musst du ändern, wenn sich etwas darin ändern soll?
- [ ] Was ist ein Parameter? Nenne ein Beispiel aus deinem Spiel.
- [ ] Was ist der Unterschied zwischen der Vorlage und einem Klon?
- [ ] Was passiert, wenn ein Klon sich nie löscht?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Spiele dem Mentor dein fertiges Weltraum-Spiel vor und zeige ihm, wo du einen eigenen Block benutzt und wo Klone entstehen.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| ------- | ------ |
| Der Schuss oder der Gegner ist von Anfang an sichtbar | Die Vorlage braucht im Flaggen-Skript den Block `verstecke dich`. Der Klon zeigt sich dann selbst mit `zeige dich`. |
| Es erscheinen keine Schüsse | Prüfe, ob im Block `erzeuge Klon von` wirklich der **Schuss** ausgewählt ist und ob das Skript beim **Raumschiff** liegt. Prüfe auch, ob unter „Wenn ich als Klon starte" im Schuss ein `zeige dich` steht. |
| Der Schuss kommt nicht aus dem Raumschiff | Im Block `gehe zu` muss das **Raumschiff** ausgewählt sein. Die Figur muss genau `Raumschiff` heißen. |
| Der Schuss fliegt nach oben und bleibt dort hängen | Der Block `lösche diesen Klon` fehlt am Ende des Klon-Skripts. Er steht **nach** der Schleife, nicht darin. |
| Ein Treffer zählt nicht | Prüfe, ob im Block `wird … berührt?` der **Schuss** ausgewählt ist. Ist der Schuss sehr klein, triff den Gegner genau in der Mitte. |
| Der eigene Block tut nichts | Der Block muss im Skript auch **benutzt** werden. „Definiere" allein reicht nicht. Prüfe außerdem, ob der Block bei der richtigen Figur liegt. Eigene Blöcke gehören immer zu einer Figur. |
| Der Parameter `Tempo` lässt sich nicht in `ändere y um` ziehen | Ziehe das runde `Tempo` aus dem Block „Definiere" in das Eingabefeld. Es ist in „Definiere fliegen" selbst zu finden, nicht in der Palette. |
| Ein verpasster Gegner kostet zwei Leben | Beim Gegner gibt es noch das alte Skript „Wenn ich als Klon starte". Lösche es, sodass nur das Skript mit `fliegen` übrig ist. |
| Das Spiel wird immer langsamer | Irgendwo bleiben Klone übrig. Prüfe, ob **jedes** Klon-Skript mit `lösche diesen Klon` endet, auch beim Gegner, der unten ankommt. |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 8

In der letzten Einheit entscheidest du selbst! Du planst ein eigenes Projekt (ein Spiel, eine Geschichte, ein Quiz oder eine Animation), baust es und stellst es der Gruppe vor. Dabei kannst du alles verwenden, was du gelernt hast: Variablen, Bedingungen, Schleifen, eigene Blöcke und Klone.

---
