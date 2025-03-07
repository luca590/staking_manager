import unittest

# I need to run the below block to import utils
import sys
sys.path.append("../staking_manager")
# --------

from utils import get_project_root_dir, executeCliCommand
import os
from config import venv_env, main_script

account = "5C7piVESupk6paengZYaGMzdU79YTgWKoafJPfE76pYkwdEM"
mnemonic = "tomorrow pet when height sight target term flip deposit web moment wine"


class BounderTest(unittest.TestCase):
    def setUp(self):
        pass

    # bond
    def test_bond_without_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bond_without_args ", "dot", "bounder", "bond")
        self.assertTrue(
            "error: the following arguments are required: -m/--mnemonic, -ca/--controller_address, -nt/--number_of_tokens" in stdIn)

    def test_bond_missing_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bond_missing_args ", "dot", "bounder", "bond",
                                          "-m", mnemonic, "-ca", account)
        self.assertTrue(
            "error: the following arguments are required: -nt/--number_of_tokens" in stdIn)

    # BondingValidator
    # BondSize
    def test_bond_size_failure(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bond_size_failure ", "dot", "bounder", "bond",
                                          "-m", mnemonic, "-ca", account, "-nt", "0.8")
        self.assertTrue(
            "but the minimum required for bonding is" in stdIn)

    # validateAcctBalanceForBonding
    def test_bond_low_balance_failure(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bond_low_balance_failure ", "dot", "bounder",
                                          "bond",
                                          "-m", mnemonic, "-ca", account, "-nt", "100")
        self.assertTrue(
            "Low balance" in stdIn)

    # validateDecimalPoint
    def test_bond_decimal_point_failure(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bond_decimal_point_failure ", "dot", "bounder",
                                          "bond",
                                          "-m", mnemonic, "-ca", account, "-nt", "1.25555254548754858")
        self.assertTrue(
            "wrong token value token take max" in stdIn)

    def test_bond_success(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bond_success ", "dot", "bounder", "bond",
                                          "-m", mnemonic, "-ca", account, "-nt", "1")
        self.assertTrue(
            "sent and included in block" in stdIn)

    # unbond
    def test_unbond_without_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_unbond_without_args ", "dot", "bounder",
                                          "unbond")
        self.assertTrue(
            "error: the following arguments are required: -m/--mnemonic, -nt/--number_of_tokens" in stdIn)

    def test_unbond_missing_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_unbond_missing_args ", "dot", "bounder",
                                          "unbond",
                                          "-m", mnemonic)
        self.assertTrue(
            "error: the following arguments are required: -nt/--number_of_tokens" in stdIn)

    def test_unbond(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_unbond_success ", "dot", "bounder", "unbond",
                                          "-m", mnemonic, "-nt", "1")
        self.assertTrue(
            "sent and included in block" in stdIn)

    # rebond
    def test_rebond_without_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_rebond_without_args ", "dot", "bounder",
                                          "rebond")
        self.assertTrue(
            "error: the following arguments are required: -m/--mnemonic, -nt/--number_of_tokens" in stdIn)

    def test_rebond_missing_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_rebond_missing_args ", "dot", "bounder",
                                          "rebond",
                                          "-m", mnemonic)
        self.assertTrue(
            "error: the following arguments are required: -nt/--number_of_tokens" in stdIn)

    def test_rebond(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_rebond_success ", "dot", "bounder", "rebond",
                                          "-m", mnemonic, "-nt", "1")
        self.assertTrue(
            "sent and included in block" in stdIn)

    # bondextra
    def test_bondextra_without_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bondextra_without_args ", "dot", "bounder",
                                          "bondextra")
        self.assertTrue(
            "error: the following arguments are required: -m/--mnemonic, -nt/--number_of_tokens" in stdIn)

    def test_bondextra_missing_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bondextra_missing_args ", "dot", "bondextra",
                                          "bondextra",
                                          "-m", mnemonic)
        self.assertTrue(
            "error: the following arguments are required: -nt/--number_of_tokens" in stdIn)

    def test_bondextra(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_bondextra_success ", "dot", "bondextra",
                                          "bondextra", "-m", mnemonic, "-nt", "1")
        self.assertTrue(
            "sent and included in block" in stdIn)

    # withdrawunbonded
    def test_withdrawunbonded_without_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_withdrawunbonded_without_args ", "dot",
                                          "bounder", "withdrawunbonded")
        self.assertTrue(
            "error: the following arguments are required: -m/--mnemonic" in stdIn)

    def test_withdrawunbonded_missing_args(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_withdrawunbonded_missing_args ", "dot",
                                          "bounder", "withdrawunbonded",
                                          "-m")
        self.assertTrue(
            "error: argument -m/--mnemonic: expected one argument" in stdIn)

    def test_withdrawunbonded(self):
        stdIn, sdtOut = executeCliCommand(venv_env, main_script, "test_withdrawunbonded_success ", "dot", "bounder",
                                          "withdrawunbonded",
                                          "-m", mnemonic, "-nt", "1")
        self.assertTrue(
            "sent and included in block" in stdIn)


if __name__ == '__main__':
    unittest.main()
