#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:50:43 by fanilran            #+#    #+#            #
#   Updated: 2026/06/17 09:28:47 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion

def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
            f"'{strength_potion()}' mixed with '{create_fire()}'")
