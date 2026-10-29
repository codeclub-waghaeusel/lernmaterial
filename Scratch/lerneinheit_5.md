# Einheit 5 - Schleifen: Wiederholungen clever nutzen

**Kategorie:** Schleifen · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 4

---

## Lernziel

Du verstehst, wozu Schleifen gut sind, und kannst in Scratch die passende Schleife für eine Aufgabe auswählen. Am Ende hast du eine Animation programmiert: Eine Figur läuft selbstständig über die Bühne und prallt am Rand ab, während im Hintergrund Sterne blinken.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift für die Aufgaben in Phase 1

---

## Phase 1 · Einstieg: Warum Schleifen? *(20 min)*

### Schritt 1 – Die Tanz-Challenge *(8 min)*

Du willst mit deinen Freunden einen Tanz für ein Kurzvideo einstudieren. Er besteht aus drei Bewegungen, die sich **8-mal** wiederholen:

**klatschen → stampfen → einmal drehen**

Du möchtest den Ablauf für deine Freunde aufschreiben. Schreib ihn einmal komplett auf einen separaten Zettel – jede einzelne Bewegung in eine Zeile.

```text
1. ...
2. ...
3. ...
4. ...
```

Beantworte dann:

| Frage | Deine Antwort |
| ----- | ------------- |
| Wie viele Zeilen hat dein Zettel, wenn du **alle 8 Durchgänge** aufschreibst? | |
| Nach der Probe wollt ihr „stampfen“ durch „hüpfen“ ersetzen. An wie vielen Stellen musst du den Zettel ändern, wenn du alles aufgeschrieben hast? | |

Hast du eine Idee, wie du die Liste auf deinem Zettel kürzer machen könntest? Schreib deine Idee auf. An wie vielen Stellen müsstest du dann „stampfen" durch „hüpfen" ersetzen?

____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

### Schritt 2 – Wiederholungen im Alltag *(7 min)*

Auch im Alltag gibt es Wiederholungen. Es gibt drei Arten, und jede hört anders auf. Verbinde mit einer Linie, was zusammengehört:

| Alltags-Situation | Art der Wiederholung |
| ----------------- | -------------------- |
| Du putzt dir so lange die Zähne, bis die Sanduhr abgelaufen ist | ...wiederhole fortlaufend (hört nie von selbst auf) |
| Dein Lieblingslied läuft in der Playlist auf Dauerschleife | ...wiederhole 10-mal (feste Anzahl) |
| Du machst 10 Liegestütze | ...wiederhole bis ... (hört auf, wenn etwas wahr wird) |

> Tipp: Die rechte Spalte ist bewusst durcheinander. Lies jede Zeile genau!

> 💡 **Merke:** Wenn du dieselben Schritte immer wieder aufschreibst, ist das mühsam, und Fehler schleichen sich leicht ein. Besser ist: Du schreibst die Schritte **einmal** auf und sagst dazu, **wie oft** sie wiederholt werden. Genau das machen **Schleifen** in der Programmierung!

### Schritt 3 – Wie oft läuft die Schleife? *(5 min)*

Ein Rasenmäher-Roboter bekommt diese Anweisung:

> **Wiederhole 4-mal:** Fahre 10 Meter geradeaus. Drehe dich um 90 Grad nach rechts.

Ergänze die Lücken:

Der Roboter fährt insgesamt _____ Meter und dreht sich insgesamt um _____ Grad. Am Ende steht er an der ____________________ Stelle wie am Anfang und schaut in ____________________ Richtung.

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor deine Antworten aus den Schritten 1 bis 3.

---

## Phase 2 · Die drei Schleifen in Scratch testen *(20 min)*

### Schritt 1 – Neues Projekt öffnen *(2 min)*

Öffne ein **neues Scratch-Projekt**. Behalte die Katze (oder wähle eine andere Figur, die du laufen lassen willst).

### Schritt 2 – Wiederhole N-mal *(6 min)*

Baue dieses Skript und teste es:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[wiederhole 4 mal]                       ← Steuerung (orange)
    [gehe 50 Schritte]                   ← Bewegung (blau)
    [warte 0.5 Sekunden]                 ← Steuerung (orange)
    [drehe dich um 90 Grad nach rechts]  ← Bewegung (blau)
    [warte 0.5 Sekunden]                 ← Steuerung (orange)
```

Hake ab, was du beobachtet hast:

- [ ] Die Figur läuft ein Quadrat
- [ ] Nach der Schleife steht sie wieder am Startpunkt
- [ ] Wenn ich `4` auf `8` ändere, läuft sie das Quadrat zweimal

### Schritt 3 – Wiederhole bis *(6 min)*

Lösche das Skript der Katze und baue dieses neue:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[gehe zu x: -200 y: 0]                   ← Bewegung (blau)
[wiederhole bis <(x-Position) > 200>]    ← Steuerung (orange) / Operatoren (grün) / Bewegung (blau)
    [gehe 10 Schritte]                   ← Bewegung (blau)
[sage "Angekommen!" für 2 Sekunden]      ← Aussehen (lila)
```

**Wo finde ich die Blöcke?**

- „wiederhole bis" → Kategorie **Steuerung** (orange)
- `x-Position` → Kategorie **Bewegung** (blau), ganz unten
- `>` → Kategorie **Operatoren** (grün)

> 💡 **Tipp:** Ziehe zuerst den grünen Block `>` in das Feld von „wiederhole bis". Dann ziehst du den runden Block `x-Position` in sein **linkes** Feld (nicht eintippen!) und tippst `200` in das rechte.

Hake ab:

- [ ] Die Figur läuft von links nach rechts über die Bühne
- [ ] Erst **nach** der Schleife sagt sie „Angekommen!"
- [ ] Ich habe `200` auf `100` geändert - was kann ich beobachten?

### Schritt 4 – Wiederhole fortlaufend *(6 min)*

Jetzt eine Schleife, die nie aufhört. Lösche das Skript wieder und baue:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [gehe 5 Schritte]                    ← Bewegung (blau)
    [falls am Rand abprallen]            ← Bewegung (blau)
```

Klicke die Flagge und beobachte. Klicke dann auf das rote Stopp-Zeichen.

> 💡 **Merke:** Die drei Schleifen im Vergleich:
>
> - **wiederhole N-mal** → du weißt vorher, **wie oft**
> - **wiederhole bis** → du weißt, **wann es aufhören soll**, aber nicht, wie oft
> - **wiederhole fortlaufend** → läuft, **bis du das Programm stoppst** (Endlosschleife)

Hake ab:

- [ ] Die Figur läuft hin und her und bleibt nie stehen
- [ ] Die Figur steht am Rand auf dem Kopf – das beheben wir gleich in Phase 3!

---

## Phase 3 · Animierter Hintergrund und laufende Figur *(35 min)*

### Schritt 1 – Hintergrund und Figur vorbereiten *(6 min)*

Öffne ein **neues Scratch-Projekt**.

1. Wähle einen **Hintergrund**, auf dem Sterne gut aussehen, zum Beispiel „Stars" oder „Space".
2. Wähle eine **Figur**, die über die Bühne laufen soll (zum Beispiel ein Tier, eine Person oder ein Raumschiff). Sie braucht mindestens **zwei Kostüme** – schau im Reiter *Kostüme* nach.
3. Wähle als zweite Figur einen **Stern** (oder male selbst einen kleinen Stern).

Hake ab:

- [ ] Hintergrund ist gewählt
- [ ] Die laufende Figur hat mindestens zwei Kostüme
- [ ] Die Stern-Figur steht auf der Bühne

### Schritt 2 – Die Figur läuft und prallt ab *(8 min)*

Klicke die **laufende Figur** an und baue:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[setze Drehtyp auf links-rechts]         ← Bewegung (blau)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [gehe 5 Schritte]                    ← Bewegung (blau)
    [falls am Rand abprallen]            ← Bewegung (blau)
```

> 💡 **Tipp:** Der Block „setze Drehtyp auf links-rechts" sorgt dafür, dass die Figur beim Abprallen nicht kopfüber läuft, sondern nur nach links oder rechts schaut. Du findest ihn in **Bewegung** (blau), ganz unten.

**Teste:** Klicke die grüne Flagge. Läuft die Figur hin und her und schaut sie in die Richtung, in die sie läuft?

Jetzt soll die Figur beim Laufen auch so aussehen, als würde sie laufen. Ergänze im Flaggen-Skript der **laufenden Figur** **in der Schleife**, ganz unten, zwei Blöcke:

> 💡 **So liest du die Skripte ab jetzt:** Zeilen mit **+** sind neu, die baust du ein. Zeilen mit **-** nimmst du heraus. **⋮** steht für Blöcke, die bleiben, wie sie sind. Alle anderen Zeilen hast du schon.

```diff
  [Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
  [setze Drehtyp auf links-rechts]         ← Bewegung (blau)
  [wiederhole fortlaufend]                 ← Steuerung (orange)
      [gehe 5 Schritte]                    ← Bewegung (blau)
      [falls am Rand abprallen]            ← Bewegung (blau)
+     [wechsle zum nächsten Kostüm]        ← Aussehen (lila)
+     [warte 0.1 Sekunden]                 ← Steuerung (orange)
```

**Teste:** Klicke die grüne Flagge und schau genau auf die Beine oder Flügel deiner Figur.

Hake ab:

- [ ] Die Figur läuft über die Bühne und prallt am Rand ab
- [ ] Sie wechselt beim Laufen ihr Kostüm und sieht lebendig aus
- [ ] Die Figur läuft nie kopfüber

### Schritt 3 – Der Stern blinkt *(7 min)*

Klicke jetzt die **Stern-Figur** an. Sie soll fünfmal blinken, indem sie sich abwechselnd versteckt und zeigt:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[wiederhole 5 mal]                       ← Steuerung (orange)
    [verstecke dich]                     ← Aussehen (lila)
    [warte 0.3 Sekunden]                 ← Steuerung (orange)
    [zeige dich]                         ← Aussehen (lila)
    [warte 0.3 Sekunden]                 ← Steuerung (orange)
```

**Teste:** Klicke die grüne Flagge und zähle mit. Blinkt der Stern genau fünfmal und bleibt dann sichtbar?

> 💡 **Tipp:** Willst du, dass der Stern langsamer oder schneller blinkt? Ändere die Zeit bei „warte". Willst du mehr oder weniger Blinkvorgänge? Ändere die Zahl bei „wiederhole". Du musst nur **eine** Stelle ändern – genau das ist der Vorteil der Schleife!

Hake ab:

- [ ] Der Stern blinkt fünfmal
- [ ] Er ist am Ende sichtbar (nicht versteckt!)
- [ ] Ich habe die Blinkgeschwindigkeit einmal geändert

### Schritt 4 – Einen Sternenhimmel durch Duplizieren *(7 min)*

Ein einzelner Stern macht noch keinen Sternenhimmel. Dein Stern kann sich aber **kopieren lassen** – samt Skript!

1. Klicke im Figurenbereich (unten rechts) mit der **rechten Maustaste** auf deine Stern-Figur und wähle **duplizieren**.
2. Wiederhole das, bis du **mindestens fünf Sterne** hast.
3. Ziehe die Sterne mit der Maus an verschiedene Stellen der Bühne.
4. Gib einigen Sternen eine andere Größe (Feld *Größe* unter der Bühne).

**Teste:** Klicke auf die grüne Flagge. Blinken alle Sterne?

> 💡 **Tipp:** Beim Duplizieren wird das Skript mitkopiert. Darum blinken alle Sterne gleichzeitig. Wenn du bei **einem** Stern die Wartezeit änderst, blinkt nur dieser Stern anders – die Kopien sind unabhängig voneinander.

Hake ab:

- [ ] Auf der Bühne stehen mindestens fünf Sterne in verschiedenen Größen
- [ ] Alle Sterne blinken fünfmal und sind danach sichtbar
- [ ] Ich habe bei einem Stern die Wartezeit geändert und gesehen, dass nur dieser anders blinkt

### Schritt 5 – Blinken bis zum Stopp: „wiederhole bis" *(7 min)*

Jetzt kommt „wiederhole bis" zum Einsatz: Die Sterne sollen blinken, sobald du die **Taste S** drückst, und erst aufhören, wenn du die **Leertaste** drückst. Baue für **einen** Stern ein **neues Skript** (das Flaggen-Skript bleibt unverändert):

```text
[Wenn Taste S gedrückt wird]             ← Ereignisse (gelb)
[wiederhole bis <Taste Leertaste gedrückt?>]  ← Steuerung (orange) / Fühlen (hellblau)
    [verstecke dich]                     ← Aussehen (lila)
    [warte 0.3 Sekunden]                 ← Steuerung (orange)
    [zeige dich]                         ← Aussehen (lila)
    [warte 0.3 Sekunden]                 ← Steuerung (orange)
[zeige dich]                             ← Aussehen (lila)
```

Die anderen Sterne haben dieses Skript noch nicht. **Ziehe das Skript** mit der Maus auf die Bilder der anderen Sterne im Figurenbereich – dort wird es hineinkopiert.

> 💡 **Tipp:** Drücke S erst, wenn die Flaggen-Skripte durchgelaufen sind. Sonst arbeiten zwei Skripte gleichzeitig am selben Stern.

**Teste:** Klicke die grüne Flagge und warte, bis alle Sterne fertig geblinkt haben. Drücke dann S und nach ein paar Sekunden die Leertaste. Was machen die Sterne?

Hake ab:

- [ ] Alle Sterne blinken nach Druck auf S und hören auf, sobald ich die Leertaste drücke
- [ ] Ich kann erklären, warum hier „wiederhole bis" besser passt als „wiederhole 5-mal"

> 🌟 **Bonusaufgabe:** Lass die laufende Figur schneller werden: Erstelle eine Variable `Tempo` (Startwert 3) und benutze `gehe (Tempo) Schritte`. Baue in die Schleife `ändere Tempo um 0.1`. Wie verändert sich das Laufen nach einer Minute? Mit einer Bedingung aus Einheit 4 kannst du das Tempo bei `Tempo > 10` wieder auf 3 zurücksetzen!

---

## Phase 4 · Abschluss & Reflexion *(15 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 5 – meine Animation`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Welche drei Arten von Schleifen gibt es, und woran erkennst du, welche du brauchst?
- [ ] Was ist eine Endlosschleife? Wann ist sie sinnvoll, wann ein Fehler?
- [ ] Was würde passieren, wenn du `wechsle zum nächsten Kostüm` **vor** die Schleife statt hinein schreibst?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor deine fertige Animation und zeige, wo du welche Art von Schleife benutzt hast.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| ------- | ------ |
| Die Figur läuft kopfüber, wenn sie abprallt | Setze am Anfang **setze Drehtyp auf links-rechts** (Bewegung, blau). |
| Die Figur läuft, aber nur ein Mal und dann nicht mehr | Prüfe, ob alle Blöcke **innerhalb** der Schleife stecken. Sie müssen eingerückt im „C" der Schleife liegen. |
| Die Figur bewegt sich so schnell, dass man sie kaum sieht | Füge in die Schleife **warte 0.1 Sekunden** ein oder verringere die Schrittzahl. |
| Die Schleife hört nicht mehr auf | „wiederhole bis" endet nur, wenn die Bedingung wahr wird. Prüfe, ob sie überhaupt wahr werden kann (zum Beispiel ob die Figur wirklich die Position `x > 200` erreicht). Mit dem roten Stopp-Zeichen kannst du jederzeit abbrechen. |
| Der Stern ist nach dem Blinken verschwunden | Die Schleife endet mit „verstecke dich"? Füge **nach** der Schleife ein „zeige dich" hinzu. |
| Nur ein Stern blinkt nach Druck auf S | Das S-Skript gibt es nur bei der Figur, bei der du es gebaut hast. Ziehe es auf die Bilder der anderen Sterne im Figurenbereich, um es zu kopieren. |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 6

Im nächsten Schritt kombinierst du **Schleifen und Bedingungen**: Du baust ein Fang-Spiel, in dem Objekte vom Himmel fallen und du sie mit einer Figur auffängst. Dafür brauchst du alles, was du bisher gelernt hast – Variablen, Bedingungen und jetzt auch Schleifen!

---
