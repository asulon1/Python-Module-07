# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  factory.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 15:41:55 by asulon          #+#    #+#               #
#  Updated: 2026/04/22 16:01:45 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import CreatureFactory
from .creature import Bloomelle, Sproutling, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
