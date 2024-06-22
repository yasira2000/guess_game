from __future__ import annotations
from jaclang import jac_import as __jac_import__
__jac_import__(target='random', base_path=__file__, mod_bundle=__jac_mod_bundle__, lng='py', absorb=False, mdl_alias=None, items={'randint': False})
from random import randint
print('Random number ', randint(0, 100))