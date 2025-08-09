class RiskManager:
    def __init__(self, max_position_size, max_daily_loss, risk_per_trade, account_balance, stop_loss, take_profit):
        self.max_position_size = max_position_size
        self.max_daily_loss = max_daily_loss
        self.risk_per_trade = risk_per_trade
        self.account_balance = account_balance
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.daily_loss = 0.0