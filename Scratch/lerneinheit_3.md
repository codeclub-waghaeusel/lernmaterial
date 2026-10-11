# Einheit 3 - Variablen: Punkte zählen & speichern

**Kategorie:** Grundkonzepte · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 2

---

## Lernziel

Du verstehst, was eine Variable ist, und kannst sie in Scratch anlegen und verwenden. Am Ende hast du dein Klickspiel aus Einheit 2 mit einem echten Punktezähler ausgebaut – und als Bonus mit einem Zeitlimit versehen.

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

_______________________________________________

### Schritt 2 – Vier wichtige Blöcke *(5 min)*

In Scratch gibt es 2 verschiedene Blöcke um mit Variablen zu arbeiten.

- Block 1: `setze ... auf ...` -> setzte eine Variable auf einen bestimmten Wert
- Block 2: `ändere ... um ...` -> verändert die Variable um einen bestimmten Wert

Ordne jedem Block durch verbinden zu was dieser Block bewirkt:

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

### Schritt 3 – Variable in Scratch anlegen *(5 min)*

Öffne ein neues Scratch-Projekt und lege eine Variable an:

- [ ] Klicke in der Blockpalette auf **„Variablen"** (orange-rot)
- [ ] Klicke auf **„Erstelle eine Variable"**
- [ ] Gib der Variable den Namen `Punkte` und bestätige mit OK
- [ ] Oben auf der Bühne erscheint jetzt eine kleine Anzeige: **Punkte: 0**

---

## Phase 2 · Variable testen *(20 min)*

### Schritt 1 – Klickspiel öffnen *(2 min)*

Schließe das Testprojekt und öffne dein gespeichertes **Klickspiel aus Einheit 2** auf scratch.mit.edu.

Falls du das Projekt nicht mehr hast: Erstelle ein neues Projekt mit einer Figur, die sich zufällig bewegt (wie in Einheit 2 beschrieben), und lege eine Variable `Punkte` an.

### Schritt 2 – Variable ausprobieren *(10 min)*

Bevor du das Spiel veränderst, baue ein kleines Test-Skript **neben** deine anderen Skripte (nicht dranhängen!):

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[setze Punkte auf 0]                     ← Variablen (orange-rot)
[warte 2 Sekunden]                       ← Steuerung (orange)
[ändere Punkte um 1]                     ← Variablen (orange-rot)
[warte 2 Sekunden]                       ← Steuerung (orange)
[ändere Punkte um 1]                     ← Variablen (orange-rot)
```

**Schau auf die Bühne!** Die Anzeige oben links zählt hoch.

Hake ab, was du ausprobiert hast:

- [ ] Variable startet bei 0, wenn ich die Flagge klicke
- [ ] Nach 2 Sekunden springt sie auf 1, dann auf 2
- [ ] Ich habe „ändere Punkte um 5" versucht – was passiert?
- [ ] Ich habe „ändere Punkte um −1" versucht – was passiert?

### Schritt 3 – Test-Skript löschen *(8 min)*

Das Test-Skript hat seinen Zweck erfüllt. Lösche es wieder:

**Rechtsklick auf das Test-Skript → „Block löschen"**

> 💡 **Tipp:** Ob eine Variable auf der Bühne sichtbar ist, steuerst du mit dem Häkchen neben dem Variablennamen in der Blockpalette unter „Variablen". Häkchen weg = Variable versteckt, Häkchen da = Variable sichtbar.

---

## Phase 3 · Das Klickspiel mit Punkten ausbauen *(35 min)*

### Schritt 1 – Spielernamen abfragen & Punktezähler einbauen *(15 min)*

Zuerst bauen wir eine **Text-Variable** ein: Das Spiel soll den Namen des Spielers abfragen und ihn begrüßen. Erstelle dazu eine neue Variable mit dem Namen `Name`:

- Klicke auf „Erstelle eine Variable" → Name: `Name`

Ergänze das **Flagge-Skript** ganz oben, vor allem anderen:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[frage "Wie heißt du?" und warte]        ← Fühlen (hellblau)   ← NEU
[setze Name auf Antwort]                 ← Variablen (orange-rot) ← NEU
[sage Name für 2 Sekunden]               ← Aussehen (lila)     ← NEU
[setze Punkte auf 0]                     ← Variablen (orange-rot)  ← NEU
[setze Größe auf 100 %]                  ← Aussehen (lila)
[gehe zu x: 0 y: 0]                      ← Bewegung (blau)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [warte 1 Sekunden]
    [gehe zu zufälliger Position]
```

**Wo finde ich „frage ... und warte"?** → Kategorie **Fühlen** (hellblau), ganz oben in der Liste.

> 💡 **Was passiert hier?** Der Block `frage ... und warte` öffnet ein Eingabefeld auf der Bühne. Was der Spieler tippt, landet automatisch in einer speziellen Variable namens **„Antwort"**. Mit `setze Name auf Antwort` kopierst du diesen Text in deine eigene Variable `Name` – die du dann überall im Spiel verwenden kannst. Das ist ein Beispiel für eine **Zeichenfolge** (Text) in einer Variable, genauso wie du es in Schritt 2 gelernt hast!

Jetzt noch den **Punktezähler** ins Klick-Skript einbauen – füge ganz unten einen neuen Block hinzu:

```
[Wenn diese Figur angeklickt]            ← Ereignisse (gelb)
[spiele Klang "Miau" ab]                 ← Klang (pink)
[sage "Treffer!" für 1 Sekunden]         ← Aussehen (lila)
[ändere Größe um -10]                    ← Aussehen (lila)
[ändere Punkte um 1]                     ← Variablen (orange-rot)  ← NEU
```

**Teste das Spiel:** Klicke die Flagge – wirst du nach deinem Namen gefragt? Sagt die Figur deinen Namen? Steigt der Punktezähler bei jedem Treffer?

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

> 🌟 **Bonusaufgabe:** Dein Spiel hat einen Punktezähler, aber kein Zeitlimit. Das wollen wir ändern!

Erstelle eine zweite Variable mit dem Namen `Zeit`:

- Klicke auf „Erstelle eine Variable" → Name: `Zeit`

Baue ein **neues, viertes Skript** neben deine anderen Skripte:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[setze Zeit auf 15]                      ← Variablen (orange-rot)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [warte 1 Sekunden]                   ← Steuerung (orange)
    [ändere Zeit um -1]                  ← Variablen (orange-rot)
    [falls Zeit < 1]                     ← Steuerung (orange)
        [sage "Zeit abgelaufen!" für 2 Sek.]  ← Aussehen (lila)
        [stoppe alles]                   ← Steuerung (orange)
```

> 💡 **Erklärung:** Die Variable `Zeit` startet bei 15 und zählt jede Sekunde um 1 runter. Wenn sie unter 1 fällt – also 0 erreicht – ist die Zeit abgelaufen und das Spiel stoppt. Du hast **15 Sekunden**, so viele Treffer wie möglich zu landen!

Hake ab:

- [ ] Variable „Zeit" startet bei 15 und zählt runter
- [ ] Das Spiel stoppt, wenn die Zeit 0 erreicht
- [ ] Punkte und Zeit werden beide auf der Bühne angezeigt
- [ ] Ich habe die Startzeit auf `10` geändert – wird das Spiel schwieriger?

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

Im nächsten Schritt lernst du **Bedingungen** kennen – dann kann dein Spiel selbst Entscheidungen treffen: „Wenn die Punkte über 10 sind, mach die Figur schneller!" Speichere dein Klickspiel sorgfältig, denn wir bauen es weiter aus!

---
