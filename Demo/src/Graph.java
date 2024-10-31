import java.util.ArrayList;
import java.util.LinkedList;

class Graph {
    private final int vertices; // Number of vertices
    private final ArrayList<LinkedList<Integer>> adjList; // Adjacency list

    // Constructor
    public Graph(int vertices) {
        this.vertices = vertices;
        adjList = new ArrayList<>(vertices);
        for (int i = 0; i < vertices; i++) {
            adjList.add(new LinkedList<>());
        }
    }

    // Add an edge from source to destination
    public void addEdge(int src, int dest) {
        adjList.get(src).add(dest);
   
    }

    public void printGraph() {
        for (int i = 0; i < vertices; i++) {
            System.out.print(i + ": ");
            for (int dest : adjList.get(i)) {
                System.out.print("-> " + dest + " ");
            }
            System.out.println();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Graph graph = new Graph(5); // Create a graph with 5 vertices

        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);
        graph.addEdge(4, 2);

        System.out.println("Graph adjacency list:");
        graph.printGraph();
    }
}