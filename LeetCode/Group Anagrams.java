// Title: Group Anagrams
// Runtime: 69 ms
// Memory: 46.8 MB

import java.util.Vector;

class Solution {
    public HashMap<Character, Integer> toMap(String str) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (map.get(ch) == null) {
                map.put(ch, 1);
            } else {
                map.put(ch, map.get(ch) + 1);
            }
        }
        return map;
    }
    
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>, Vector<String>> mapOfMaps = new HashMap<>();
        if (strs.length == 0)
            return new Vector<List<String>>();
        HashMap<Character, Integer> map = toMap(strs[0]);
        Vector<String> group = new Vector<>();
        group.add(strs[0]);
        mapOfMaps.put(map, group);
        for (int i = 1; i < strs.length; i++) {
            map = toMap(strs[i]);
            group = mapOfMaps.get(map);
            if (group != null) {
                group.add(strs[i]);
                mapOfMaps.put(map, group);
            } else {
                group = new Vector<>();
                group.add(strs[i]);
                mapOfMaps.put(map, group);
            }
        }
        List<List<String>> groups = new Vector<>();
        for (Map.Entry<HashMap<Character, Integer>, Vector<String>> iter_group: mapOfMaps.entrySet()) {
            groups.add(iter_group.getValue());
        }
        return groups;
    }
}