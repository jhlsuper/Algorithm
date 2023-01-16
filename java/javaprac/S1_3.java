package java.javaprac;

import java.util.*;

public class S1_3 {
    // public static void main(String[] args) {
    // MyProfile m = new MyProfile();
    // MyProfile m2 = new MyProfile();
    // System.out.print(m.myName);
    // System.out.print(m2.myName);
    // }
    public static void main(String[] args) {
        System.out.println("가위바위보 게임을 시작합니다. 아래 보기 중 하나를 고르세요");
        System.out.println();
        System.out.println("1. 5판3승");
        System.out.println("2. 3판2승");
        System.out.println("3. 1판1승");
        int player = 0;
        int com = 0;
        int win = 0;
        int count = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("번호를 입력하세요");
        int num = sc.nextInt();
        if (num == 1) {
            win = 3;
            count = 5;
        } else if (num == 2) {
            win = 2;
            count = 3;
        } else {
            win = 1;
            count = 1;
        }
        for (int i = 0; i < count; i++) {
            System.out.print("번호를 입력하세요.");
            int rand = (int) (Math.random() * 3) + 1;
            int temp = sc.nextInt();
            System.out.print("가위바위보 중 하나 입력: ");
            String input = sc.nextLine();
            if (input.equals("가위")) {
                if (rand == 1) {
                    System.out.println("비겼습니다!!!.");
                } else if (rand == 2) {
                    System.out.println("졌습니다!!!.");
                } else if (rand == 3) {
                    System.out.println("이겼습니다!!!.");
                }
            } else if (input.equals("바위")) {
                if (rand == 1) {
                    System.out.println("이겼습니다!!!.");
                } else if (rand == 2) {
                    System.out.println("비겼습니다!!!.");
                } else if (rand == 3) {
                    System.out.println("졌습니다!!!.");
                }

            } else if (input.equals("보")) {
                if (rand == 1) {
                    System.out.println("졌습니다!!!.");
                } else if (rand == 2) {
                    System.out.println("이겼습니다!!!.");
                } else if (rand == 3) {
                    System.out.println("비겼습니다!!!.");
                }

            }
        }

    }
}