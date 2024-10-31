
import java.util.PriorityQueue;
import java.util.Comparator;

public class Heap {
    private PriorityQueue<Integer> heap;
    private PriorityQueue<Integer> maxHeap;

    public Heap() {
        this.heap = new PriorityQueue<>();
        this.maxHeap=new PriorityQueue<>(Comparator.reverseOrder());
    }

    public void addElement(int value) {
        heap.add(value);
        maxHeap.add(value);
        
    }

    public Integer pollElement() {
        if (!heap.isEmpty()) {
            return heap.poll();

        } else {
            System.out.println("Heap is empty.");
            return null;
        }
    }
    
    public void displayHeap() {
        System.out.println("Min heap: " + heap);
        System.out.println("Max heap: " + maxHeap);
    }
}
