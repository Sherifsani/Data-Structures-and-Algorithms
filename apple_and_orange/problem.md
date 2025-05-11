# 🍎🍊 Count Apples and Oranges

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given, this challenge determines how many apples and oranges land on Sam's house.

## Problem Description

* Sam's house is located between points **`s`** and **`t`** on the x-axis.
* The **apple tree** is located at point **`a`** (to the left of the house).
* The **orange tree** is located at point **`b`** (to the right of the house).

When a fruit falls:

* It lands a certain distance from its tree along the x-axis.
* A negative distance means the fruit falls to the left; a positive distance means it falls to the right.

Given the distances at which apples and oranges fall, determine how many of them land on Sam's house (within the inclusive range `[s, t]`).

## Function Signature

```python
def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]) -> None:
```

## Parameters

* `s` (int): Starting point of Sam's house.
* `t` (int): Ending point of Sam's house.
* `a` (int): Location of the apple tree.
* `b` (int): Location of the orange tree.
* `apples` (list of int): Distances each apple falls from the apple tree.
* `oranges` (list of int): Distances each orange falls from the orange tree.

## Input Format

```
s t
a b
m n
apples (m space-separated integers)
oranges (n space-separated integers)
```

Where:

* `m` is the number of apples
* `n` is the number of oranges

## Constraints

* Fruits can fall both to the left (negative distance) and to the right (positive distance).
* Print two integers:

  * First line: number of apples that fall on Sam's house.
  * Second line: number of oranges that fall on Sam's house.

## Output Format

Print the result:

```
<number_of_apples>
<number_of_oranges>
```

## Example

**Sample Input 0**

```
7 11
5 15
3 2
-2 2 1
5 -6
```

**Sample Output 0**

```
1
1
```

### Explanation:

* Apples fall at positions: `3`, `7`, `6`
* Oranges fall at positions: `20`, `9`

Fruits within the house range `[7, 11]`:

* Apple: only `7` ➔ count is `1`
* Orange: only `9` ➔ count is `1`

Thus, we print:

```
1
1
```

