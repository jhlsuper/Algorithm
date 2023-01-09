import java.util.*;
public class B1343 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String answer ="";
        String A = "AAAA", B = "BB";
        String a = sc.nextLine();
        sc.close();
        String[] arr = a.split("");  //String 배열에 넣는법
//        System.out.println(a);
        a =  a.replaceAll("XXXX",A);
        answer = a.replaceAll("XX",B);

        if(answer.contains("X")){
            answer ="-1";
        }
        System.out.println(answer);
    }
}
