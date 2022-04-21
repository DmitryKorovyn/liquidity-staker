#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
	# perform a chain rewind after completing each test, to ensure proper isolation
	# https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
	pass

@pytest.fixture(scope="module")
def staking_contracts(TestERC20, StakingRewards, accounts):
	staked_token = TestERC20.deploy("Staked token", "STAKED_TOKEN", 18, 1e21, {"from": accounts[0]})
	reward_token = TestERC20.deploy("Reward token", "REWARD_TOKEN", 18, 1e21, {"from": accounts[0]})

	staking = StakingRewards.deploy(staked_token.address, reward_token.address, accounts[0], {"from": accounts[0]})

	return (staked_token, reward_token, staking)