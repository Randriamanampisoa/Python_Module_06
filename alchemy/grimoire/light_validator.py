#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:50:35 by fanilran            #+#    #+#            #
#   Updated: 2026/06/22 16:55:09 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def validate_ingredients(ingredients: str):
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    is_valid = any(i in ingredients.lower() for i in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    return f"({ingredients} - {keyword})"
