import java.util.*;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;
public class ExamTest06 {
    public static void main(String[] args) {
        for(int i=0; i<3;i++){
            int computer = (int)(Math.random()*3)+1;
            System.out.println(computer);
        }
    }
    // public static void main(String[] args) {
    // int c_500 = 0;
    // int c_100 = 0;
    // int c_50 = 0;
    // int c_10 = 0;
    // int productPrice = 2340;
    // Scanner sc = new Scanner(System.in);
    // System.out.print("금액을 지불해 주세요 : ");
    // int money = sc.nextInt();
    // sc.nextLine();
    // sc.close();
    // System.out.println("상품의 가격 :" + productPrice);
    // if (money < productPrice) {
    // System.out.println("제품을 구매할 수 없어요");
    // } else if (money == productPrice) {
    // System.out.println("거스름돈이 없습니다.");

    // } else {

    // int left = money - productPrice;
    // System.out.println("거스름돈" + left);
    // while (left != 0) {
    // c_500 = left / 500;
    // left = left - (left / 500) * 500;
    // c_100 = left / 100;
    // left = left - (left / 100) * 100;
    // c_50 = left / 50;
    // left = left - (left / 50) * 50;
    // c_10 = left / 10;
    // left = left - (left / 10) * 10;

    // }
    // if (c_500 != 0) {
    // System.out.printf("500원 %d개,", c_500);
    // }
    // if (c_100 != 0) {
    // System.out.printf("100원 %d개,", c_100);
    // }
    // if (c_50 != 0) {
    // System.out.printf("50원 %d개,", c_50);
    // }
    // if (c_10 != 0) {
    // System.out.printf("10원 %d개", c_10);
    // }
    // }
    // }

//    public static void main(String[] args) {
//        Product ob = new Product("새우깡", "농심", 1200, 2012, 3, 10);
//        ob.printPro();
//        ob.printDate();
//    }


    //        public static void main(String[] args) {
//            Scanner sc = new Scanner(System.in);
//            System.out.print("3자리 정수를 입력하세요 :");
//            String str = sc.nextLine();
//            String[] strArr = new String[str.length()];
//            strArr = str.split("");
//            int answer =0;
//            for(String e :strArr) {
//                answer += Integer.parseInt(e);
//            }
//
//            System.out.println("3자리의 합은 "+answer+"입니다." );
//            sc.close();
//        }

}





