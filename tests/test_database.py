from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns_length(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_name(self, database):
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_buns_price(self, database):
        buns = database.available_buns()
        assert buns[0].get_price() == 100
        assert buns[1].get_price() == 200
        assert buns[2].get_price() == 300

    def test_available_ingredients_length(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_name(self, database):
        ingredients = database.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"

    def test_available_ingredients_type(self, database):
        ingredients = database.available_ingredients()
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING