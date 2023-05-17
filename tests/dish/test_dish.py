from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("Estrogonofe", 10.00)
    dish2 = Dish("Estrogonofe", 10.00)
    dish3 = Dish("Macarrão", 5.00)

    assert dish1.name == "Estrogonofe"

    # Test __hash__
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Test __eq__
    assert dish1 == dish2
    assert dish1 != dish3

    # Test __repr__
    assert str(dish1) == "Dish('Estrogonofe', R$10.00)"

    # Test raises
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Macarrão", "5")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Macarrão", -5)

    # Test Ingredients
    ingredient = Ingredient("salmão")
    dish = Dish("Estrogonofe", 10.00)
    dish.add_ingredient_dependency(ingredient, 2)

    assert dish.get_ingredients() == {Ingredient("salmão")}

    # Test Restrictions
    assert dish.get_restrictions() == {
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
