import java.util.LinkedList;
import java.util.Queue;




class Main {
    public static void main(String[] args) {
        String  a = new String("Hello World!");
        System.out.println(a);        

        Queue<Integer> que = new LinkedList<Integer>();
        for(int i = 0; i <10; i++) {
            que.add(i);
        }
        for(int i = 0; i <5; i++) {
            System.out.println(que.poll());
        }
        System.out.println(que);
    }
}
