class Solution {
    public int[] findOrder(int n, int[][] prerequisites) {
        int[] sortedOrder = new int[n];
        int index = 0;
        // if n is smaller than or equal to zero we will return the empty array
        if (n <= 0)
            return new int[0];

        // Store the count of incoming prerequisites in a hashmap
        HashMap<Integer, Integer> inDegree = new HashMap<>();
        // a. Initialize the graph
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            inDegree.put(i, 0);
            graph.put(i, new ArrayList<Integer>());
        }

        // b. Build the graph
        for (int i = 0; i < prerequisites.length; i++) {
            int parent = prerequisites[i][1], child = prerequisites[i][0];
            graph.get(parent).add(child); // put the child into it's parent's list
            inDegree.put(child, inDegree.get(child) + 1); // increment child's inDegree
        }

        // c. Find all sources i.e., all n with 0 in-degrees
        Queue<Integer> sources = new LinkedList<>();
        // traverse in inDegree using key
        for (Map.Entry<Integer, Integer> entry : inDegree.entrySet()) {
            if (entry.getValue() == 0)
                sources.add(entry.getKey());
        }

        // d. For each source, add it to the sortedOrder and subtract one from all of
        // its children's in-degrees
        // if a child's in-degree becomes zero, add it to the sources queue
        while (!sources.isEmpty()) {
            // pop an element from the start of the sources and store
            // the element in vertex
            int vertex = sources.poll();
            // append the vertex at the end of the sorted_order
            sortedOrder[index++] = vertex;
            List<Integer> children = graph.get(vertex); // get the node's children to decrement their in-degrees
            // traverse in graph[vertex] using child
            // get the node's children to decrement
            // their in-degrees
            for (int child : children) {
                inDegree.put(child, inDegree.get(child) - 1);
                // if inDegree[child] is 0 append the child in the deque sources
                if (inDegree.get(child) == 0)
                    sources.add(child);
            }
        }

        if (index != n) // topological sort is not possible as the graph has a cycle
            return new int[0];

        return sortedOrder;
    }
}