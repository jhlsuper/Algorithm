import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.*;

public class B10866 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Deque<Integer> de = new ArrayDeque<>();

        for (int i=0; i<N;i++) {
            String a = sc.nextLine();
            String[] aa = a.split(" ");
// System.out.println(Arrays.toString(aa));
            if(aa.length==2) {
                if(aa[0].equals("push_front")) {
                    de.addFirst(Integer.parseInt(aa[1]));
                }
                else {
                    de.addLast(Integer.parseInt(aa[1]));
                }

            }
            else {
// System.out.println((de) );
                if(aa[0].equals("pop_front")){
                    if(de.size() ==0) {

                        System.out.printf("%d\n", -1);
                    }
                    else {
                        System.out.printf("%d\n", de.pollFirst());
                    }
                }
                else if(aa[0].equals("pop_back")) {
                    if(de.size()==0) {
                        System.out.printf("%d\n", -1);
                    }
                    else {
                        System.out.printf("%d\n", de.pollLast());
                    }
                }
                else if(aa[0].equals("size")) {
                    System.out.printf("%d\n", de.size());
                }
                else if(aa[0].equals("empty")) {
                    if(de.isEmpty()) {
                        System.out.printf("%d\n", 1);
                    }
                    else{
                        System.out.printf("%d\n", 0);
                    }
                }
                else if(aa[0].equals("front")) {
// System.out.println("its called ^^");
                    if(de.size()==0) {
                        System.out.printf("%d\n", -1);
                    }
                    else {
                        System.out.printf("%d\n", de.getFirst());
                    }
                }
                else if(aa[0].equals("back")) {
                    if(de.size()==0) {
                        System.out.printf("%d\n", -1);
                    }
                    else {
                        System.out.printf("%d\n", de.getLast());
                    }
                }

            }
        }
    }
}
