# StakingManager
Python based CLI tool for staking (nominating) in Polkadot
<br />⚠️ Not production ready ⚠️

## Instructions:
run `python StakingManager.py dot -h`
    <br />- NOTE: because only polkadot is supported, you must give `dot` as the first argument.
    In the future, when we support additional networks, there will be other options to `dot`

### Features:
* Pretty intuitive ArgParser (see examples.py) for:
	- Creating a mnemonic, keypair, getting acct info
	- Bonding, unbonding, rebonding, withdrawing
	- Nominating (Staking), setting staker requirements
* Validations and error handling for staking:
	- Keep-alive checks (existential deposit)
	- https://wiki.polkadot.network/docs/maintain-errors

### Codebase Notes:
* StakingManager.py is the cli executed file
* Most "unique" logic is in fxn_decorator_implementations folder
* config.py specifies the network (see bottom of config file), right now only Polkadot mainnet and Westend are really functional
* Under the hood:
    - SubstrateInterface (py):
        + Github: https://github.com/polkascan/py-substrate-interface
        + Documentation: https://polkascan.github.io/py-substrate-interface/
    - SS58:
        + Github: https://github.com/paritytech/ss58-registry/blob/main/ss58-registry.json
    - TODO: Testing Tools:
        + https://github.com/wpank/polkadot-local-network
        + https://github.com/w3f/1k-validators-be/blob/master/src/misc/testSetup.ts

### Coding Patterns (Ideals):
* SOLID - https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd
* If a filename has a corresponding Utils file, one should not ever need to import the Utils file except in its pair.
    - For example, accountManager.py should import accountManagerUtils.py, but no other files should import accountManagerUtils.py.
Instead, all other files should only ever have to import accountManager.py.
* Pass "generic" arguements first in a function and more unique arguements subsequently
    - For example, in `def __init__(self, logger, accountManager)`, `self` and `logic` are generic and therefore passed before `accountManager`


#### Immediate TODOs:
* Add local network docker deployment for better testing
* Adding new substrate based chains to stake on
* check TODOs in substrateCallImplementationUtils
* rename all cases of "bounder" to "bonder"
* rename code_src > src
