## Turtle

## Ściągawka dla biblioteki `turtle` w Pythonie

Rozszerzam poprzednią wersję o dodatkowe funkcje i możliwości biblioteki `turtle`.

| **Kategoria**            | **Funkcja / Metoda**                  | **Opis**                                                                | **Skrót**      |
| ------------------------ | ------------------------------------- | ----------------------------------------------------------------------- | -------------- |
| **Ruchy**                | `forward(distance)`                   | Porusza żółwia o podaną odległość do przodu.                            | `fd(distance)` |
|                          | `backward(distance)`                  | Porusza żółwia do tyłu o podaną odległość.                              | `bk(distance)` |
|                          | `right(angle)`                        | Obraca żółwia w prawo o określony kąt (w stopniach).                    | `rt(angle)`    |
|                          | `left(angle)`                         | Obraca żółwia w lewo o określony kąt (w stopniach).                     | `lt(angle)`    |
|                          | `setx(x)`                             | Ustawia pozycję żółwia na osi X.                                        | Brak           |
|                          | `sety(y)`                             | Ustawia pozycję żółwia na osi Y.                                        | Brak           |
| **Rysowanie**            | `penup()`                             | Podnosi pióro, aby żółw przestał rysować.                               | `pu()`         |
|                          | `pendown()`                           | Opuszcza pióro, aby żółw zaczął rysować.                                | `pd()`         |
|                          | `pensize(width)`                      | Ustawia grubość pióra.                                                  | Brak           |
|                          | `pencolor(color)`                     | Ustawia kolor pióra, np. `"red"`, `"blue"`.                             | Brak           |
|                          | `speed(speed)`                        | Ustawia prędkość żółwia (1-10 lub `"fastest"`, `"slowest"`).            | Brak           |
|                          | `circle(radius, extent)`              | Rysuje łuk/okrąg o promieniu i kącie (opcjonalnie).                     | Brak           |
| **Pozycjonowanie**       | `goto(x, y)`                          | Przenosi żółwia na współrzędne `(x, y)`.                                | `setpos(x, y)` |
|                          | `setheading(angle)`                   | Ustawia kierunek żółwia na określony kąt.                               | `seth(angle)`  |
|                          | `home()`                              | Przenosi żółwia do punktu początkowego (środka).                        | Brak           |
| **Kolory i wypełnienie** | `fillcolor(color)`                    | Ustawia kolor wypełnienia, np. `"green"`.                               | Brak           |
|                          | `begin_fill()`                        | Rozpoczyna wypełnianie obszaru kształtu.                                | Brak           |
|                          | `end_fill()`                          | Kończy wypełnianie obszaru kształtu.                                    | Brak           |
|                          | `bgcolor(color)`                      | Ustawia kolor tła.                                                      | Brak           |
| **Wygląd**               | `shape(name)`                         | Ustawia kształt żółwia (`"turtle"`, `"arrow"`, `"circle"`, `"square"`). | Brak           |
|                          | `shapesize(stretch_wid, stretch_len)` | Skaluje kształt żółwia.                                                 | Brak           |
| **Czyszczenie**          | `clear()`                             | Czyści rysunek, ale nie zmienia pozycji żółwia.                         | Brak           |
|                          | `reset()`                             | Czyści rysunek i resetuje pozycję żółwia.                               | Brak           |
| **Informacje**           | `position()`                          | Zwraca aktualne współrzędne żółwia.                                     | Brak           |
|                          | `heading()`                           | Zwraca aktualny kierunek żółwia.                                        | Brak           |
|                          | `isdown()`                            | Sprawdza, czy pióro jest opuszczone.                                    | Brak           |
| **Inne**                 | `stamp()`                             | Odbija kształt żółwia na aktualnej pozycji.                             | Brak           |
|                          | `undo()`                              | Cofnięcie ostatniego ruchu żółwia.                                      | Brak           |
|                          | `bye()`                               | Zamyka okno rysowania.                                                  | Brak           |
|                          | `done()`                              | Kończy pracę i utrzymuje okno aktywne.                                  | Brak           |

### Przykład bardziej zaawansowanego użycia:

```python
from turtle import *

speed("fastest")       # Najszybszy ruch żółwia
bgcolor("black")       # Kolor tła
