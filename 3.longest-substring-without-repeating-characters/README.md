用一个数组来存储遍历过的字符，如果遍历过的字符在数组中，那么数组中这个字符后面的都是不重复的，把在数组中的这个字符以及它前面的都清空，继续遍历，每次遍历记录数组的最大长度

优化：用字典来记录遍历过的字符以及下标，这样可以快速的知道字符是否重复，还需要一个字段 start 记录重复字符下标的下一位，从这里开始字符是不重复的，每次遍历不重复的字符长度就应该等于 i - start + 1

也可以使用[滑动窗口](../76.minimum-window-substring/)的思想来解决这道题