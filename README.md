# Лабораторная работа №2

Самодуров Матвей Николаевич, группа 221341, вариант 8, лабораторная №2.

## Задания варианта

**Средняя сложность:**

- №8 — перевернуть строку (`lab2/reverse.py`)
- №10 — словарь квадратов чисел (`lab2/squares.py`)
- №4 — НОД двух чисел (`lab2/gcd.py`)

**Повышенная сложность:**

- №8 — бинарный поиск (`lab2/searching.py`)
- №1 — сортировка списка пузырьком (`lab2/sorting.py`)

## Запуск

```bash
python -m lab2
```

## Проверки

```bash
python -m unittest discover -s tests -v
python -m compileall -q lab2 tests
flake8 lab2 tests
```

Подробное описание выполнения — в `docs/report.md`.
