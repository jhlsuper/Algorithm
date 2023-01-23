import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class B11653 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int temp =2;
        if(M ==1){
            return;
        }
        else{
            while(M!=1){
                if(M%temp ==0){
                    M=M/temp;
                    System.out.println(temp);

                }
                else{
                    temp++;
                }
            }
        }
    }
}
