import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the miniMaxSum function below.
     */
    static void miniMaxSum(int[] arr) {
        long[] newArr = new long[arr.length];
        for (int i = 0; i < newArr.length; i++)
            newArr[i] = arr[i];
        Arrays.sort(newArr);
        long min = newArr[0] + newArr[1] + newArr[2] + newArr[3], 
             max = newArr[1] + newArr[2] + newArr[3] + newArr[4];
        System.out.print(min + " " + max);
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int[] arr = new int[5];

        String[] arrItems = scan.nextLine().split(" ");

        for (int arrItr = 0; arrItr < 5; arrItr++) {
            int arrItem = Integer.parseInt(arrItems[arrItr].trim());
            arr[arrItr] = arrItem;
        }

        miniMaxSum(arr);
    }
}
