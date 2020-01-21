# 트리 구조에서 사용할 노드에 대한 자료형

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
def init_tree():
	global root
		
	new_node = Node("A")
	root = new_node
	
	new_node = Node("B")
	root.left = new_node
	
	new_node = Node("C")
	root.right = new_node
		
	new_node_1 = Node("D")
	new_node_2 = Node("E")
		
	node = root.left # refer to address 
	node.left = new_node_1
	node.right = new_node_2
		
	new_node_1 = Node("F")
	new_node_2 = Node("G")
		
	node = root.right
	node.left = new_node_1
	node.right = new_node_2
	
# 전위순회 알고리즘 (Pre-Order Traverse)
# 가운데 노드를 먼저 방문하고 그 다음에는 왼쪽 노드를 방문하고 그리고 나서 오른쪽 노드를 방문하는 방법
def preorder_traverse(node):
	if node==None: 
		return
	print(node.data, end = ' -> ')
	preorder_traverse(node.left)
	preorder_traverse(node.right)

# 중위순회 알고리즘 (In-Order Traverse)
# 왼쪽 자식 노드를 방문하고 그 다음 부모 노드를 방문한 후 다시 오른쪽 자식 노드를 방문
def inorder_traverse(node):
	if node==None:
		return
	inorder_traverse(node.left)
	print(node.data, end = ' -> ')
	inorder_traverse(node.right)	

# 후위순회 알고리즘 (Post-Order Traverse)
# 왼쪽 자식 노드를 방문하고 다음에 오른쪽 자식 노드를 방문한 후에 마지막으로 부모 노드를 방문하는 알고리즘
def postorder_traverse(node):
	if node==None:
		return
	postorder_traverse(node.left)
	postorder_traverse(node.right)
	print(node.data, end = ' -> ')

# 단계순회 알고리즘 (Level-Order Traverse)
# 루트 노드부터 단계 순서대로 왼쪽부터 오른쪽으로 방문하는 순회 알고리즘 
# 단계 순회 알고리즘의 경우 스택을 사용하기는 어렵고, 큐를 사용하는게 바람직하다. 
levelq = []

def levelorder_traverse(node):
	global levelq
	levelq.append(node)
	
	while len(levelq) != 0:
		# visit
		visit_node = levelq.pop(0)
		print(visit_node.data, end = ' -> ')
		# put child node
		if visit_node.left != None:
			levelq.append(visit_node.left)
		if visit_node.right != None:
			levelq.append(visit_node.right)


# 실행결과
if __name__=='__main__':
	init_tree()	
	
	print("전위순회(Preorder-traverse)")
	preorder_traverse(root)
	
	print("중위순회(Inorder-traverse)")
	inorder_traverse(root)
	
	print("후위순회(Postorder-traverse)")
	postorder_traverse(root)
	
	print("단계 순위 순회 알고리즘(Levelorder-Traverse)")
	levelorder_traverse(root)
	

		
