#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:50:49 by fanilran            #+#    #+#            #
#   Updated: 2026/06/17 09:25:06 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .elements import create_air, create_earth
from elements import create_fire, create_water

def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    return f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
