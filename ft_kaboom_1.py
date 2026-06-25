#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:51:04 by fanilran            #+#    #+#            #
#   Updated: 2026/06/23 14:10:41 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.dark_spellbook import dark_spell_record
from alchemy.grimoire.dark_validator import validate_ingredients


ingredient = "frogs"
spell_name = "Fantastic"
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print(
        f"Testing dark spell: {dark_spell_record(spell_name, ingredient)} "
        f"{validate_ingredients(ingredient)}"
    )
