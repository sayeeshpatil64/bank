from q24_bank import bank

def test_bank():
    result = bank(1000, 500, 300)
    expected = "Final Balance: 1200"
    assert result == expected
