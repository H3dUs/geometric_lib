# Geometric Lib

## Общее описание

**Geometric Lib** — небольшая библиотека на Python для вычисления площади и периметра
простых геометрических фигур: круга и квадрата.

Каждая фигура описана в отдельном файле, в каждом файле есть две функции:
`area(...)` (площадь) и `perimeter(...)` (периметр).

### Структура проекта

```
geometric_lib
├── circle.py
├── square.py
├── test_circle.py
├── test_square.py
├── .gitignore
├── .github
│   └── workflows
│       └── main.yml
└── docs
    ├── README.md
    ├── test_plan.md
    ├── ci.md
    └── img
        ├── tests_ok.png
        ├── tests_fail.png
        ├── ci_ok.png
        └── ci_windows.png
```

### Использование

```python
import circle
import square

print(circle.area(1))       # 3.141592653589793
print(square.perimeter(4))  # 16
```

## Описание функций

### `circle.py`

#### `area(r)`
Площадь круга радиуса `r`.

- **Параметры:** `r` (int | float) — радиус, `r >= 0`
- **Возвращаемое значение:** float — площадь

```python
>>> circle.area(1)
3.141592653589793
```

#### `perimeter(r)`
Длина окружности радиуса `r`.

- **Параметры:** `r` (int | float) — радиус, `r >= 0`
- **Возвращаемое значение:** float — длина окружности

```python
>>> circle.perimeter(1)
6.283185307179586
```

### `square.py`

#### `area(a)`
Площадь квадрата со стороной `a`.

- **Параметры:** `a` (int | float) — сторона, `a >= 0`
- **Возвращаемое значение:** int | float — площадь

```python
>>> square.area(4)
16
```

#### `perimeter(a)`
Периметр квадрата со стороной `a`.

- **Параметры:** `a` (int | float) — сторона, `a >= 0`
- **Возвращаемое значение:** int | float — периметр

```python
>>> square.perimeter(4)
16
```

## Тестирование

Функции покрыты unit-тестами на стандартном модуле `unittest`:

- `test_circle.py` — тесты `circle.area` и `circle.perimeter`;
- `test_square.py` — тесты `square.area` и `square.perimeter`.

Запуск всех тестов из корня проекта:

```
python3 -m unittest -v
```

План тестирования описан в [test_plan.md](test_plan.md).

## Непрерывная интеграция (CI)

После каждого push GitHub Actions автоматически запускает все unit-тесты
на двух runner'ах: `ubuntu-latest` и `windows-latest`.
Workflow описан в файле `.github/workflows/main.yml`.

Подробности и результаты запуска — в [ci.md](ci.md).

## История изменений

| Хеш коммита | Описание                                |
|-------------|-----------------------------------------|
| `8ba9aeb`   | L-03: Circle and square added           |
| `d078c8d`   | L-03: Docs added                        |
| `adbfd2a`   | Add docstrings in files                 |
| `8ed5e45`   | Updated proj documentation              |
| `ad31f3a`   | Final update in docs                    |
| `53271b3`   | Docs: update changelog                  |
| `4da91c1`   | L-04: Unit tests added                  |
| `a45ad3b`   | L-04: Docs: tests section and test plan |
| `1a64adb`   | L-04: Docs: fix README                  |
| `1174bd8`   | L-05: CI workflow added                 |
