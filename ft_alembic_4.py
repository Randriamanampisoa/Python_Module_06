#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_4.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:51:21 by fanilran            #+#    #+#            #
#   Updated: 2026/06/22 14:45:47 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")

try:
    print(f"Testing  the hidden create_heart: {alchemy.create_earth()}")
except Exception as e:
    print("Now show that not all functions can be reached\n"
    "This will raise an exception!")
    print(f"AttributeError: {e}. Did you mean: 'create_air'?\n")
