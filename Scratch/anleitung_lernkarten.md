# So liest du deine Lernkarten

Jede Lernkarte führt dich Schritt für Schritt durch eine Einheit. Hier erfährst du, was die Zeichen und Abschnitte bedeuten. Lies diese Seite einmal in Ruhe durch, dann kennst du dich auf jeder Karte aus.

---

## Wie eine Lernkarte aufgebaut ist

Jede Einheit hat vier Phasen:

| Phase | Was du machst |
| ----- | ------------- |
| **Phase 1 · Einstieg** | Du löst eine Aufgabe mit Stift und Papier. Der Computer bleibt noch aus. |
| **Phase 2 · Testen** | Du probierst das Neue in Scratch an einem kleinen Beispiel aus. |
| **Phase 3 · Bauen** | Du baust dein Projekt, zum Beispiel ein Spiel. |
| **Phase 4 · Abschluss** | Du speicherst dein Projekt und prüfst, was du gelernt hast. |

Am Ende jeder Karte findest du die Tabelle **Häufige Probleme & Lösungen**. Schau dort zuerst nach, wenn etwas nicht klappt.

---

## Die Zeichen auf der Karte

| Zeichen | Bedeutung |
| ------- | --------- |
| 💡 **Merke** | Das Wichtigste aus diesem Schritt. Lies es genau. |
| 💡 **Tipp** | Eine Hilfe, zum Beispiel wo du einen Block findest. |
| **Teste:** | Jetzt probierst du aus, ob dein Programm funktioniert. Achte genau darauf, was passiert. |
| **Hake ab:** | Setze einen Haken ☑, wenn du das geschafft oder beobachtet hast. |
| 🟠 **Mentor-Moment** | Zeige einem Mentor, was du gemacht hast. Der Mentor stellt dir Fragen, statt dir die Lösung zu verraten. So findest du sie selbst. |
| 🌟 **Bonusaufgabe** | Eine Zusatzaufgabe, wenn du schon fertig bist. Du musst sie nicht machen. |
| `________` | Hier schreibst du deine Antwort hin. |

---

## So sehen Scratch-Blöcke auf der Karte aus

Auf der Karte sind Scratch-Blöcke als Text geschrieben. Ein Beispiel:

```
[Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
[wiederhole fortlaufend]                 ← Steuerung (orange)
    [warte 1 Sekunden]                   ← Steuerung (orange)
    [gehe zu zufälliger Position]        ← Bewegung (blau)
```

- **Eckige Klammern `[ ]`:** Jede Zeile ist ein Block.
- **Der Pfeil `←`:** Er zeigt dir, in welcher Kategorie du den Block findest und welche Farbe er hat.
- **Eingerückte Zeilen:** Diese Blöcke stecken **in** dem Block darüber. Hier stecken „warte" und „gehe zu" in der Schleife „wiederhole fortlaufend".

### Blöcke in Blöcken

Manchmal steckt ein Block in einem Feld eines anderen Blocks. Die Klammer zeigt dir seine Form:

| Auf der Karte | In Scratch | Was du tust |
| ------------- | ---------- | ----------- |
| `< ... >` | ein **sechseckiger** Block | Hineinziehen. Er ist entweder wahr oder falsch, zum Beispiel `<wird Korb berührt?>`. |
| `( ... )` | ein **runder** Block | Hineinziehen, **nicht eintippen!** Zum Beispiel `(Punkte)` aus der Kategorie Variablen. |
| ohne Klammer | eine Zahl oder ein Wort | Selbst eintippen oder im Menü auswählen, zum Beispiel die `10` in `[ändere x um 10]`. |
| `"..."` | ein Text | Den Text eintippen, aber **ohne** die Anführungszeichen. |
| `___` | ein Platzhalter | Hier setzt du etwas Eigenes ein. Was, steht direkt unter dem Skript. Bei `"Hallo! Ich bin ___!"` tippst du zum Beispiel `Hallo! Ich bin Mia!`. |

Ein Beispiel: `[falls <(Leben) < 1> dann]` heißt: Ziehe den grünen Block „ ... < ... " in das Feld von „falls". Ziehe dann den runden Block `Leben` in sein linkes Feld und tippe `1` in das rechte Feld.

### Ein Skript erweitern

Wenn du ein Skript veränderst, das du schon gebaut hast, zeigt die Karte das so:

```diff
  [Wenn grüne Flagge angeklickt wird]      ← Ereignisse (gelb)
+ [wiederhole fortlaufend]                 ← Steuerung (orange)
      [falls <wird Mauszeiger berührt?>]   ← Steuerung (orange) / Fühlen (hellblau)
  ⋮
```

| Zeichen am Zeilenanfang | Bedeutung |
| ----------------------- | --------- |
| **+** | Diesen Block baust du neu ein. |
| **-** | Diesen Block nimmst du heraus. |
| **⋮** | Hier stehen Blöcke, die du schon hast. Sie bleiben, wie sie sind. |
| nichts | Diesen Block hast du schon. |

---

## Wenn du nicht weiterkommst

1. Lies den Schritt noch einmal langsam durch.
2. Schau in die Tabelle **Häufige Probleme & Lösungen** am Ende der Karte.
3. Mit **Strg + Z** machst du deinen letzten Schritt rückgängig.
4. Frag einen Mentor. Erzähl dabei, was du erwartet hast und was stattdessen passiert ist.

---
