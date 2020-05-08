# project/api/v1/accounts/crud.py


from project import db
from project.api.models import Account


def get_all_accounts():
    return Account.query.order_by(Account.created_at.desc()).all()
    # return Account.query.all()


def get_account_by_email(email):
    return Account.query.filter_by(email=email).first()


def add_account(email, password):
    account = Account(email=email, password=password)
    db.session.add(account)
    db.session.commit()
    return account
