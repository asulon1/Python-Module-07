# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  battle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 11:43:06 by asulon          #+#    #+#               #
#  Updated: 2026/04/21 12:04:33 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import AquaFactory as Aqua, FlameFactory as Flame


def factory_test(factory: Aqua | Flame) -> None:
    base = factory.create_base()
    evolve = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolve.describe())
    print(evolve.attack())


def battle(atk_factory: Aqua | Flame, def_factory: Aqua | Flame) -> None:
    atk_base = atk_factory.create_base()
    def_base = def_factory.create_base()

    print(f"{atk_base.describe()}\n vs.\n{def_base.describe()}")
    print(f"{atk_base.attack()}\n{def_base.attack()}")


def main() -> None:
    fire = Flame()
    aqua = Aqua()

    print("Testing factory")
    factory_test(fire)
    print("\nTesting factory")
    factory_test(aqua)
    print("\nTesting battle")
    battle(fire, aqua)


if __name__ == "__main__":
    main()
