import java.util.*;
public class B2164 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        Queue<Integer> qu = new LinkedList<>();

        for(int i=0; i<N; i++) {
            qu.add(i+1);
        }
        while(qu.size() != 1) {
// System.out.println(qu);
            qu.remove();
            if(qu.size()==1) {
                break;
            }
            int a = qu.poll();
            qu.add(a);
        }

        System.out.printf("%d", qu.poll()) ;
    }
}

