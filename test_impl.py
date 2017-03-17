""" Class: CIS 640 ZA
    Assignment: Extra Credit 1
    Author: Zachary Cleary """

import impl


class TestTicTacToeCheck(object):
    """ Unit tests for function tic_tac_toe_check """

    def test_raises_if_board_is_none(self):
        """ Asserts that TypeError is raised if the given board is None """
        try:
            impl.tic_tac_toe_check(None)
            assert False
        except TypeError:
            assert True
        except:
            assert False

    def test_raises_if_board_is_non_list(self):
        """ Asserts that TypeError is raised if the given board is not a list """
        try:
            impl.tic_tac_toe_check("board")
            assert False
        except TypeError:
            assert True
        except:
            assert False

    def test_raises_if_board_is_not_length_nine(self):
        """ Asserts that ValueError is raised if the board is not exactly nine strings """
        try:
            impl.tic_tac_toe_check([""])
            assert False
        except ValueError:
            assert True
        except:
            assert False

    def test_raises_if_board_contains_invalid_characters(self):
        """ Asserts that ValueError is raised if the board contains invalid characters """
        try:
            impl.tic_tac_toe_check(["", "", "", "", "", "", "", "", "z"])
            assert False
        except ValueError:
            assert True
        except:
            assert False

    def test_raises_if_board_contains_more_than_one_winner(self):
        """ Asserts that ValueError is raised if the board contains more than one winner """
        try:
            impl.tic_tac_toe_check(["x", "x", "x", "o", "o", "o", "", "", ""])
            assert False
        except ValueError:
            assert True
        except:
            assert False

    def test_returns_winning_char_if_board_is_legal(self):
        """ Asserts that the winning character is returned if the given board is a legal board """
        try:
            impl.tic_tac_toe_check(["", "", "", "", "", "", "", "", ""])
            assert True
        except:
            assert False
