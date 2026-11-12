# Токенизатор

## Запуск

```bash
python3 main.py <имя файла>
```

## Пример содержимого файла
```text
x = y * 2 + z * 3
```

## Пример вывода:
```text
(IDENT, x, 1:1)
(OP, =, 1:3)
(IDENT, y, 1:5)
(OP, *, 1:7)
(INT, 2, 1:9)
(OP, +, 1:11)
(IDENT, z, 1:13)
(OP, *, 1:15)
(INT, 3, 1:17)

```
## Пример некорректного содержимого файла
```text
x @ a
```
## Пример вывода сообщения об ошибке

```text
test.txt:1:3: lexical: unexpected token '@'
```

## Тесты и покрытие
```bash
pytest test_tokenizer.py
pytest --cov=main test_tokenizer.py   
