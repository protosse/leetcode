解题的核心思路是按照右、下、左、上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界
![](https://labuladong.github.io/algo/images/%e8%8a%b1%e5%bc%8f%e9%81%8d%e5%8e%86/6.png)
随着螺旋遍历，相应的边界会收缩，直到螺旋遍历完整个数组
![](https://labuladong.github.io/algo/images/%e8%8a%b1%e5%bc%8f%e9%81%8d%e5%8e%86/7.png)

还有一种牛逼的思路是先遍历第一行，然后把这一行去除，剩下的矩阵逆时针旋转90度。重复上述动作直到最后矩阵为空，甚至只需要一行代码就可以实现
``` python
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])
```

```
    |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    |7 8 9|      |4 7|
```

```
  spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]
```