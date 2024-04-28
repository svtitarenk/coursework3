from src.functions import hide_numbers

card_Maestro = "Maestro 1596837868705199"
bill_1 = "Счет 64686473678894779589"
card_visa_classic = "Visa Classic 6831982476737658"
empty_string = None


def test_hide_numbers():
    assert hide_numbers(card_Maestro) == "Maestro 1596 83** **** 5199"
    assert hide_numbers(card_visa_classic) == "Visa Classic 6831 98** **** 7658"
    assert hide_numbers(bill_1) == "Счет **9589"
    assert hide_numbers(empty_string) == "Не определено"