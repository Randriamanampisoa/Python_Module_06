#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:51:01 by fanilran            #+#    #+#            #
#   Updated: 2026/06/23 13:30:57 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire import light_spellbook, light_validator

ingredient = "Earth, wind Fire"
spell_name = "Fantasy"
print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(
        "Testing light spell: "
        f"{light_spellbook.light_spell_record(spell_name, ingredient)} "
        f"{light_validator.validate_ingredients(ingredient)}"
    )
