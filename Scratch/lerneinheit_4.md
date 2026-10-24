# Einheit 4 - Bedingungen: Wenn das passiert, dann

**Kategorie:** Grundkonzepte · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 3

---

## Lernziel

Du verstehst, was eine Bedingung ist, und kannst in Scratch selbst entscheiden lassen, was passiert – je nachdem, ob etwas wahr oder falsch ist. Am Ende hast du ein Quiz-Spiel programmiert, das Antworten prüft und Punkte vergibt.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift für die Aufgaben in Phase 1

---

## Phase 1 · Einstieg: Was ist eine Bedingung? *(20 min)*

### Schritt 1 – Wahr oder falsch? *(10 min)*

Ein Computer kann auf eine Frage immer nur zwei Antworten geben: **wahr** oder **falsch** – nie etwas dazwischen. Das ist der Kern jeder Bedingung.

**Stell dir vor, ein Spieler hat gerade 7 Punkte. Ist die Aussage wahr ✓ oder falsch ✗?**

| Aussage | wahr ✓ oder falsch ✗? |
| --------- | :--------------------: |
| Punkte > 5 | |
| Punkte = 10 | |
| Punkte < 3 | |
| Punkte > 0 | |
| Punkte = 7 | |
| Punkte < 7 | |

> 💡 **Merke:** Die Zeichen `>` (größer als), `<` (kleiner als) und `=` (gleich) heißen **Vergleichsoperatoren**. Sie vergleichen zwei Werte und liefern immer entweder *wahr* oder *falsch* – wie eine Ja-oder-Nein-Frage für den Computer.

### Schritt 2 – Wenn-dann im Alltag *(5 min)*

In deinem Alltag triffst du ständig Entscheidungen mit Bedingungen. Verbinde mit einer Linie, was zusammengehört:

| Bedingung (Wenn ...) | Ergebnis (dann ...) |
| --------------------- | --------------------- |
| Wenn dein Handy-Akku unter 10% ist | ...dann kommt das nächste Level |
| Wenn du im Spiel 10 Punkte erreichst | ...dann lade es auf |
| Wenn es regnet | ...dann darfst du rein |
| Wenn du das richtige Passwort eingibst | ...dann nimm einen Regenschirm mit |

### Schritt 3 – Was ist mit „sonst"? *(5 min)*

Was passiert, wenn die Bedingung *falsch* ist? Dafür gibt es das Wort **„sonst"**. Ergänze die Sätze:

Wenn es regnet, nehme ich einen Regenschirm mit. **Sonst** _______________________________________________

Wenn ich die Frage richtig beantworte, bekomme ich einen Punkt. **Sonst** _______________________________________________

> 💡 **Wenn-dann-sonst** bedeutet: Du hast immer zwei Möglichkeiten – eine für den Fall, dass die Bedingung *wahr* ist, und eine für den Fall, dass sie *falsch* ist.

> 🟠 **Mentor-Moment (ca. 5 min)**
> Zeige dem Mentor deine Antworten aus Schritt 1 und 2. Der Mentor fragt:
>
> - „Schau auf Schritt 1: Was ändert sich, wenn der Spieler statt 7 Punkten plötzlich 3 Punkte hat?"
> - „Erfinde eine eigene Wenn-dann-sonst-Regel für dein Lieblingsspiel!"
> - „Was würde passieren, wenn ein Computer keine wahr/falsch-Entscheidungen treffen könnte?"

---

## Phase 2 · Bedingungen in Scratch testen *(20 min)*

### Schritt 1 – Neues Projekt öffnen *(2 min)*

Öffne ein **neues Scratch-Projekt** auf scratch.mit.edu. Wähle eine Figur, die die Quiz-Fragen stellen soll – zum Beispiel eine Person, ein Tier oder eine sprechende Glühbirne.

### Schritt 2 – Erste Bedingung: nur „wenn-dann" *(10 min)*

Baue dieses Skript und teste es:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[frage "Wie viel ist 5 + 3?" und warte]  ← Fühlen (hellblau)
[falls <Antwort = "8"> dann]             ← Steuerung (orange)
    [sage "Richtig!" für 2 Sekunden]     ← Aussehen (lila)
```

**Wo finde ich die Blöcke?**

- „falls ... dann" → Kategorie **Steuerung** (orange)
- Den Vergleich `Antwort = "8"` baust du so: Nimm den `=`-Block aus **Operatoren** (grün), ziehe das Oval „Antwort" aus **Fühlen** (hellblau) in die linke Lücke und tippe `8` in die rechte Lücke.

Hake ab, was du beobachtet hast:

- [ ] Wenn ich „8" eingebe → Figur sagt „Richtig!"
- [ ] Wenn ich „5" eingebe → Figur sagt gar nichts
- [ ] Wenn ich „8 " (mit Leerzeichen dahinter) eingebe – was passiert?

### Schritt 3 – Besser: „wenn-dann-sonst" *(8 min)*

Der Block „falls ... dann" alleine reagiert nicht, wenn die Bedingung falsch ist. Baue jetzt die vollständige Version – **verändere** dein Skript entsprechend:

```
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[frage "Wie viel ist 5 + 3?" und warte]  ← Fühlen (hellblau)
[falls <Antwort = "8"> dann]             ← Steuerung (orange)
    [sage "Richtig!" für 2 Sekunden]     ← Aussehen (lila)
[sonst]
    [sage "Leider falsch – es ist 8." für 2 Sek.]  ← Aussehen (lila)
```

> 💡 **Tipp:** Den „falls-dann-sonst"-Block findest du in der Kategorie **Steuerung** (orange). Er sieht dem normalen „falls-dann"-Block ähnlich, hat aber eine zweite Öffnung für den „sonst"-Fall. Scrolle in der Steuerungskategorie nach unten, wenn du ihn nicht gleich siehst.

**Teste:** Gib sowohl eine richtige als auch eine falsche Antwort ein – reagiert die Figur unterschiedlich?

---

## Phase 3 · Das Quiz-Spiel bauen *(45 min)*

### Schritt 1 – Punktezähler und erste Frage *(10 min)*

Erstelle eine Variable `Punkte` (wie in Einheit 3 gelernt). Baue das vollständige Skript mit der ersten echten Quiz-Frage:

```
[Wenn grüne Flagge angeklickt]            ← Ereignisse (gelb)
[setze Punkte auf 0]                      ← Variablen (orange-rot)
[frage "Was ist die Hauptstadt von Deutschland?" und warte]  ← Fühlen (hellblau)
[falls <Antwort = "Berlin"> dann]         ← Steuerung (orange)
    [sage "Richtig! +1 Punkt" für 2 Sek.] ← Aussehen (lila)
    [ändere Punkte um 1]                  ← Variablen (orange-rot)
[sonst]
    [sage "Leider falsch – es ist Berlin." für 2 Sek.]  ← Aussehen (lila)
```

Hake ab:

- [ ] Punkte starten bei 0
- [ ] Bei richtiger Antwort steigen die Punkte um 1
- [ ] Bei falscher Antwort erscheint ein Hinweis mit der richtigen Lösung

### Schritt 2 – Zwei weitere Fragen *(15 min)*

Füge **direkt darunter** im selben Skript zwei weitere Fragen hinzu. Du kannst eigene Fragen erfinden!

```
[frage "Wie viel ist 7 × 8?" und warte]  ← Fühlen (hellblau)
[falls <Antwort = "56"> dann]
    [sage "Richtig! +1 Punkt" für 2 Sek.]
    [ändere Punkte um 1]
[sonst]
    [sage "Leider falsch – es ist 56." für 2 Sek.]

[frage "Wie heißt der Planet zwischen Venus und Mars?" und warte]
[falls <Antwort = "Erde"> dann]
    [sage "Richtig! +1 Punkt" für 2 Sek.]
    [ändere Punkte um 1]
[sonst]
    [sage "Leider falsch – es ist die Erde." für 2 Sek.]
```

> 💡 **Eigene Fragen einbauen:** Du kannst die Themen frei wählen – Sport, Tiere, Filme, Geografie... Schreib dir die Antwort genau auf, damit du weißt, wie du sie in Scratch eintippen musst.

Hake ab:

- [ ] Alle drei Fragen werden nacheinander gestellt
- [ ] Richtige Antworten geben je 1 Punkt
- [ ] Falsche Antworten zeigen den richtigen Hinweis

### Schritt 3 – Abschlussnachricht einbauen *(10 min)*

Füge ganz am Ende des Skripts, nach allen drei Fragen, die Auswertung hinzu:

```
[falls <Punkte = 3> dann]                ← Steuerung (orange)
    [sage "Perfekt! 3 von 3 – du bist ein Quiz-Champion!" für 3 Sek.]  ← Aussehen (lila)
[sonst]
    [sage "Nicht alle richtig – versuch es nochmal!" für 3 Sek.]  ← Aussehen (lila)
```

**Teste dein Quiz:** Klicke die Flagge und beantworte alle drei Fragen. Erscheint am Ende die richtige Nachricht?

### Schritt 4 – Verschachtelte Bedingungen: mehrere Stufen *(10 min)*

Stell dir vor, Deine Eltern wollen entscheiden, ob du nach der Schule draußen spielen darfst. Das klappt nicht mit einer einzigen Frage – du brauchst mehrere:

**Überlege, was in jeder Situation passiert – fülle die leeren Felder aus:**

| Bedingung 1 | Bedingung 2 | Was passiert? |
| ------------- | ------------- | --------------- |
| Hausaufgaben fertig? → **Nein** | – | „Erst Hausaufgaben machen!" |
| Hausaufgaben fertig? → **Ja** | Regnet es? → **Ja** | ☐ |
| Hausaufgaben fertig? → **Ja** | Regnet es? → **Nein** | ☐ |

Das nennt man eine **verschachtelte Bedingung**.

> 💡 **Merke:** **Eine** verschachtelte Bedingung ist eine Bedingung, die innerhalb einer anderen Bedingung steckt – wie eine kleine Box in einer großen Box. Der Computer prüft immer zuerst die äußere Bedingung: Ist sie **wahr**, landet er im „dann"-Bereich. Ist sie **falsch**, landet er im „sonst"-Bereich. In *beiden* Bereichen kann eine weitere Bedingung stecken! So kannst du mehrere Fragen nacheinander stellen und für jede Kombination eine eigene Antwort festlegen.

**Wende das jetzt auf dein Quiz an!** Ersetze die Abschlussnachricht aus Schritt 3 durch diese verschachtelte Version – damit gibt es jetzt vier verschiedene Auswertungen:

```
[falls <Punkte = 3> dann]
    [sage "Perfekt! Alle 3 richtig – du bist Quiz-Champion!" für 3 Sek.]
[sonst]
    [falls <Punkte > 1> dann]
        [sage "Sehr gut! 2 von 3 richtig." für 3 Sek.]
    [sonst]
        [falls <Punkte > 0> dann]
            [sage "Nicht schlecht! 1 von 3 richtig." für 3 Sek.]
        [sonst]
            [sage "Kein Punkt – probier es nochmal!" für 3 Sek.]
```

> 💡 **Tipp:** Den inneren „falls-dann-sonst"-Block ziehst du direkt in den „sonst"-Bereich des äußeren Blocks. Scratch zeigt das durch Einrückung – so siehst du auf einen Blick, welcher Block zu welcher Ebene gehört.

Hake ab:

- [ ] Ich habe den alten Abschlussblock entfernt und durch die verschachtelte Version ersetzt
- [ ] Bei 3 Punkten erscheint „Perfekt! Alle 3 richtig"
- [ ] Bei 2 Punkten erscheint „Sehr gut!"
- [ ] Bei 1 Punkt erscheint „Nicht schlecht!"
- [ ] Bei 0 Punkten erscheint „Kein Punkt – probier es nochmal!"

> 🌟 **Bonusaufgabe:** Füge eine vierte eigene Frage hinzu – jetzt sind 4 Punkte möglich! Passe die verschachtelten Bedingungen an: Der erste Block prüft `Punkte = 4`, der zweite `Punkte > 2`, der dritte `Punkte > 1` und der vierte `Punkte > 0`.

---

## Phase 4 · Abschluss & Reflexion *(15 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 4 – mein Quiz-Spiel`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Was bedeutet „wahr" und „falsch" bei einer Bedingung? (Erkläre es mit einem Beispiel!)
- [ ] Was ist der Unterschied zwischen „falls-dann" und „falls-dann-sonst"?
- [ ] Was würde passieren, wenn du `setze Punkte auf 0` nach den Fragen statt davor schreibst?

> 🟠 **Mentor-Moment (ca. 5 min)**
> Zeige dem Mentor dein fertiges Quiz-Spiel. Der Mentor spielt es einmal durch und fragt dann:
>
> - „Erkläre mir, was eine Bedingung ist – mit einem Beispiel aus dem Alltag!"
> - „Was passiert, wenn jemand ‚berlin' (klein geschrieben) eingibt statt ‚Berlin'? Teste es!"
> - „Wie könntest du das Quiz fairer machen – zum Beispiel für Antworten mit Groß/Kleinschreibung?"

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| --------- | -------- |
| Figur reagiert nicht auf die richtige Antwort | Leerzeichen in der Antwort zählen! „Berlin " (mit Leerzeichen) ist für Scratch nicht gleich „Berlin". Prüfe auch, ob du den richtigen Vergleichsblock verwendet hast. |
| Den „falls-dann-sonst"-Block finde ich nicht | Er ist in **Steuerung** (orange) – scrolle nach unten. Er sieht dem normalen „falls-dann"-Block ähnlich, hat aber eine zweite Öffnung. |
| Punkte zählen nicht hoch | Prüfe, ob „ändere Punkte um 1" *innerhalb* des „dann"-Bereichs steckt – er muss eingerückt unter dem „falls"-Block stehen, nicht dahinter. |
| Das Spiel fragt nur die erste Frage | Die Fragen müssen alle nacheinander im *selben* Skript stehen – nicht als separate Skripte. |
| Abschlussnachricht erscheint nicht | Steht der letzte „falls"-Block auch innerhalb desselben Skripts, nach den drei Fragen? |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 5

Im nächsten Schritt lernst du **Schleifen** kennen – dann musst du nicht mehr jede Quiz-Frage einzeln aufschreiben! Eine Schleife kann Code immer wieder ausführen, was dein Programm kürzer und mächtiger macht. Speichere dein Quiz sorgfältig!

---
