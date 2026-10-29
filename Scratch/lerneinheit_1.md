# Einheit 1 - Was ist ein Computer? Erste Schritte in Scratch

**Kategorie:** Einstieg · **Dauer:** 90 Minuten · **Sozialform:** Einzelarbeit · **Vorkenntnisse:** Keine

---

## Lernziel

Du kannst erklären, was ein Algorithmus ist, die Scratch-Oberfläche benennen und eine eigene steuerbare Figur mit Auslöser- und Bewegungsblöcken programmieren.

---

## Materialien

- Computer mit Internetzugang und Scratch-Konto (scratch.mit.edu) – oder Scratch Desktop offline
- Diese Lernkarte (ausgedruckt oder am zweiten Bildschirm geöffnet)
- Stift und Notizzettel (bekommst du bei einem Mentor) für die Algorithmus-Aufgabe in Phase 1

---

## Phase 1 · Einstieg: Was ist ein Algorithmus? *(20 min)*

### Schritt 1 – Schreib-Aufgabe *(12 min)*

Schreib auf, wie du dir morgens die Zähne putzt – so genau, dass ein Roboter es nachmachen könnte, der noch nie Zähne geputzt hat.

Stell dir vor: Der Roboter weiß nicht, was eine Zahnbürste ist, wo der Mund ist oder was „normal" bedeutet!

> 💡 **Tipp:** Gute Algorithmen sind vollständig (kein Schritt fehlt), eindeutig (keine Lücken) und in der richtigen Reihenfolge.

### Schritt 2 – Überprüfe deinen Algorithmus *(8 min)*

Lies deine Anleitung noch einmal durch. Könnte jemand, der noch nie eine Zahnbürste gesehen hat, deinen Algorithmus ausführen und hätte danach saubere Zähne?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige und erkläre einem der Mentoren deinen Algorithmus.

---

## Phase 2 · Scratch kennenlernen *(20 min)*

### Schritt 1 – Scratch öffnen *(2 min)*

Gehe auf **[scratch.mit.edu](https://scratch.mit.edu)** und klicke auf „Entwickeln" am oberen Bildschirmrand.

### Schritt 2 – Erkundungsauftrag *(10 min)*

Klicke dich durch alle Bereiche und finde selbst heraus, wo folgendes ist. Hake ab, was du gefunden hast:

- [ ] Die **Bühne** – der Bereich rechts oben, wo die Figur sichtbar ist.
- [ ] Den **Sprites-Bereich** – der Bereich rechts unten. Alle Figuren werden hier aufgelistet.
- [ ] Die **Blockpalette** – die bunten Blöcke auf der linken Seite
- [ ] Den **Skriptbereich** – die weiße Fläche in der Mitte, hier baust du dein Programm
- [ ] Die Reiter **Kostüme** und **Klänge** – oben links neben dem Reiter „**Skripte**"

### Schritt 3 – Figur wechseln *(8 min)*

Ziel ist es, die aktuelle Figur **Katze** durch eine neue Figur zu ersetzen.

Klicke dafür auf den kleinen Mülleimer rechts oben an der **Katze** im **Sprites-Bereich** (alternativ kannst du auch mit der rechten Maustaste auf die **Katze** klicken und **Löschen** betätigen)

> 💡 **Tipp:** Die Figuren werden in Scratch auch Sprites genannt.

Wähle nun eine neue Figur aus der Bibliothek und gib ihr einen eigenen Namen.

> 💡 **Tipp:** Den Namen änderst du über dem Sprite-Bereich: Klicke deine Figur an, klicke in das Feld **Figur**, lösche den alten Namen, tippe den neuen ein und drücke die Eingabetaste.

> 💡 **Tipp:** Du kannst mit der Schaltfläche mit dem Katzenkopf rechts unten im Sprite-Bereich auf die Figurenbibliothek zugreifen.

> 💡 **Tipp:** Klicke auf jede Kategorie in der Blockpalette (Bewegung, Aussehen, Klang…) und schau, welche Blöcke es gibt. Du brauchst sie gleich!

---

## Phase 3 · Erstes Skript bauen *(35 min)*

### Schritt 1 – Skript nachbauen *(15 min)*

Ziehe diese Blöcke in den Skriptbereich und verbinde sie von oben nach unten:

```text
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[gehe 10 Schritte]                       ← Bewegung (blau)
[sage "Hallo! Ich bin ___!" für 2 Sek.]  ← Aussehen (lila)
[wechsle zum nächsten Kostüm]            ← Aussehen (lila)
[spiele Klang ___]                       ← Klang (pink)
```

Setze beim „sage"-Block bei `___` deinen eigenen Namen ein. Beim „spiele Klang"-Block wählst du im Menü ▼ einen Klang deiner Figur aus.

**Wo sind die Blöcke?**

| Kategorie | Ereignisse | Bewegung | Aussehen | Klang |
| ------ | ------ | ----- | ----- | ----- |
| **Farbe** | Gelb | Blau | Lila | Pink |

**Teste:** Klicke die grüne Flagge. Schau auf die Bühne: Was macht deine Figur nacheinander?

Hake ab:

- [ ] Die Figur geht ein Stück nach rechts
- [ ] Sie sagt deinen Namen
- [ ] Sie wechselt das Kostüm und spielt einen Klang

### Schritt 2 – Experimentieren *(10 min)*

Probiere folgendes aus und hake ab, was du getestet hast:

- [ ] Ändere die Schrittzahl auf `100` – was passiert?
- [ ] Ändere die Schrittzahl auf `-50` – was passiert?
- [ ] Versuche, die Figur durch mehrmaliges Klicken genau an den rechten Rand zu bringen.
- [ ] Ändere die Wartezeit beim „sage"-Block – was ändert sich?

### Schritt 3 – Pfeiltasten-Steuerung *(10 min)*

Erstelle **4 neue, separate Skripte** (nicht mit dem ersten Skript verbinden!):

```text
[Wenn Taste Pfeil rechts gedrückt wird]  ← Ereignisse (gelb)
[gehe 10 Schritte]                       ← Bewegung (blau)

[Wenn Taste Pfeil links gedrückt wird]   ← Ereignisse (gelb)
[gehe -10 Schritte]                      ← Bewegung (blau)

[Wenn Taste Pfeil hoch gedrückt wird]    ← Ereignisse (gelb)
[ändere y um 10]                         ← Bewegung (blau)

[Wenn Taste Pfeil unten gedrückt wird]   ← Ereignisse (gelb)
[ändere y um -10]                        ← Bewegung (blau)
```

> 💡 **Tipp:** Im Block „Wenn Taste … gedrückt wird" steht zuerst **Leertaste**. Klicke auf das kleine Dreieck ▼ und wähle die richtige Taste aus, zum Beispiel den Pfeil nach rechts.

**Teste:** Drücke nacheinander alle vier Pfeiltasten und steuere deine Figur über die ganze Bühne.

Hake ab:

- [ ] Die Figur bewegt sich mit den Pfeiltasten nach rechts, links, oben und unten

> 🌟 **Bonusaufgabe:** Baue ein Skript mit `Wenn Taste Leertaste gedrückt wird`, bei dem deine Figur „Boing!" für 1 Sekunde sagt. Kannst du noch einen eigenen Effekt erfinden?

---

## Phase 4 · Abschluss & Reflexion *(15 min)*

### Schritt 1 – Projekt speichern

Datei → **Auf deinem Computer speichern**

Name: `Einheit 1 – meine erste Figur`

### Schritt 2 – Selbstkontrolle

Beantworte diese Fragen und hake ab, wenn du eine Antwort hast:

- [ ] Was ist ein Algorithmus? (erkläre es mit deinen eigenen Worten)
- [ ] Was passiert, wenn du einen Block aus dem Skript entfernst?
- [ ] Was ist der Unterschied zwischen der Bühne und einem Sprite?

> 🟠 **Mentor-Moment (ca. 5 min)**
>
> Zeige dem Mentor dein fertiges Projekt.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
| --------- | -------- |
| Figur bewegt sich nicht | Ist die Figur im Sprites-Bereich ausgewählt (blauer Rahmen)? Skripte gelten nur für den aktiven Sprite. |
| Block lässt sich nicht einfügen | Lass ihn direkt unter dem vorherigen Block fallen, bis ein weißer Strich erscheint. |
| Figur verschwindet vom Bildschirm | Klicke auf die Figur im Sprites-Bereich und nutze den Block „gehe zu x: 0 y: 0". |
| Nichts funktioniert mehr | Strg+Z macht den letzten Schritt rückgängig. Scratch speichert automatisch in der Cloud, wenn du eingeloggt bist. |

---

## Ausblick auf Einheit 2

In der nächsten Einheit baust du dein erstes richtiges Spiel: Eine Figur springt über die Bühne, und du musst sie anklicken. Dabei lernst du, warum die Reihenfolge der Blöcke so wichtig ist.

---
