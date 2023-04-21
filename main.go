package main

import "math"

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func add(a int, b int) int {
	sum := a
	for b != 0 {
		sum = a ^ b
		b = (a & b) << 1
		a = sum
	}
	return sum
}

func minus(a int, b int) int {
	return add(a, add(^b, 1))
}

func multi(a int, b int) int {
	neg := (a < 0) != (b < 0)
	res := 0
	a, b = abs(a), abs(b)
	for b != 0 {
		if (b & 1) != 0 {
			res = add(res, a)
		}
		a <<= 1
		b >>= 1
	}
	if neg {
		res = -res
	}
	return res
}

func div(a int, b int) int {
	neg := (a < 0) != (b < 0)
	res := 0
	a, b = abs(a), abs(b)
	// 获取a的二进制长度
	l := int(math.Log2(float64(a))) + 1
	for i := l; i >= 0; i-- {
		if (a >> i) >= b {
			res |= (1 << i)
			a = minus(a, b<<i)
		}
	}
	if neg {
		res = -res
	}
	return res
}

func main() {
	println(add(10, 1))
	println(add(10, -1))
	println(add(-10, 1))
	println(add(-10, -1))
	println(minus(10, 1))
	println(minus(10, -1))
	println(minus(-10, 1))
	println(minus(-10, -1))
	println(multi(10, 1))
	println(multi(10, -1))
	println(multi(-10, 1))
	println(multi(-10, -1))
	println(div(10, 3))
	println(div(100, -3))
	println(div(-10, 3))
	println(div(-10, -3))
}
