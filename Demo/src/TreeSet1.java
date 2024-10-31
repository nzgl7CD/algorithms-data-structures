import java.util.TreeSet;

public class TreeSet1 {
    private TreeSet<Integer> treeset;

    public TreeSet1() {
        this.treeset = new TreeSet<>();
        // this.treeset=new TreeSet<>(java.util.Collections.reverseOrder());
    }

    public void addElement(int value) {
        treeset.add(value);
    }

    public void displayTreeSet(){
        System.out.println("Treeset: "+ treeset);
    }

}
