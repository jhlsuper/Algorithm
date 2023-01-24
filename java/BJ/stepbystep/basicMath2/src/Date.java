public class Date {
    int year;
    int month;
    int day;

    public Date(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public void printDate() {
        System.out.println("제조일 : " + this.year + "/" + this.month + "/" + this.day);

    }
}