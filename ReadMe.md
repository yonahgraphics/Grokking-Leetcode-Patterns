# Grokking Leetcode Patterns

## Table of Contents

- [Background](#background)
- [Preface](#preface)
- [Notes](#notes)
- [Question List](#question-list)
- [Solutions](#solutions)
- [Leetcode Discuss](#leetcode-discuss)
- [Tips to Consider](#tips-to-consider)
- [Suggestions](#suggestions)
- [Acknowledgements](#acknowledgements)

## Background

This repo is intended for any individual that want to improve their problem
solving skills for coding interviews.

Problems are grouped under their respective subtopic, in order to focus on
repeatedly applying common patterns rather than randomly tackling questions.

All questions are available on [leetcode.com] with some requiring [leetcode premium].

## Preface

It is highly recommended to read chapters 1, 2, 3, 4, 8, and 10 of [Cracking The Coding Interview]
to familiarize yourself with the following data structures and their operations:

- Arrays
- Maps
- Linked Lists
- Queues
- Heaps
- Stacks
- Trees
- Graphs

In addition, you should have a good grasp on common algorithms such as:

- Breadth-first search
- Depth-first search
- Binary search
- Recursion

## Question List

The some question that are solved here can be found here:
https://seanprashad.com/leetcode-patterns/.


## Solutions

Solutions written in Python can be found here [solutions].

## Leetcode Discuss

[Leetcode discuss] is an amazing resource and features previous interview
questions, as well as compensation and general career advice.

## Tips to Consider

```
If input array is sorted then
    - Binary search
    - Two pointers

If asked for all permutations/subsets then
    - Backtracking

If given a tree then
    - DFS
    - BFS

If given a graph then
    - DFS
    - BFS

If given a linked list then
    - Two pointers

If recursion is banned then
    - Stack

If must solve in-place then
    - Swap corresponding values
    - Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
    - Dynamic programming

If asked for top/least K items then
    - Heap

If asked for common strings then
    - Map
    - Trie

Else
    - Map/Set for O(1) time & O(n) space
    - Sort input for O(nlogn) time and O(1) space
```

## Suggestions

Think a question should/shouldn't be included? Wish there was another feature?
Feel free to open an [issue] with your suggestion!

## Acknowledgements

This list is heavily inspired by  from [Grokking the Coding Interview]  and  [Sean Prashad's leetcode Patterns repository], with
additional problems extracted from the [Blind 75 list] and this medium article
on [14 patterns to ace any coding interview question].

[leetcode premium]: https://leetcodehttps://github.com/seanprashad/leetcode-patterns.com/subscribe/
[this pdf]: https://drive.google.com/open?id=1ao4ZA28zzBttDkuS6MLQI52gDs_CJZEm
[cracking the coding interview]: http://www.crackingthecodinginterview.com/contents.html
[here]: https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed
[topcoder]: https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/
[back to back swe youtube channel]: https://www.youtube.com/watch?v=jgiZlGzXMBw
[solutions]: https://github.com/yonahgraphics/Leetcode-Patterns
[leetcode discuss]: https://leetcode.com/discuss/interview-question
[grokking the coding interview]: https://www.educative.io/courses/grokking-the-coding-interview
[Sean Prashad's leetcode Patterns repository]: https://github.com/seanprashad/leetcode-patterns
[issue]: https://github.com/yonahgraphics/Leetcode-Patterns/issues/new
[blind 75 list]: https://www.teamblind.com/article/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU?utm_source=share&utm_medium=ios_app
[14 patterns to ace any coding interview question]: https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed
