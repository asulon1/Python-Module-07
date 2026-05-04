# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Factory.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 11:35:27 by asulon          #+#    #+#               #
#  Updated: 2026/05/04 18:56:36 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from .Creature import Flameling, Aquabub, Torragon, Pyrodon
from ex1.creature import Sproutling, Bloomelle, Shiftling, Morphagon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Flameling | Aquabub | Sproutling | Shiftling:
        pass

    @abstractmethod
    def create_evolved(self) -> Pyrodon | Torragon | Bloomelle | Morphagon:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
