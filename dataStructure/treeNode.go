package datastructure

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pop(slice *[]*TreeNode) *TreeNode {
	node := (*slice)[len((*slice))-1]
	*slice = (*slice)[:len((*slice))-1]
	return node
}

// 前序遍历
func preorderTraversal(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Print(root.Val)
	preorderTraversal(root.Left)
	preorderTraversal(root.Right)
}

// 前序非递归
func preorderTraversalNoRecur(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	result := make([]int, 0)
	stack := make([]*TreeNode, 0)
	for root != nil || len(stack) != 0 {
		if root != nil {
			result = append(result, root.Val)
			stack = append(stack, root)
			root = root.Left
		} else {
			node := pop(&stack)
			root = node.Right
		}
	}
	return result
}

// 中序非递归
func inorderTraversalNoRecur(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	result := make([]int, 0)
	stack := make([]*TreeNode, 0)
	for root != nil || len(stack) != 0 {
		if root != nil {
			stack = append(stack, root)
			root = root.Left
		} else {
			node := pop(&stack)
			result = append(result, node.Val)
			root = node.Right
		}
	}
	return result
}

// 后序非递归
func postorderTraversalNoRecur(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	result := make([]int, 0)
	return result
}
