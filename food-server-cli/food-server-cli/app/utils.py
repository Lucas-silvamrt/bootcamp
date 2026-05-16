from datetime import datetime


def is_expired(date_str):
    today = datetime.today().date()
    expiry = datetime.strptime(date_str, "%Y-%m-%d").date()
    return expiry < today


def is_expiring_soon(date_str, days=3):
    today = datetime.today().date()
    expiry = datetime.strptime(date_str, "%Y-%m-%d").date()
    return 0 <= (expiry - today).days <= days