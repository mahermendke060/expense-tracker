from backend import db_helper

def test_fetch_expenses_for_date():
    expenses=db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses)==1

    assert expenses[0]['amount']==10
    assert expenses[0]['category']=='Shopping'
    assert expenses[0]['notes']=='Bought potatoes'

def test_fetch_expenses_for_date_invalid():
    expenses=db_helper.fetch_expenses_for_date("9999-01-01")

    assert len(expenses)==0

def test_fetch_expense_summary_invalid_range():
    summary=db_helper.fetch_expense_summary("9999-09-01","2015-05-15")
    assert len(summary)==0