#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:50:30 by fanilran            #+#    #+#            #
#   Updated: 2026/06/22 17:23:21 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def validate_ingredients(ingredients: str):
    from .dark_spellbook import dark_spell_allowed_ingredients
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(i in ingredients.lower() for i in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    return f"({ingredients} - {keyword})"
