class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Integer, List<String>> pairs = new HashMap<>();

        for (var str : strs) {
            int[] counts = new int[26];
            for (int i = 0; i < str.length(); i++) {
                var pos = str.charAt(i) - 'a';
                counts[pos]++;
            }
            var hash = Arrays.hashCode(counts);
            var list = pairs.getOrDefault(hash, new ArrayList<>());
            list.add(str);
            pairs.put(hash, list);
        }

        return new ArrayList<>(pairs.values());
    }
}
