# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capacitor.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 12:10:07 by asulon          #+#    #+#               #
#  Updated: 2026/04/22 17:27:12 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1 import Healing, Transform


def test_healing_factory(factory: Healing) -> None:
    base = factory.create_base()
    evolve = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolve:")
    print(evolve.describe())
    print(evolve.attack())
    print(evolve.heal(base))


def test_transform_factory(factory: Transform) -> None:
    base = factory.create_base()
    evolve = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolve:")
    print(evolve.describe())
    print(evolve.attack())
    print(evolve.transform())
    print(evolve.attack())
    print(evolve.revert())


def main() -> None:
    healing = Healing()
    transform = Transform()
    print('Testing Creature with healing capability')
    test_healing_factory(healing)
    print()
    print('Testing Creature with transform capability')
    test_transform_factory(transform)


if __name__ == "__main__":
    main()
