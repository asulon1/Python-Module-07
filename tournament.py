# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  tournament.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 17:26:57 by asulon          #+#    #+#               #
#  Updated: 2026/04/22 20:07:03 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import Aqua, Flame, CreatureFactory
from ex1 import Healing, Transform
from ex2 import (StrategyError, Aggressive,
                 Normal, Defensive, BattleStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]
           ) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    if len(opponents) < 2:
        print("Not enough opponents for a tournament")
        return

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            atk_factory, atk_strategy = opponents[i]
            def_factory, def_strategy = opponents[j]

            atk_creature = atk_factory.create_base()
            def_creature = def_factory.create_base()

            print("* Battle *")
            print(atk_creature.describe())
            print(" vs.")
            print(def_creature.describe())

            print(" now fight!")
            try:
                atk_strategy.act(atk_creature)
                def_strategy.act(def_creature)
            except StrategyError as error:
                print(f"Battle error, aborting tournament {error}")
                return


def main() -> None:
    print("Tournament 0 (basic)\n [ (Flameling+Normal), (Healing+Defensive) ]")
    opponents = [(Flame(), Normal()), (Healing(), Defensive())]
    battle(opponents)

    print("\nTournament 1 (error)\n"
          "[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents = [(Flame(), Aggressive()), (Healing(), Defensive())]
    battle(opponents)

    print("\nTournament 2 (multiple)\n"
          "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    opponents = [(Aqua(), Normal()), (Healing(), Defensive()),
                 (Transform(), Aggressive())]
    battle(opponents)


if __name__ == "__main__":
    main()
