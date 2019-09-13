// Title: Reveal Cards In Increasing Order
// Runtime: 77 ms
// Memory: 25.3 MB

class Solution {
    public int[] getOrder(int[] shuffled_deck) {
        int length = shuffled_deck.length;
        if (length <= 2) {
            return shuffled_deck;
        }
        int[] temp = Arrays.copyOfRange(shuffled_deck, length - 2, length);
        List<Integer> store = new LinkedList<>();
        store.add(temp[0]);
        store.add(temp[1]);
        for (int i = length - 3; i >= 0; i--) {
            store.add(0, store.remove(store.size() - 1));
            store.add(0, shuffled_deck[i]);
        }
        return store.stream().mapToInt(i -> i).toArray();
    }
    
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        return getOrder(deck);
    }
}