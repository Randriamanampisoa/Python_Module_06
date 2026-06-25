#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_spellbook.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:50:27 by fanilran            #+#    #+#            #
#   Updated: 2026/06/22 17:24:23 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    from .dark_validator import validate_ingredients
    validate_result = validate_ingredients(ingredients)
    if "- VALID" in validate_result:
        return f"Spell recorded: {spell_name}"
    else: 
        return f"Spell rejected: {spell_name}"