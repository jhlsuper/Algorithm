import java.util.Arrays;

public class MagicEel {
    public static void main(String[] args) {
        solution(2554);
    }
    public static int solution(int storey) {
        int answer = 0;
        String s = String.valueOf(storey);
        String[] strArr = s.split("");
        int[] arr = new int[strArr.length];
        for(int i=0; i<strArr.length; i++){
            arr[i] = Integer.parseInt(strArr[i]);
        }
        int len = arr.length;
        if(storey%10==0){

//            System.out.print(Arrays.toString(strArr));
            for(int i=0; i<strArr.length-1;i++){
//                answer +=Integer.parseInt(strArr[i]);
                answer += arr[i];
            }
        }
        else{
            if(strArr.length==1){
//                answer = Integer.parseInt(strArr[0]);
                answer = arr[0];
            }
            else{

                for(int i=0; i<strArr.length;i++){
                    if(arr[len-i-1]>=6){
                        answer+=10-(arr[len-i-1])+1;
                    }
                    else{
                        answer +=arr[len-i-1];
                    }
                }
            }
        }
        System.out.println(answer);
        return answer;
    }
}
