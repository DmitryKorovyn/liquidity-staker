// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity >0.5.0 <0.6.0;

import "OpenZeppelin/openzeppelin-contracts@2.3.0/contracts/token/ERC20/ERC20Detailed.sol";
import "OpenZeppelin/openzeppelin-contracts@2.3.0/contracts/token/ERC20/ERC20Mintable.sol";

contract TestERC20 is ERC20Detailed, ERC20Mintable {
    constructor(uint amount) ERC20Detailed('Test ERC20', 'TEST', 18) public {
        mint(msg.sender, amount);
    }
}
