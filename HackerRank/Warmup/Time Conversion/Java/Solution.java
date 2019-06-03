import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the timeConversion function below.
     */
    static String timeConversion(String s) {
        int result = Integer.parseInt(s.substring(0, 2));
        if (s.contains("PM") && result < 12) {
            result += 12;
        }
        else if (s.contains("AM") && result == 12) {
            result = 0;
            s = s.substring(0, 2) + "0" + s.substring(2); 
        }
        else {
            return s.substring(0, 8);
        }
        s = result + "" + s.substring(2);
        return s.substring(0, 8);
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
