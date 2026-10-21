# Постфиксная стековая машина

## Запуск

```bash
python main.py "3 0 4 ~ 2 ~"
```

Пример вывода:
```text
Stack state(1): [3.0]
Stack state(2): [3.0, 0.0]
Stack state(3): [3.0, 0.0, 4.0]
Stack state(4): [49.0]
Stack state(5): [49.0, 2.0]
Stack state(6): [47.0]
(3 0 4 ~ 2 ~) = 47.0
```

## Тесты и покрытие
```bash
pytest test_postfix.py
pytest --cov=main test_postfix.py   
