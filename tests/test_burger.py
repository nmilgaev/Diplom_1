import pytest
from unittest.mock import MagicMock

class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_invalid_index(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    def test_move_ingredient(self, burger):
        ingredient1 = MagicMock()
        ingredient1.get_name.return_value = "Cheese"
        ingredient2 = MagicMock()
        ingredient2.get_name.return_value = "Ketchup"

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)  # перемещаем Cheese на второй индекс
        assert burger.ingredients == [ingredient2, ingredient1]  # Порядок должен быть: Ketchup, Cheese

    @pytest.mark.parametrize("ingredient_data, expected_price", [
        ([("FILLING", "Cheese", 50.0), ("SAUCE", "Ketchup", 20.0)], 270.0),
        ([("FILLING", "Lettuce", 10.0), ("FILLING", "Tomato", 15.0)], 225.0)
    ])
    def test_get_price(self, burger, bun, ingredient_data, expected_price):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = MagicMock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_price

    def test_get_receipt_with_bun(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert "Price: " in receipt
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'(==== {bun.get_name()} ====)\n' in receipt
