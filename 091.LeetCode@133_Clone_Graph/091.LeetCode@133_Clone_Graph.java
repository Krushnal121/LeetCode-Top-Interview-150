class Solution {
    // HashMap to store the cloned nodes
    private Map<Node, Node> clonedNodes = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null)
            return null;

        // If the node has already been cloned, return the cloned node
        if (clonedNodes.containsKey(node)) {
            return clonedNodes.get(node);
        }

        // Clone the node (without neighbors initially)
        Node clonedNode = new Node(node.val);
        clonedNodes.put(node, clonedNode);

        // Clone the neighbors recursively
        for (Node neighbor : node.neighbors) {
            clonedNode.neighbors.add(cloneGraph(neighbor));
        }

        return clonedNode;
    }
}