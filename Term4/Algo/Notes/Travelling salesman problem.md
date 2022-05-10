---
aliases: TSP
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Problem
We have a list of cities and the distances between very pair of cities. Suppose we are given a particular route that visits each city exactly once and returns to the origin city. Does this route have the shortest distance, among all such possible routes?

## Solving "converted" decision problems
> If we have a solution to an [[Optimisation problem]], then we can use this solution to solve the "converted" [[Decision problem]].

Example: [[Travelling salesman problem]]
- Suppose we know how to solve this.
- This means we have an algorithm to find a shortest route that visits each city exactly once and returns to origin city
- This means any other shortest route found must have same total distance as the shortest route found
- Solving the decision problem: given a candidate, we can compute its total distance, and check if the value equals the total distance of your shortest route found.

## Verifying a no
One possible [[Verification algorithms|certificate]] for a "no" answer is a route whose distance is strictly smaller than the distance of the input route $I$

## Verifying a yes
We need to confirm that every other possible route has a distance that is NOT strictly smaller than the distance of the given route.

One possible [[Verification algorithms|certificate]] for a "yes"