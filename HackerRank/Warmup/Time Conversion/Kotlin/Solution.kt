import java.io.*
import java.math.*
import java.text.*
import java.util.*
import java.util.regex.*

/*
 * Complete the timeConversion function below.
 */

fun handleAm(hh: String): String {
    if (hh == "12") 
        return "00";
    return hh;
}

fun handlePm(hh: String): String {
    if (hh != "12") 
        return "${hh.toInt() + 12}";
    return hh;
}

fun timeConversion(s: String): String {
    /*
     * Write your code here.
     */
    var hh = s.split(":")[0];
    val mm = s.split(":")[1];
    val ss = String(charArrayOf(s.split(":")[2][0], s.split(":")[2][1]));
    val amPm = String(charArrayOf(s.split(":")[2][2], s.split(":")[2][3]));
    when(amPm) {
        "AM" -> hh = handleAm(hh);
        "PM" -> hh = handlePm(hh);
    }
    return "${hh}:${mm}:${ss}";
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val s = scan.nextLine()

    val result = timeConversion(s)

    println(result)
}
