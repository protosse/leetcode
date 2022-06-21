这个题是[303 题](../303.range-sum-query-immutable/)的升级版，同样使用前缀和来解决

先构建 preSum，preSum[i][j]表示的是从 [0,0][0,0] 位置到 [i,j][i,j] 位置的子矩形所有元素之和。

从下图可以看出

```
S(O,D)=S(O,C)+S(O,B)−S(O,A)+D
```

![](https://pic.leetcode-cn.com/1614646493-EriDmE-304.001.jpeg)
那么我们的 preSum 就有如下的递推公式

```
preSum[i][j]=preSum[i−1][j]+preSum[i][j−1]−preSum[i−1][j−1]+matrix[i][j]
```

随后我们再根据 preSum 计算子矩形面积，从下图可以看出

```
S(A,D)=S(O,D)−S(O,E)−S(O,F)+S(O,G)
```

![](https://pic.leetcode-cn.com/1614646585-JOesrN-304.002.jpeg)

假设要求 [row1, col1] 到 [rwo2, col2] 的子矩形面积，用preSum表示就应该是

```
preSum[row2][col2]-preSum[row2][col1-1]-preSum[row1-1][col2]+preSum[row1-1][col1-1] 
```