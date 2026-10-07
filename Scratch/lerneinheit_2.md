# Einheit 2 - Reihenfolge & Auslöser: Mein erstes Spiel

**Kategorie:** Einstieg · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Einheit 1

---

## Lernziel

Du verstehst, dass die Reihenfolge von Blöcken in Scratch wichtig ist, und weißt, wie du auf verschiedene Auslöser (z. B. Klick oder Taste) reagieren kannst. Am Ende hast du ein erstes kleines Klickspiel programmiert.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift für die Aufgaben in Phase 1
- Gespeichertes Projekt aus Einheit 1 (optional als Ausgangspunkt)

---

## Phase 1 · Einstieg: Reihenfolge ist alles! *(20 min)*

### Schritt 1 – Das Chaos-Experiment *(10 min)*

Stell dir vor, du erklärst deiner kleinen Schwester, wie sie morgens Cornflakes frühstückt.
Du schreibst ihr jeden Schritt auf einen eigenen Zettel.

**Hier sind die Schritte – aber sie sind durcheinander geraten! Schreibe die Nummern 1–5 in die Kästchen, um die richtige Reihenfolge herzustellen:**

| Reihenfolge | Schritt |
| ----------- | --------- |
| ☐ | Löffel nehmen und essen |
| ☐ | Schüssel auf den Tisch stellen |
| ☐ | Cornflakes in die Schüssel schütten |
| ☐ | Milch über die Cornflakes gießen |
| ☐ | Kühlschrank öffnen und Milch rausholen |

> 💡 **Wichtig:** Wenn die Reihenfolge falsch ist, geht etwas schief! Was passiert zum Beispiel, wenn du zuerst die Milch eingießt, bevor du die Schüssel holst?
>
> Schreib es hier auf: _______________________________________________

### Schritt 2 – Reihenfolge in Scratch *(5 min)*

In Scratch ist es genauso! Die Blöcke werden **immer von oben nach unten** ausgeführt – Schritt für Schritt, in der Reihenfolge, in der sie gestapelt sind.

Schau dir diese zwei Skripte an. Was ist der Unterschied?

```text
Skript A:                          Skript B:
─────────────────────────          ─────────────────────────
[Wenn Flagge angeklickt]           [Wenn Flagge angeklickt]
[sage "Ich starte!" 2 Sek.]        [gehe 100 Schritte]
[gehe 100 Schritte]                [sage "Ich starte!" 2 Sek.]
```

Was macht die Figur zuerst in **Skript A**? _______________________________________________

Was macht die Figur zuerst in **Skript B**? _______________________________________________

### Schritt 3 – Auslöser: Wann passiert was? *(5 min)*

In Scratch gibt es auch **Auslöser** – das sind Blöcke ganz oben in einem Skript, die sagen: *„Starte erst, wenn das passiert!"*

Verbinde mit einer Linie, welcher Auslöser zu welchem Beispiel aus dem Alltag passt:

| Auslöser in Scratch | Beispiel aus dem Alltag |
| --------------------- | ------------------------- |
| Wenn **grüne Flagge** angeklickt | Du drückst „A" auf dem Controller – dein Charakter springt |
| Wenn **diese Figur** angeklickt | Du drückst „Play" bei YouTube – das Video startet |
| Wenn **Taste gedrückt** | Du tippst auf eine App auf dem Handy – sie öffnet sich |

> 💡 **Merke:** Ein Auslöser ist wie ein Startschuss. Nichts passiert, bevor der Startschuss fällt!

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige und erkläre dem Mentor deine Antworten aus Schritt 1–3.

---

## Phase 2 · Zufällige Bewegung & Klick-Reaktion *(20 min)*

### Schritt 1 – Projekt öffnen *(2 min)*

Öffne dein gespeichertes Projekt aus Einheit 1 oder erstelle ein neues Projekt auf **scratch.mit.edu**.
Wähle eine Figur aus, die sich gut anklicken lässt – zum Beispiel ein Tier, ein Ball oder eine bunte Form.

### Schritt 2 – Figur springt zufällig umher *(10 min)*

Baue dieses Skript. Die Figur springt nach dem Start der grünen Flagge immer wieder an eine zufällige Stelle:

```text
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [warte 1 Sekunden]                   ← Steuerung (orange)
    [gehe zu zufälliger Position]        ← Bewegung (blau)
```

**Wo finde ich die Blöcke?**

- „gehe zu zufälliger Position" → Kategorie **Bewegung** (blau)
- „wiederhole fortlaufend" → Kategorie **Steuerung** (orange)
- „warte 1 Sekunden" → Kategorie **Steuerung** (orange)

Hake ab, was du ausprobiert hast:

- [ ] Figur springt bei Flagge an eine zufällige Position
- [ ] Wartezeit auf `0.5` Sekunden geändert – was passiert?
- [ ] Wartezeit auf `3` Sekunden geändert – was passiert?

### Schritt 3 – Figur reagiert auf Klick *(8 min)*

Füge ein **zweites, separates Skript** hinzu – leg es einfach neben das erste in den Skriptbereich, **nicht dranhängen!**

```text
[Wenn diese Figur angeklickt]            ← Ereignisse (gelb)
[spiele Klang "Miau" ab]                 ← Klang (pink)
[sage "Erwischt!" für 1 Sekunden]        ← Aussehen (lila)
```

**Teste dein Programm:** Klicke die grüne Flagge – springt die Figur umher? Kannst du sie anklicken und „Erwischt!" lesen?

> 💡 **Cool, oder?** Du hast jetzt zwei Skripte gleichzeitig aktiv. Das erste reagiert auf die Flagge, das zweite auf den Klick auf die Figur. Beide laufen gleichzeitig – das ist der Trick!

---

## Phase 3 · Das Klickspiel bauen *(35 min)*

### Schritt 1 – Figur wird beim Treffer kleiner *(10 min)*

Jetzt bauen wir das echte Spiel! Passe das Klick-Skript so an:

```text
[Wenn diese Figur angeklickt]            ← Ereignisse (gelb)
[spiele Klang "Miau" ab]                 ← Klang (pink)
[sage "Treffer! +1 Punkt" für 1 Sekunden] ← Aussehen (lila)
[ändere Größe um -10]                    ← Aussehen (lila)
```

> 💡 **Tipp:** Den Block „ändere Größe um" findest du unter **Aussehen**. Die Zahl `-10` bedeutet: die Figur wird kleiner. Probiere `-20` – was passiert dann?

Hake ab, was du getestet hast:

- [ ] Figur wird kleiner, wenn ich sie anklicke
- [ ] Figur springt weiterhin zufällig umher
- [ ] „Treffer!"-Nachricht erscheint bei jedem Klick

### Schritt 2 – Spiel sauber starten *(15 min)*

Wenn du die Flagge mehrmals klickst, wird die Figur immer kleiner. Das wollen wir verhindern! Ergänze das Flagge-Skript oben mit zwei Reset-Blöcken:

```text
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[setze Größe auf 100 %]                  ← Aussehen (lila)    ← NEU
[gehe zu x: 0 y: 0]                      ← Bewegung (blau)    ← NEU
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [warte 1 Sekunden]                   ← Steuerung (orange)
    [gehe zu zufälliger Position]        ← Bewegung (blau)
```

> 💡 **Warum steht das vor der Schleife?** Die Blöcke *vor* „wiederhole fortlaufend" werden nur **einmal** ausgeführt – gleich beim Start. Die Blöcke *innerhalb* der Schleife laufen immer und immer wieder. Die Reihenfolge der Blöcke macht also auch hier den Unterschied!

**Teste das Spiel:** Klicke die Flagge mehrmals hintereinander. Startet die Figur jedes Mal wieder in normaler Größe?

### Schritt 3 – Spielende einbauen *(10 min)*

Wenn die Figur zu klein wird, soll das Spiel aufhören. Baue ein drittes Skript neben die anderen beiden:

```test
[Wenn grüne Flagge angeklickt]           ← Ereignisse (gelb)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [falls Größe < 30]                   ← Steuerung (orange)
        [sage "Game Over!" für 2 Sek.]   ← Aussehen (lila)
        [stoppe alles]                   ← Steuerung (orange)
```

> 💡 **Tipp:** Den Block „falls ... dann" und „stoppe alles" findest du unter **Steuerung** (orange).
>
> 🌟 **Bonusaufgabe:** Füge einen Hintergrund hinzu! Klicke auf die **Bühne** (nicht auf die Figur!) im Sprites-Bereich unten rechts. Dann findest du unter „Hintergründe" verschiedene Bilder. Wähle einen passenden Hintergrund für dein Spiel aus.

---

## Phase 4 · Abschluss & Reflexion *(10 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 2 – mein erstes Klickspiel`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Warum ist die Reihenfolge der Blöcke in Scratch wichtig? (Denk an das Cornflakes-Beispiel!)
- [ ] Warum brauchst du in deinem Spiel zwei separate Skripte und nicht nur eines?
- [ ] Was passiert, wenn du „setze Größe auf 100 %" aus dem Flagge-Skript löschst und dann mehrmals auf die Flagge klickst?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige und erkläre dem Mentor dein fertiges Spiel.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| --------- | -------- |
| Figur springt nicht zufällig | Ist der Block „wiederhole fortlaufend" vorhanden? Ohne ihn läuft „gehe zu zufälliger Position" nur einmal. |
| Klick auf Figur reagiert nicht | Schau unten rechts: Ist die Figur im Sprites-Bereich mit einem blauen Rahmen markiert? Das Klick-Skript gilt nur für die ausgewählte Figur. |
| Figur wird nicht kleiner | Prüfe, ob „ändere Größe um -10" im **Klick-Skript** steckt – nicht im Flagge-Skript. |
| Spiel stoppt sofort beim Start | Die Figur startet vielleicht schon kleiner als 30 %. Füge „setze Größe auf 100 %" ganz oben im Flagge-Skript ein. |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 3

Im nächsten Schritt lernst du **Variablen** kennen – dann können wir Punkte wirklich zählen und auf der Bühne anzeigen, statt nur „Treffer!" zu sagen. Speichere dein Klickspiel sorgfältig, denn wir bauen es weiter aus!

---
