# How to Use This Script

## Requirements

1. **Python 3.7+** (или выше).
2. Библиотеки [Web3.py 6+](https://pypi.org/project/web3/) и [openpyxl](https://pypi.org/project/openpyxl/).

Установить библиотеки можно командой:

pip install web3 openpyxl

## Настройка

1. **Отредактируйте `config.py`:**
   - **`RPC_URL`** — URL RPC (Ethereum, Arbitrum, BSC и т. д.).
   - **`TOKEN_CONTRACT_ADDRESS`** — адрес вашего токена (ERC-20).
   - **`amount_from` / `amount_to`** — задайте диапазон сумм для отправки, либо включите `transfer_all_balance = True` для отправки всего баланса.
   - Другие параметры (например, задержка `DELAY_BETWEEN_TXS`, порог `min_amount_transfer` и т. д.) при необходимости.

2. **Подготовьте Excel-файл** `data.xlsx`:
   - **A (колонка 1):** Приватный ключ.
   - **B (колонка 2):** Адрес получателя.

Убедитесь, что файл `data.xlsx` находится в том же каталоге или правильно указано его расположение в `config.py` (переменная `EXCEL_FILE`).
