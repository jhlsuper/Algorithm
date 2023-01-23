import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class B9020 {
    public static boolean[] prime;

    public static void main(String[] args) throws IOException {
        prime = new boolean[10001];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        get_prime();

        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < prime.length; i++) {
            if (prime[i] == false) {
                arr.add(i);

            }
        }
//        for(int e : arr){
//            System.out.printf("%d ", e);
//        }

        for(int i=0; i<T;i++){
            int n = Integer.parseInt(br.readLine());

            int x=0;
            int y =0;
//            System.out.println(arr.size());
            for(int a=0; a<arr.size(); a++){
                if(n-arr.get(a)>0 ){
                    if(prime[n-arr.get(a)]==false && arr.get(a)<=n-arr.get(a)){
//                        System.out.printf("%d %d \n",arr.get(a), n-arr.get(a));
                        x = arr.get(a);
                        y = n- arr.get(a);
                    }
                }

            }
            System.out.printf("%d %d\n",x,y);
        }
    }

    public static void get_prime() {
        prime[0] = prime[1] = true;
        for (int i = 2; i < Math.sqrt(prime.length); i++) {
            if (prime[i]) continue;
            for (int j = i * i; j < prime.length; j += i) {
                prime[j] = true;
            }
        }
    }
}
