#!/usr/bin/python3

import brownie
from brownie import chain

def test_stake(accounts, staking_contracts):
	(staked_token, reward_token, staking) = staking_contracts
