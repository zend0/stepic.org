#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fib(n):
    f = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
    return f[n]


def main():
    n = int(input())
    # n = int(sys.stdin.readline())
    print(fib(n))


if __name__ == "__main__":
    main()