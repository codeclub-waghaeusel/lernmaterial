# Einheit 3 - Variablen: Punkte zählen & speichern

**Kategorie:** Grundkonzepte · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 2

---

## Lernziel

Du verstehst, was eine Variable ist, und kannst sie in Scratch anlegen und verwenden. Am Ende hast du dein Klickspiel aus Einheit 2 mit einem echten Punktezähler ausgebaut – mit Spielernamen und einem Zeitlimit.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift für die Aufgabe in Phase 1
- Gespeichertes Klickspiel aus Einheit 2

---

## Phase 1 · Einstieg: Was ist eine Variable? *(20 min)*

### Schritt 1 – Das Punktezettel-Experiment *(10 min)*

Stell dir vor, du spielst mit Freunden ein Kartenspiel. Jemand schreibt die Punkte auf einen Zettel – und streicht den alten Wert durch, wenn sich etwas ändert.

**Füll die Tabelle aus – was steht nach jeder Runde auf dem Zettel?**

| Runde | Was passiert | Punkte |
| :-----: | ------------- | :------: |
| Start | Spiel beginnt | 0 |
| 1 | Du sammelst zwei Münzen (+2) | ☐ |
| 2 | Du sammelst eine Münze (+1) | ☐ |
| 3 | Du verlierst drei Münzen (−3) | ☐ |
| 4 | Du sammelst fünf Münzen (+5) | ☐ |
| 5 | Du verlierst eine Münze (−1) | ☐ |

> 💡 **Das ist eine Variable!** Der Zettel „Punkte" merkt sich immer den aktuellen Stand. Er kann sich verändern – größer, kleiner, null – aber es gibt immer genau **einen** aktuellen Wert. In Scratch macht eine Variable genau das: Sie ist ein **Platzhalter** mit einem Namen, der während das Programm läuft einen Wert speichert. Das Programm kann diesen Wert jederzeit lesen („Wie viele Punkte hat der Spieler gerade?"), verändern („+1 Punkt!") oder neu setzen z. B. wenn das Spiel neu gestartet wird („Spiel neu gestartet → 0 Punkte"). Ohne Variablen könnte dein Programm nichts merken – es wäre, als würdest du das Kartenspiel spielen, ohne jemals aufzuschreiben, wer wie viele Punkte hat.

Schreib in deinen eigenen Worten auf, was eine Variable ist:

`_____________________________________________________________`

### Schritt 2 – Zwei wichtige Blöcke *(10 min)*

In Scratch gibt es zwei wichtige Blöcke, um mit Variablen zu arbeiten:

- Block 1: `setze ... auf ...` → setzt eine Variable auf einen bestimmten Wert
- Block 2: `ändere ... um ...` → verändert die Variable um einen bestimmten Wert

Verbinde jedes Beispiel mit einer Linie mit dem, was es bewirkt:

| Block | ..... | Was er macht |
| ------- | ------ | ------------- |
| **setze Punkte auf 0** | | Variablen können jeden beliebigen Wert annehmen – nicht nur 0 oder 1 |
| **ändere Punkte um 1** | | Speichert Text (eine Zeichenfolge) statt einer Zahl |
| **setze Punkte auf 42** | | Setzt eine Variable auf einen festen Startwert – egal was vorher drin war |
| **setze Name auf "Alex"** | | Zählt eine Zahl zum aktuellen Wert hinzu – oder zieht sie ab (mit negativer Zahl) |

> 💡 **Merke:** `setze ... auf ...` ist wie ein neuer leerer Zettel – du schreibst ganz von vorne, mit einem beliebigen Wert. `ändere ... um ...` ist wie eine Strichliste – du addierst etwas dazu oder ziehst es ab. Und: Variablen können nicht nur **Zahlen** speichern, sondern auch **Text** – zum Beispiel einen Namen. Text in einer Variable nennt man **Zeichenfolge** (auf Englisch: *String*).

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor deine ausgefüllte Tabelle und Verbindungsaufgabe.

---

## Phase 2 · Variable testen *(20 min)*

### Schritt 1 – Neues Projekt öffnen *(2 min)*

Öffne ein **neues Scratch-Projekt**. Behalte die Katze. Dieses Projekt ist nur zum Ausprobieren – dein Klickspiel lädst du danach in Phase 3.

### Schritt 2 – Variable anlegen *(5 min)*

Lege eine Variable an und hake ab:

- [ ] Klicke in der Blockpalette auf **„Variablen"** (orange-rot)
- [ ] Klicke auf **„Neue Variable"** (links oben)
- [ ] Gib der Variable den Namen `Punkte` und bestätige mit OK
- [ ] Oben links auf der Bühne erscheint jetzt eine kleine Anzeige: **Punkte 0**

### Schritt 3 – Variable ausprobieren *(13 min)*

Baue für die Katze dieses Test-Skript:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[setze Punkte auf 0]                     ← Variablen (orange-rot)
[warte 2 Sekunden]                       ← Steuerung (orange)
[ändere Punkte um 1]                     ← Variablen (orange-rot)
[warte 2 Sekunden]                       ← Steuerung (orange)
[ändere Punkte um 1]                     ← Variablen (orange-rot)
```

**Teste:** Klicke die grüne Flagge und schau auf die Anzeige **Punkte** oben links auf der Bühne.

Hake ab, was du ausprobiert hast:

- [ ] Variable startet bei 0, wenn ich die Flagge klicke
- [ ] Nach 2 Sekunden springt sie auf 1, dann auf 2
- [ ] Ich habe „ändere Punkte um 5" versucht – was passiert?
- [ ] Ich habe „ändere Punkte um −1" versucht – was passiert?

> 💡 **Tipp:** Ob eine Variable auf der Bühne sichtbar ist, steuerst du mit dem Häkchen neben dem Variablennamen in der Blockpalette unter „Variablen". Häkchen weg = Variable versteckt, Häkchen da = Variable sichtbar.

---

## Phase 3 · Das Klickspiel mit Punkten ausbauen *(35 min)*

### Schritt 1 – Spielernamen abfragen & Punktezähler einbauen *(15 min)*

Lade dein gespeichertes **Klickspiel aus Einheit 2**: Datei → **Von deinem Computer hochladen**. Falls du das Projekt nicht mehr hast, baue die Figur, die zufällig springt, wie in Einheit 2 noch einmal.

Lege im Klickspiel zwei Variablen an (die Variable aus dem Testprojekt gehört nur zum Testprojekt):

- Klicke auf „Neue Variable" → Name: `Punkte`
- Klicke auf „Neue Variable" → Name: `Name`. Das ist eine **Text-Variable**: Das Spiel soll den Namen des Spielers abfragen und ihn begrüßen.

Klicke deine **Figur** an. Ergänze im **Flaggen-Skript** ganz oben, direkt unter „Wenn grüne Flagge angeklickt wird":

> 💡 **So liest du die Skripte ab jetzt:** Zeilen mit **+** sind neu, die baust du ein. Zeilen mit **-** nimmst du heraus. **⋮** steht für Blöcke, die bleiben, wie sie sind. Alle anderen Zeilen hast du schon.

```diff
  [Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
+ [frage "Wie heißt du?" und warte]        ← Fühlen (hellblau)
+ [setze Name auf (Antwort)]               ← Variablen (orange-rot) / Fühlen (hellblau)
+ [sage (Name) für 2 Sekunden]             ← Aussehen (lila) / Variablen (orange-rot)
+ [setze Punkte auf 0]                     ← Variablen (orange-rot)
  [setze Größe auf 100 %]                  ← Aussehen (lila)
  [gehe zu x: 0 y: 0]                      ← Bewegung (blau)
  [wiederhole fortlaufend]                 ← Steuerung (orange)
      [warte 1 Sekunden]                   ← Steuerung (orange)
      [gehe zu zufälliger Position]        ← Bewegung (blau)
```

**Wo finde ich „frage ... und warte"?** → Kategorie **Fühlen** (hellblau), ganz oben in der Liste.

> 💡 **Tipp:** Die Klammern `( )` zeigen dir einen **runden Block**, den du in ein Feld ziehst. Den runden Block **Antwort** findest du unter **Fühlen**, den runden Block **Name** unter **Variablen**, sobald du die Variable angelegt hast. **Tippe die Wörter nicht ein!** Sonst sagt die Figur nur das Wort „Name" statt deines Namens.

> 💡 **Was passiert hier?** Der Block `frage ... und warte` öffnet ein Eingabefeld auf der Bühne. Was der Spieler tippt, landet automatisch in einer speziellen Variable namens **„Antwort"**. Mit `setze Name auf (Antwort)` kopierst du diesen Text in deine eigene Variable `Name` – die du dann überall im Spiel verwenden kannst. Das ist ein Beispiel für eine **Zeichenfolge** (Text) in einer Variable, genauso wie du es in Phase 1 gelernt hast!

Jetzt noch den **Punktezähler**: Ergänze im **Klick-Skript** ganz unten einen Block:

```diff
  [Wenn diese Figur angeklickt wird]        ← Ereignisse (gelb)
  [spiele Klang Meow]                       ← Klang (pink)
  [sage "Treffer! +1 Punkt" für 1 Sekunden] ← Aussehen (lila)
  [ändere Größe um -10]                     ← Aussehen (lila)
+ [ändere Punkte um 1]                      ← Variablen (orange-rot)
```

**Teste:** Klicke die grüne Flagge und gib deinen Namen ein. Triff dann die Figur ein paarmal und schau auf die Anzeige **Punkte** auf der Bühne.

Hake ab:

- [ ] Die Figur fragt beim Start nach meinem Namen
- [ ] Die Figur sagt meinen Namen für 2 Sekunden
- [ ] Punkte starten bei 0, wenn ich die Flagge drücke
- [ ] Punkte steigen um 1 bei jedem Treffer
- [ ] Figur wird trotzdem kleiner wie in Einheit 2

### Schritt 2 – Spiel ausprobieren und anpassen *(5 min)*

Spiele dein Spiel ein paar Mal durch:

- [ ] Wie viele Punkte schaffst du in einem Durchgang? Notiere deinen Rekord: ______
- [ ] Ändere die Wartezeit auf `0.5` Sekunden – wird das Spiel schwieriger?
- [ ] Ändere die Wartezeit auf `2` Sekunden – wird das Spiel leichter?

> 💡 **Warum steht `setze Punkte auf 0` vor dem "Wiederhole fortlaufend"-Block (Programmierer sagen dazu "Schleife")?**
> Weil er nur **einmal** ausgeführt werden soll – gleich beim Start. Blöcke *vor* der Schleife laufen einmal. Blöcke *innerhalb* der Schleife laufen immer wieder. Wenn `setze Punkte auf 0` in der Schleife wäre, würden die Punkte bei jedem Sprung der Figur auf 0 zurückgesetzt!

### Schritt 3 – Zeitlimit einbauen *(15 min)*

Dein Spiel hat einen Punktezähler, aber kein Zeitlimit. Das ändern wir jetzt!

Erstelle eine dritte Variable mit dem Namen `Zeit`:

- Klicke auf „Neue Variable" → Name: `Zeit`

Baue ein **neues, viertes Skript** neben deine anderen Skripte:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[setze Zeit auf 15]                      ← Variablen (orange-rot)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [warte 1 Sekunden]                   ← Steuerung (orange)
    [ändere Zeit um -1]                  ← Variablen (orange-rot)
    [falls <(Zeit) < 1> dann]            ← Steuerung (orange) / Operatoren (grün) / Variablen (orange-rot)
        [sage "Zeit abgelaufen!" für 2 Sek.]  ← Aussehen (lila)
        [stoppe alles]                   ← Steuerung (orange)
```

> 💡 **Tipp:** Die spitzen Klammern `< >` zeigen dir einen **sechseckigen Block**: Ziehe den grünen Block „ ... < ... " aus **Operatoren** in das Feld von „falls". In sein linkes Feld ziehst du den runden Block **Zeit** aus **Variablen** (nicht eintippen!), in das rechte Feld tippst du `1`.

> 💡 **Erklärung:** Die Variable `Zeit` startet bei 15 und zählt jede Sekunde um 1 runter. Wenn sie unter 1 fällt – also 0 erreicht – ist die Zeit abgelaufen und das Spiel stoppt. Du hast **15 Sekunden**, so viele Treffer wie möglich zu landen!

**Teste:** Klicke die grüne Flagge und schau auf die Anzeige **Zeit** auf der Bühne. Was passiert, wenn sie bei 0 ankommt?

Hake ab:

- [ ] Variable „Zeit" startet bei 15 und zählt runter
- [ ] Das Spiel stoppt, wenn die Zeit 0 erreicht
- [ ] Punkte und Zeit werden beide auf der Bühne angezeigt
- [ ] Ich habe die Startzeit auf `10` geändert – wird das Spiel schwieriger?

> 🌟 **Bonusaufgabe:** Mach das Spiel mit jedem Treffer schneller! Lege eine Variable `Wartezeit` an. Setze sie im Flaggen-Skript vor der Schleife auf `1` und benutze in der Schleife `warte (Wartezeit) Sekunden`. Baue ins Klick-Skript `ändere Wartezeit um -0.05` ein. Wie viele Punkte schaffst du jetzt?

---

## Phase 4 · Abschluss & Reflexion *(15 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 3 – Klickspiel mit Punkten`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Was ist eine Variable? (Erkläre es mit dem Punktezettel-Beispiel aus Phase 1!)
- [ ] Was ist der Unterschied zwischen „setze Punkte auf 0" und „ändere Punkte um 1"?
- [ ] Warum muss „setze Punkte auf 0" *vor* der Schleife stehen und nicht darin?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor dein fertiges Spiel.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| --------- | -------- |
| Variable erscheint nicht auf der Bühne | Setze den Haken neben dem Variablennamen in der Blockpalette unter „Variablen". |
| Punkte zählen nicht hoch | Prüfe, ob „ändere Punkte um 1" im **Klick-Skript** steckt – nicht im Flagge-Skript. |
| Punkte starten nicht bei 0 | Prüfe, ob „setze Punkte auf 0" ganz oben im Flagge-Skript steht, *vor* der Schleife. |
| Die Figur fragt nicht nach dem Namen | Ist „frage ... und warte" ganz oben im Flagge-Skript, *vor* der Schleife? Den Block findest du unter **Fühlen** (hellblau). |
| Zeit zählt nicht runter | Ist das Zeit-Skript ein **separates** Skript neben den anderen? Es darf nicht am Flagge-Skript hängen. |
| Spiel stoppt sofort beim Start | Prüfe, ob „setze Zeit auf 15" *vor* der Schleife im Zeit-Skript steht. |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 4

In der nächsten Einheit lernst du **Bedingungen** kennen – dann kann dein Programm selbst Entscheidungen treffen: Ist die Antwort richtig oder falsch? Damit baust du ein Quiz-Spiel, das Punkte vergibt.

---
