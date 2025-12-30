Pewnie 🙂 Poniżej masz **zadanie zapisane w Markdown**, z czytelną strukturą oraz **tabelą na dane wejściowe i wyjściowe**.

---

# 🥕 Zadanie **Królik**

**LOGIA 25 (2024/25), etap 2**

## 📘 Treść zadania

Królik przygotowuje się do wysiewu marchwi. Pragnie, aby wszystkie marchewki wykiełkowały i nie chce zbyt długo czekać na pierwsze plony.

* Posiane **zbyt płytko** nie wzejdą.
* Posadzenie ich **głębiej** wydłuża czas oczekiwania na plony.

Dlatego królik chce wyrównać głębokość dołków, w których sadzi marchewki, w **optymalny sposób**:

* Jeśli **choć jeden dołek jest za płytki**, królik **pogłębia wszystkie za płytkie dołki**.
* W przeciwnym przypadku **dosypuje ziemię w najpłytszych dołkach**, tak aby miały **minimalną głębokość**, przy której marchewki wzeszły.

Twoim zadaniem jest napisać program, który:

* wczyta minimalną głębokość dołka,
* wczyta głębokości wszystkich dołków,
* obliczy **łączną zmianę głębokości dołków**.

---

## 📥 Wejście

| Element      | Opis                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------- |
| `g`          | minimalna głębokość dołka, liczba całkowita, `1 ≤ g ≤ 1000`                                     |
| lista dołków | niepusty ciąg liczb całkowitych (maks. 100 000), każda w zakresie `1–2000`, oddzielone spacjami |

---

## 📤 Wyjście

| Element | Opis                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------ |
| wynik   | jedna liczba całkowita – łączna zmiana głębokości dołków (suma pogłębień **lub** suma dosypanej ziemi) |

---

## 📊 Przykłady

### Przykład 1

| Dane      | Wartość                                          |
| --------- | ------------------------------------------------ |
| Wejście   | `g = 20`<br>`8 30 15 40 20`                      |
| Wyjście   | `17`                                             |
| Komentarz | Należy pogłębić pierwszy dołek o 12 i trzeci o 5 |

---

### Przykład 2

| Dane      | Wartość                                         |
| --------- | ----------------------------------------------- |
| Wejście   | `g = 12`<br>`30 40 50 40 30 60 70`              |
| Wyjście   | `36`                                            |
| Komentarz | Należy dosypać w pierwszym i piątym dołku po 18 |

---

### Przykład 3

| Dane      | Wartość                            |
| --------- | ---------------------------------- |
| Wejście   | `g = 10`<br>`8 30 15 40 20`        |
| Wyjście   | `2`                                |
| Komentarz | Należy pogłębić pierwszy dołek o 2 |

---

Jeśli chcesz, mogę:

* pomóc rozpisać **algorytm krok po kroku**,
* przygotować **rozwiązanie w Pythonie / C++**,
* albo wyjaśnić zadanie prostszym językiem 👌
