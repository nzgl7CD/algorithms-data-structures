public class App {
    public static void main(String[] args) {
        Heap heap = new Heap();
        TreeSet1 treeset=new TreeSet1();

        // Adding elements to the heap
        heap.addElement(10);
        heap.addElement(5);
        heap.addElement(20);
        heap.addElement(15);
        heap.addElement(30);

        treeset.addElement(10);
        treeset.addElement(5);
        treeset.addElement(20);
        treeset.addElement(15);
        treeset.addElement(30);

        // Display the heap contents
        heap.displayHeap();
        treeset.displayTreeSet();

        // // Poll an element (retrieve and remove the smallest element)
        // System.out.println("Polled element: " + heap.pollElement());


        // heap.displayHeap();
    }
}
