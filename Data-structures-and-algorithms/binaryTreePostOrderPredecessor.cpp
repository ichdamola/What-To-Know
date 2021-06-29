// C++ program to find postorder predecessor of
// a node in Binary Tree.
#include <iostream>
using namespace std;

struct Node {
	struct Node *left, *right, *parent;
	int key;
};

Node* newNode(int key)
{
	Node* temp = new Node;
	temp->left = temp->right = temp->parent = NULL;
	temp->key = key;
	return temp;
}

Node* postorderPredecessor(Node* root, Node* n)
{
	// If right child exists, then it is postorder
	// predecessor.
	if (n->right)
		return n->right;

	// If right child does not exist, then
	// travel up (using parent pointers)
	// until we reach a node which is right
	// child of its parent.
	Node *curr = n, *parent = curr->parent;
	while (parent != NULL && parent->left == curr) {
		curr = curr->parent;
		parent = parent->parent;
	}

	// If we reached root, then the given
	// node has no postorder predecessor
	if (parent == NULL)
		return NULL;

	return parent->left;
}

int main()
{
	Node* root = newNode(20);
	root->parent = NULL;
	root->left = newNode(10);
	root->left->parent = root;
	root->left->left = newNode(4);
	root->left->left->parent = root->left;
	root->left->right = newNode(18);
	root->left->right->parent = root->left;
	root->right = newNode(26);
	root->right->parent = root;
	root->right->left = newNode(24);
	root->right->left->parent = root->right;
	root->right->right = newNode(27);
	root->right->right->parent = root->right;
	root->left->right->left = newNode(14);
	root->left->right->left->parent = root->left->right;
	root->left->right->left->left = newNode(13);
	root->left->right->left->left->parent = root->left->right->left;
	root->left->right->left->right = newNode(15);
	root->left->right->left->right->parent = root->left->right->left;
	root->left->right->right = newNode(19);
	root->left->right->right->parent = root->left->right;

	Node* nodeToCheck = root->left->right;

	Node* res = postorderPredecessor(root, nodeToCheck);

	if (res) {
		printf("Postorder predecessor of %d is %d\n",
			nodeToCheck->key, res->key);
	}
	else {
		printf("Postorder predecessor of %d is NULL\n",
			nodeToCheck->key);
	}

	return 0;
}
