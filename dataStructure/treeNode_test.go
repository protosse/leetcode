package datastructure

import (
	"testing"
)

func Test_order(t *testing.T) {
	root := &TreeNode{
		Val:   0,
		Left:  &TreeNode{Val: 1, Left: &TreeNode{Val: 3}, Right: &TreeNode{Val: 4}},
		Right: &TreeNode{Val: 2},
	}
	t.Log(preorderTraversalNoRecur(root))
	t.Log(inorderTraversalNoRecur(root))
	t.Log(postorderTraversalNoRecur(root))
}
