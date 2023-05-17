from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Instantiate ingredients
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    ingredient3 = Ingredient("presunto")

    # Test __repr__
    assert str(ingredient1) == "Ingredient('farinha')"

    # Test __eq__
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    # Test __hash__
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)

    # Test attributes
    assert ingredient1.name == "farinha"
    assert ingredient1.restrictions == {Restriction.GLUTEN}
