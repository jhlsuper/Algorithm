public class Product extends Date {
    String item;
    String company;
    int price;

    Product(String item, String company, int price, int year, int month, int day) {
        super(year, month, day);
        this.item = item;
        this.company = company;
        this.price = price;


    }

    public void printPro() {
        System.out.println("상품명 : " + item);
        System.out.println("제조사 : " + company);
        System.out.println("가격 : " + price + "원");

    }
}

