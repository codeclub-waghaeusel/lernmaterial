# Einheit 6 - Schleifen und Bedingungen: Das Fang-Spiel

**Kategorie:** Schleifen · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 5

---

## Lernziel

Du verbindest Schleifen, Bedingungen und Variablen zu einem kompletten Spiel und weißt, wie du Fehler in deinem Code findest. Am Ende hast du ein Fang-Spiel programmiert: Du fängst fallende Äpfel mit einem Korb, sammelst Punkte und verlierst Leben, wenn du einen Apfel verpasst.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift für die Aufgaben in Phase 1

---

## Phase 1 · Einstieg: Wie läuft ein Spiel ab? *(20 min)*

### Schritt 1 – Der Ablauf eines Handyspiels *(8 min)*

Du kennst bestimmt Spiele, in denen Obst vom Himmel fällt und du es auffangen musst. Hier ist der Ablauf eines solchen Spiels – aber die Karten sind durcheinander geraten:

| Karte | Was passiert |
| ----- | ------------ |
| A | Ein Obststück fällt von oben nach unten. |
| B | Auf dem Bildschirm steht „Game Over". |
| C | Die Punkte stehen auf 0 und du hast 3 Leben. |
| D | Hast du das Obst gefangen? Dann bekommst du einen Punkt. Hast du es verpasst, verlierst du ein Leben. |
| E | Du tippst auf „Start". |
| F | Das Spiel prüft: Hast du noch Leben? Wenn ja, fällt das nächste Obststück. |

Bringe die Karten in die richtige Reihenfolge und schreibe die Buchstaben auf:

`_____ → _____ → _____ → _____ → _____ → _____`

Beantworte dann:

| Frage | Deine Antwort |
| ----- | ------------- |
| Welche Karten wiederholen sich, solange du noch Leben hast? | |
| Bei welcher Karte trifft das Spiel eine Entscheidung (wenn ..., dann ...)? | |

> 💡 **Merke:** In fast jedem Spiel stecken **Wiederholungen** (das Spiel läuft immer weiter) und **Entscheidungen** (gefangen oder verpasst?). Beides zusammen macht ein Spiel aus: eine **Schleife**, in der bei jedem Durchlauf eine **Bedingung** geprüft wird.

### Schritt 2 – Was gerade im Spiel los ist *(7 min)*

Ein Spiel merkt sich, in welcher Lage es gerade steckt. Das nennt man den **Spielzustand**. Verbinde mit einer Linie, was zusammengehört:

| Spielzustand | Was du auf dem Bildschirm siehst |
| ------------ | -------------------------------- |
| Startbildschirm | „Game Over", die Leben sind bei 0 |
| Das Spiel läuft | „Geschafft!", die Ziel-Punktzahl ist erreicht |
| Verloren | Du siehst „Drücke Start", nichts bewegt sich |
| Gewonnen | Obst fällt, Punkte und Leben ändern sich |

> Tipp: Die rechte Spalte ist bewusst durcheinander. Lies jede Zeile genau!

> 💡 **Merke:** Der Spielzustand hängt oft an **Variablen**. Zum Beispiel: Sind die Leben bei 0, ist das Spiel verloren. Das Spiel schaut also ständig auf seine Variablen, um zu wissen, wie es weitergeht.

### Schritt 3 – Der Torwart *(5 min)*

Stell dir einen Torwart beim Elfmeterschießen vor. Ergänze die Lücken:

Der Torwart beobachtet den Ball **die ganze Zeit**, nicht nur einmal am Anfang. Bei jedem Moment fragt er sich: „Fliegt der Ball ins Tor?"

- Wenn **ja**, dann _______________________________________________
- **Sonst** _______________________________________________

Was würde passieren, wenn der Torwart nur **ein einziges Mal** am Anfang auf den Ball schaut und danach wegsieht?

____________________________________________________________________________________________________________________________________

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor deine Antworten aus den Schritten 1 bis 3.

---

## Phase 2 · Schleife und Bedingung in Scratch testen *(20 min)*

### Schritt 1 – Neues Projekt öffnen *(2 min)*

Öffne ein **neues Scratch-Projekt**. Behalte die Katze. Dieses Projekt ist nur zum Ausprobieren – dein Spiel baust du danach in einem weiteren neuen Projekt.

### Schritt 2 – Nur einmal prüfen oder immer wieder? *(9 min)*

Baue zuerst dieses Skript für die Katze:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[falls <wird Mauszeiger berührt?>]       ← Steuerung (orange) / Fühlen (hellblau)
    [sage "Hab dich!" für 0.5 Sekunden]  ← Aussehen (lila)
```

**Teste:** Klicke die grüne Flagge und bewege den Mauszeiger **danach** auf die Katze. Reagiert die Katze?

Baue das Skript jetzt um. Die Bedingung kommt **in eine Schleife**:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [falls <wird Mauszeiger berührt?>]   ← Steuerung (orange) / Fühlen (hellblau)
        [sage "Hab dich!" für 0.5 Sekunden]  ← Aussehen (lila)
```

**Teste:** Bewege den Mauszeiger jetzt auf die Katze und wieder weg. Was ist anders als vorher?

> 💡 **Merke:** Ein „falls" prüft **nur einmal**, nämlich genau dann, wenn Scratch an dem Block ankommt. Damit das Spiel **ständig** prüft, muss das „falls" **in einer Schleife** stecken – wie der Torwart, der den Ball die ganze Zeit beobachtet.

Hake ab:

- [ ] Ohne Schleife reagiert die Katze nicht, wenn ich den Mauszeiger erst nach dem Klick auf die Flagge auf sie bewege
- [ ] Mit Schleife reagiert die Katze jedes Mal, wenn ich sie berühre
- [ ] Ich kann erklären, warum das „falls" in die Schleife gehört

### Schritt 3 – Etwas fällt herunter *(9 min)*

Jetzt eine Schleife, die von selbst aufhört, und eine Bedingung darin. Lösche das alte Skript der Katze und baue dieses neue Skript:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[gehe zu x: 0 y: 150]                    ← Bewegung (blau)
[wiederhole bis <y-Position < -150>]     ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
    [ändere y um -5]                     ← Bewegung (blau)
    [falls <wird Mauszeiger berührt?>]   ← Steuerung (orange) / Fühlen (hellblau)
        [sage "Gefangen!" für 0.5 Sekunden]  ← Aussehen (lila)
[sage "Unten angekommen!" für 2 Sekunden]  ← Aussehen (lila)
```

**Teste:** Starte das Skript mit der grünen Flagge, damit die Katze fällt, und versuche, die Katze mit dem Mauszeiger zu fangen. Starte es dann noch einmal und bewege die Maus diesmal nicht. Wann sagt die Katze „Gefangen!"? Und was sagt sie in beiden Fällen am Ende?

> 💡 **Merke:** Die Schleife sorgt für das **Wiederholen**, das „falls" sorgt für das **Entscheiden**. Zusammen entsteht daraus ein Spielablauf.

Hake ab:

- [ ] Die Katze fällt von oben nach unten
- [ ] Sie sagt „Gefangen!", wenn ich sie mit der Maus berühre
- [ ] Erst **nach** der Schleife sagt sie „Unten angekommen!", egal ob ich sie berührt habe oder nicht

---

## Phase 3 · Das Fang-Spiel bauen *(35 min)*

### Schritt 1 – Figuren, Variablen und der Korb *(7 min)*

Öffne ein **neues Scratch-Projekt** und lösche die Katze.

1. Wähle einen **Hintergrund** (zum Beispiel „Blue Sky" oder „Garden").
2. Wähle als Spieler einen **Korb** (zum Beispiel „Bowl") und als Fang-Objekt einen **Apfel** (oder etwas anderes, das fallen kann).
3. Lege zwei Variablen an: **Punkte** und **Leben** (jeweils für alle Figuren).

Klicke den **Korb** an und baue:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[gehe zu x: 0 y: -130]                   ← Bewegung (blau)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [falls <Taste Pfeil rechts gedrückt?>]   ← Steuerung (orange) / Fühlen (hellblau)
        [ändere x um 10]                 ← Bewegung (blau)
    [falls <Taste Pfeil links gedrückt?>]    ← Steuerung (orange) / Fühlen (hellblau)
        [ändere x um -10]                ← Bewegung (blau)
```

**Teste:** Kannst du den Korb mit den Pfeiltasten nach links und rechts bewegen?

Hake ab:

- [ ] Hintergrund, Korb und Apfel sind in der Szene
- [ ] Die Variablen `Punkte` und `Leben` gibt es
- [ ] Der Korb lässt sich mit den Pfeiltasten steuern

### Schritt 2 – Der Apfel fällt *(7 min)*

Klicke den **Apfel** an und baue:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[setze Punkte auf 0]                     ← Variablen (orange-rot)
[setze Leben auf 3]                      ← Variablen (orange-rot)
[gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [ändere y um -6]                     ← Bewegung (blau)
    [falls <y-Position < -165>]          ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
        [gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
```

**Teste:** Fällt der Apfel herunter und taucht dann oben an einer neuen Stelle wieder auf?

Hake ab:

- [ ] Der Apfel fällt und startet danach wieder oben
- [ ] Er startet jedes Mal an einer anderen Stelle

### Schritt 3 – Den Apfel fangen *(7 min)*

Ergänze im Skript des Apfels **in der Schleife** eine zweite Bedingung. Sie kommt direkt unter die erste:

```
    [falls <wird Korb berührt?>]         ← Steuerung (orange) / Fühlen (hellblau)
        [ändere Punkte um 1]             ← Variablen (orange-rot)
        [gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
```

> 💡 **Tipp:** Im Block „wird … berührt?" wählst du aus dem Menü die Figur **Korb** aus.

**Teste:** Starte das Spiel und fange an, Äpfel mit dem Korb zu fangen. Lass auch hin und wieder einen Apfel fallen. Schau dabei auf den Punktestand auf der Bühne. Bleibt der Punktestand gleich?

Hake ab:

- [ ] Beim Fangen steigt der Punktestand um 1
- [ ] Der Apfel erscheint nach dem Fangen wieder oben

### Schritt 4 – Leben und Spielende *(8 min)*

Bisher läuft das Spiel für immer. Jetzt bekommt es einen Spielzustand: Es läuft, solange du noch Leben hast.

1. Wenn der Apfel unten ankommt (und nicht gefangen wurde), soll `Leben` um 1 sinken.
2. Die Schleife soll aufhören, wenn `Leben` bei 0 ist. Dafür tauschst du „wiederhole fortlaufend" gegen „wiederhole bis".
3. Wenn du 10 Punkte hast, hast du gewonnen.

Dein Skript für den Apfel sieht danach so aus:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[setze Punkte auf 0]                     ← Variablen (orange-rot)
[setze Leben auf 3]                      ← Variablen (orange-rot)
[gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
[wiederhole bis <Leben = 0>]             ← Steuerung (orange) / Operatoren (grün)
    [ändere y um -6]                     ← Bewegung (blau)
    [falls <wird Korb berührt?>]         ← Steuerung (orange) / Fühlen (hellblau)
        [ändere Punkte um 1]             ← Variablen (orange-rot)
        [gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
    [falls <y-Position < -165>]          ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
        [ändere Leben um -1]             ← Variablen (orange-rot)
        [gehe zu x: (zufallszahl von -200 bis 200) y: 170]  ← Bewegung (blau) / Operatoren (grün)
    [falls <Punkte = 10>]                ← Steuerung (orange) / Operatoren (grün)
        [sage "Gewonnen!" für 2 Sekunden]    ← Aussehen (lila)
        [stoppe alle]                    ← Steuerung (orange)
[sage "Game Over!" für 2 Sekunden]       ← Aussehen (lila)
[stoppe alle]                            ← Steuerung (orange)
```

**Teste:** Spiele das Spiel zweimal: einmal, bis du verlierst, und einmal, bis du gewinnst.

Hake ab:

- [ ] Bei jedem verpassten Apfel sinkt `Leben` um 1
- [ ] Bei 0 Leben erscheint „Game Over!" und das Spiel stoppt
- [ ] Bei 10 Punkten erscheint „Gewonnen!" und das Spiel stoppt
- [ ] Ein neuer Start mit der Flagge setzt Punkte und Leben zurück

### Schritt 5 – Fehler-Detektiv *(6 min)*

Auch erfahrene Programmierer bauen Fehler ein. Wichtig ist, sie systematisch zu finden. Dabei hilft diese Methode:

1. **Beobachten:** Was passiert genau? Was sollte passieren?
2. **Vermuten:** Welcher Block könnte schuld sein?
3. **Ändern:** Ändere nur **eine** Sache.
4. **Testen:** Ist der Fehler weg?

Baue jetzt zwei Fehler **absichtlich** ein und finde heraus, was dann passiert. Überlege dir vorher, was du erwartest! Mit Strg+Z oder dem Zurückbauen machst du den Fehler danach wieder weg.

| Fehler einbauen | Was passiert? Warum? |
| --------------- | -------------------- |
| Lösche im „falls Korb berührt"-Block den Block `gehe zu ...` | |
| Ziehe das „falls Korb berührt" **aus** der Schleife heraus, direkt vor „wiederhole bis" | |

> 💡 **Tipp:** Willst du sehen, was in einer Variablen steckt? Setze das Häkchen neben der Variablen, dann zeigt Scratch den Wert auf der Bühne an.

> 🌟 **Bonusaufgabe:** Mach das Spiel schwerer, je länger es läuft! Lege eine Variable `Tempo` an (Startwert `-6`). Benutze `ändere y um (Tempo)` und baue beim Fangen `ändere Tempo um -0.5` ein. Oder baue eine zweite Figur (zum Beispiel eine Bombe), bei der du ein Leben verlierst, wenn du sie fängst.

---

## Phase 4 · Abschluss & Reflexion *(15 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 6 – mein Fang-Spiel`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Warum muss ein „falls" in einer Schleife stehen, wenn das Spiel ständig prüfen soll?
- [ ] Woran erkennt das Spiel, dass es verloren ist?
- [ ] Was passiert, wenn du `setze Leben auf 3` **in** die Schleife schreibst statt davor?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Spiele dem Mentor dein fertiges Fang-Spiel vor und zeige ihm, welche Teile des Skripts sich wiederholen und wo das Spiel eine Entscheidung trifft.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| ------- | ------ |
| Der Korb bewegt sich nicht | Prüfe, ob die beiden „falls"-Blöcke **innerhalb** von „wiederhole fortlaufend" stecken und ob du den **Korb** (nicht den Apfel) ausgewählt hast. |
| Der Apfel fällt nur einmal | Der Block `gehe zu ... y: 170` fehlt im „falls". Ohne ihn bleibt der Apfel unten liegen. |
| Die Punkte steigen sehr schnell auf 10 | Nach dem Fangen muss der Apfel wieder nach oben springen (`gehe zu ... y: 170`). Sonst berührt er den Korb weiter und zählt immer wieder. |
| Der Apfel wird nie gefangen | Prüfe, ob das „falls wird Korb berührt?" **in** der Schleife steht und im Menü wirklich **Korb** gewählt ist. |
| Das Spiel hört nie auf | „wiederhole bis" endet nur, wenn `Leben = 0` wahr wird. Prüfe, ob `Leben` wirklich um 1 sinkt (`ändere Leben um -1`). |
| Punkte und Leben starten nicht bei 0 und 3 | `setze Punkte auf 0` und `setze Leben auf 3` müssen **vor** der Schleife stehen, nicht darin. |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 7

Hast du gemerkt, dass der Block `gehe zu x: (zufallszahl von -200 bis 200) y: 170` in deinem Skript dreimal vorkommt? In der nächsten Einheit lernst du **eigene Blöcke** kennen: Du baust sie einmal und benutzt sie überall. Außerdem lernst du **Klone** kennen, mit denen du viele gleiche Objekte gleichzeitig erzeugen kannst, zum Beispiel für ein Shooter-Spiel.

---
