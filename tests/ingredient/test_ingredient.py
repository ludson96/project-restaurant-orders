from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    farinha1 = Ingredient("farinha")
    farinha2 = Ingredient("farinha")
    presunto = Ingredient("presunto")

    assert farinha1.name == "farinha"
    assert farinha1.restrictions == {Restriction.GLUTEN}
    assert str(farinha1) == "Ingredient('farinha')"  # __repr__
    assert farinha1 == farinha2  # __eq__
    assert farinha1 != presunto  # __eq__
    assert hash(farinha1) == hash(farinha2)  # __hash__
    assert hash(farinha1) != hash(presunto)  # __hash__
