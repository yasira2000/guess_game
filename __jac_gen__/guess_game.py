from __future__ import annotations
from jaclang import jac_import as __jac_import__
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__
__jac_import__(target='random', base_path=__file__, mod_bundle=__jac_mod_bundle__, lng='py', absorb=False, mdl_alias=None, items={'randint': False})
from random import randint

@_Jac.make_walker(on_entry=[_Jac.DSFunc('start_game', _Jac.get_root_type())], on_exit=[])
@__jac_dataclass__(eq=False)
class GuessGame:
    correct_number: int = _Jac.has_instance_default(gen_func=lambda: randint(0, 100))

    def start_game(self, _jac_here_: _Jac.get_root_type()) -> None:
        end = _jac_here_
        i = 0
        while i < 10:
            _Jac.connect(left=end, right=(end := turn()), edge_spec=_Jac.build_edge(is_undirected=False, conn_type=None, conn_assign=None))
            i += 1
        if _Jac.visit_node(self, _Jac.edge_ref(_jac_here_, target_obj=None, dir=_Jac.EdgeDir.OUT, filter_func=None, edges_only=False)):
            pass

    def process_guess(self, guess: int) -> None:
        if guess == self.correct_number:
            print('Congratulations !!! you have guessed the number correct.')
            _Jac.disengage(self)
            return
        elif guess < self.correct_number:
            print('Too Low')
        else:
            print('Too high')

@_Jac.make_node(on_entry=[_Jac.DSFunc('check', GuessGame)], on_exit=[])
@__jac_dataclass__(eq=False)
class turn:

    def check(self, _jac_here_: GuessGame) -> None:
        guess = input('Enter the number: ')
        if guess.isdigit():
            _jac_here_.process_guess(int(guess))
        else:
            print('Enter a valid number.')
        if _Jac.visit_node(_jac_here_, _Jac.edge_ref(self, target_obj=None, dir=_Jac.EdgeDir.OUT, filter_func=None, edges_only=False)):
            pass
_Jac.spawn_call(GuessGame(), _Jac.get_root())