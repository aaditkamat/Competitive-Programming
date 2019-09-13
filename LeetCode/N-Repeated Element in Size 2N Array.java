// Title: N-Repeated Element in Size 2N Array
// Runtime: 48 ms
// Memory: 23.3 MB

class Solution {
    public int repeatedNTimes(int[] A) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        for (int i = 0; i < A.length; i++) {
            Integer val = dict.get(A[i]);
            if (val == null) {
                dict.put(A[i], 1);
            } else {
                dict.put(A[i], val + 1);
                if (++val == A.length / 2) {
                    return A[i];
                }
            }
        }
        return -1;
    }
}