# DataFrameReporter

`DataFrameReporter` — класс для первичной диагностики таблиц pandas. Он выводит количество строк и столбцов, количество и долю дубликатов, сводную статистику, а также количество и долю пропусков.

## Установка

Выполните команды в терминале из корня проекта. Если окружение `venv` уже создано, начните со второй команды.

```bash
python3.14 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Пример запуска

Выполните команду из корня проекта. Она создаст небольшую таблицу и выведет отчёт.

```bash
python -c 'import pandas as pd; from src.dataframe_reporter import DataFrameReporter; data = pd.DataFrame({"total": [100, 100, None]}); DataFrameReporter().show_report(data, "Проверочный отчёт")'
```

В отчёте будет 3 строки, 1 столбец, 1 дубликат и 1 пропуск.

Класс находится в `src/dataframe_reporter.py`. Свои датасеты можно хранить в папке `data/`. Git игнорирует локальные файлы данных и папку виртуального окружения `venv/`.