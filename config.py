from decimal import Decimal

# ========================= RPC / Сеть =========================
# Укажите RPC вашей сети (Ethereum, BSC, Arbitrum, Polygon, и т.д.)
RPC_URL = "https://zircuit1-mainnet.liquify.com"

# Адрес вашего ERC-20 токена
TOKEN_CONTRACT_ADDRESS = "0xfd418e42783382E86Ae91e445406600Ba144D162"

# ====================== Параметры отправки =====================

# Если transfer_all_balance = False, отправляем случайную сумму
# из диапазона [amount_from, amount_to] (в «человеческом» формате).
amount_from = 0.15
amount_to   = 0.16

# Если transfer_all_balance = True, отправляем весь баланс, оставляя
# на кошельке случайное число из диапазона [keep_value_from, keep_value_to].
transfer_all_balance = True
keep_value_from = 0
keep_value_to   = 0

# Если итоговая сумма меньше, чем min_amount_transfer, транзакция не отправляется
min_amount_transfer = 0.01

# Задержка между транзакциями (в секундах)
DELAY_BETWEEN_TXS = 80

# ===================== Комиссия (EIP-1559) =====================
# Если ваша сеть поддерживает EIP-1559 (Ethereum, Arbitrum и т.д.),
# используем maxFeePerGas / maxPriorityFeePerGas.
# Если нет (BSC), закомментируйте и используйте gasPrice в main.py.
MAX_FEE_PER_GAS_GWEI = Decimal("30")
MAX_PRIORITY_FEE_PER_GAS_GWEI = Decimal("2")

# ====================== Параметры Excel ========================
EXCEL_FILE = "data.xlsx"
SHEET_NAME = "1"

# ========================= ERC-20 ABI ==========================
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]
