import util
import math

class OreQuantity(object):
    def __init__(self, element=None, quantity=None, formula=None):
        self.element = element
        self.quantity = quantity
        if formula is not None:
            self.quantity, self.element = formula.strip().split(" ")
            self.quantity = int(self.quantity)

    def __repr__(self):
        return f"{self.quantity} {self.element}"

class Reaction(object):
    def __init__(self, formula):
        reactants, result = formula.split("=>")

        self.result = OreQuantity(formula=result)
        self.reactants = list(OreQuantity(formula=v) for v in reactants.split(","))

    def __repr__(self):
        return ", ".join(str(v) for v in self.reactants) + " => " + str(self.result)


def compute_ingredients(quantity, reaction):
    ingredients = []
    for ingredient in reaction.reactants:
        ingredients.append(OreQuantity(
            ingredient.element,
            ingredient.quantity * math.ceil(quantity / reaction.result.quantity)))
    return ingredients

def calc_ore(results, reactions):
    ore = 0
    ingredients = {}
    for result in results.values():
        if result.element == "ORE":
            if "ORE" not in ingredients:
                ingredients["ORE"] = result
            else:
                ingredients["ORE"].quantity += result.quantity
        else:
            for ingredient in compute_ingredients(result.quantity, reactions[result.element]):
                if ingredient.element not in ingredients:
                    ingredients[ingredient.element] = ingredient
                else:
                    ingredients[ingredient.element].quantity += ingredient.quantity

    return ingredients

def part1(data):
    reactions = {}
    for reaction in data:
        reactions[reaction.result.element] = reaction
    
    ingredients = {"FUEL": OreQuantity("FUEL", 1)}
    while "ORE" not in ingredients or len(ingredients) > 1:
        ingredients = calc_ore(ingredients, reactions)

    print(ingredients)

    util.Answer(1, ingredients["ORE"])

        
def part2(data):
    util.Answer(2, None)


if __name__ == "__main__":
    data = util.ReadPuzzle()
    data = [
        "157 ORE => 5 NZVS",
        "165 ORE => 6 DCFZ",
        "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
        "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
        "179 ORE => 7 PSHF",
        "177 ORE => 5 HKGWZ",
        "7 DCFZ, 7 PSHF => 2 XJWVT",
        "165 ORE => 2 GPVTF",
        "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT",
    ]
    data = list(Reaction(v) for v in data)

    part1(data)
    part2(data)
