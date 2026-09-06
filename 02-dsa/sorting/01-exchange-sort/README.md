<div align="center">

# 🔄 Exchange Sort

**My first sorting algorithm, implemented from scratch using pairwise comparisons.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Time](https://img.shields.io/badge/Time-O(n²)-F2C94C?style=flat-square)
![Space](https://img.shields.io/badge/Auxiliary%20Space-O(1)-2ea44f?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-2ea44f?style=flat-square)

</div>

---

## 🧪 About the project

This program asks the user for a collection of integers and sorts them in ascending order without using Python's built-in sorting functions.

The algorithm compares the values stored at every pair of indices and swaps them whenever they are positioned in the wrong relative order.

## ⚙️ How it works

1. Ask the user how many numbers they want to enter.
2. Store each number inside a list.
3. Compare every position `i` with every position `j`.
4. Swap the values when `list[i] < list[j]`.
5. Print the resulting list in ascending order.

## 📊 Complexity analysis

| Property | Result |
|---|---|
| Best-case time | `Θ(n²)` |
| Average-case time | `Θ(n²)` |
| Worst-case time | `Θ(n²)` |
| Auxiliary space | `O(1)` |
| In-place | Yes |
| Stable | No |

The nested loops always perform `n²` comparisons, even when the input is already sorted.

## 🔍 Important distinction

This implementation is a custom **pairwise Exchange Sort**, not the classic Bubble Sort.

Bubble Sort compares only adjacent elements, while this algorithm compares every index with every other index.

## ▶️ Running the program

```bash
python main.py
```

Example:

```text
How many elements would you like to introduce?: 5
Enter a number: 8
Enter a number: 2
Enter a number: 7
Enter a number: 1
Enter a number: 4
This is the sorted list: [1, 2, 4, 7, 8]
```

## 🧠 Concepts practiced

`Nested loops` · `Lists` · `Indexing` · `Value swapping` · `In-place sorting` · `Complexity analysis`

## 🚀 Possible improvements

- Rename `list` to `numbers` to avoid shadowing Python's built-in `list`.
- Use tuple unpacking to swap values.
- Remove redundant comparisons.
- Add tests for duplicates, negative values, and already sorted inputs.
- Implement Bubble Sort and compare both algorithms.
