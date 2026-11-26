# Geometric Lib

## Общее описание

**Geometric Lib** — небольшая библиотека на Python для вычисления площади и периметра
простых геометрических фигур: круга, квадрата, прямоугольника и треугольника.

Каждая фигура описана в отдельном модуле, в каждом модуле есть две функции:
`area(...)` (площадь) и `perimeter(...)` (периметр). Внешних зависимостей нет,
используется только стандартный модуль `math`.

### Структура проекта

```
geometric_lib
├── circle.py
├── square.py
├── rectangle.py
├── triangle.py
└── docs
    └── README.md
```

### Использование

```python
import circle, square, rectangle, triangle

print(circle.area(1))            # 3.141592653589793
print(rectangle.perimeter(3, 5)) # 16
```

Примеры из комментариев к функциям можно проверить автоматически:

```bash
python -m doctest circle.py square.py rectangle.py triangle.py -v
```

### Формулы

| Фигура        | Площадь         | Периметр          |
|---------------|-----------------|-------------------|
| Круг          | S = πR²         | P = 2πR           |
| Квадрат       | S = a²          | P = 4a            |
| Прямоугольник | S = ab          | P = 2a + 2b       |
| Треугольник   | S = a·h / 2     | P = a + b + c     |

## Описание функций

### `circle.py`

#### `area(r)`
Площадь круга радиуса `r`.

- **Параметры:** `r` (int | float) — радиус, `r >= 0`
- **Возвращает:** float — площадь

```python
>>> circle.area(1)
3.141592653589793
```

#### `perimeter(r)`
Длина окружности радиуса `r`.

- **Параметры:** `r` (int | float) — радиус, `r >= 0`
- **Возвращает:** float — длина окружности

```python
>>> circle.perimeter(1)
6.283185307179586
```

### `square.py`

#### `area(a)`
Площадь квадрата со стороной `a`.

- **Параметры:** `a` (int | float) — сторона, `a >= 0`
- **Возвращает:** int | float — площадь

```python
>>> square.area(4)
16
```

#### `perimeter(a)`
Периметр квадрата со стороной `a`.

- **Параметры:** `a` (int | float) — сторона, `a >= 0`
- **Возвращает:** int | float — периметр

```python
>>> square.perimeter(4)
16
```

### `rectangle.py`

#### `area(a, b)`
Площадь прямоугольника со сторонами `a` и `b`.

- **Параметры:** `a`, `b` (int | float) — длина и ширина, `>= 0`
- **Возвращает:** int | float — площадь

```python
>>> rectangle.area(3, 5)
15
```

#### `perimeter(a, b)`
Периметр прямоугольника со сторонами `a` и `b`.

- **Параметры:** `a`, `b` (int | float) — длина и ширина, `>= 0`
- **Возвращает:** int | float — периметр

```python
>>> rectangle.perimeter(3, 5)
16
```

### `triangle.py`

#### `area(a, h)`
Площадь треугольника по основанию `a` и высоте `h`.

- **Параметры:** `a` (int | float) — основание; `h` (int | float) — высота к основанию
- **Возвращает:** float — площадь

```python
>>> triangle.area(6, 4)
12.0
```

#### `perimeter(a, b, c)`
Периметр треугольника со сторонами `a`, `b`, `c`.

- **Параметры:** `a`, `b`, `c` (int | float) — стороны треугольника
- **Возвращает:** int | float — периметр

```python
>>> triangle.perimeter(3, 4, 5)
12
```

## История изменений

| Хеш коммита | Описание                                            |
|-------------|-----------------------------------------------------|
| `8ba9aeb`   | L-03: Circle and square added                       |
| `d078c8d`   | L-03: Docs added                                    |
| `a141b5f`   | Add rectangle.py                                    |
| `8345e31`   | Add triangle.py                                     |
| `f1e7fdb`   | Fix rectangle perimeter calculation                 |
| `2695006`   | Add docstrings with call examples to all functions  |
| —           | Add project documentation (docs/README.md)          |
