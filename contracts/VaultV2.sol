// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";

contract VaultV2 is Initializable {
    uint256 private value;

    function store(uint256 _value) external reinitializer(3) {
        value = _value;
    }

    function retrieve() external view returns (uint256) {
        return value;
    }

    function increment() public {
        value = value + 1;
    }
}
