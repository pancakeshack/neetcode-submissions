class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> pairs = new HashMap<>();

        for (var str : strs) {
            int[] counts = new int[26];
            for (char c : str.toCharArray()) {
                counts[c - 'a']++;
            }
            var hash = Arrays.toString(counts);
            pairs.putIfAbsent(hash, new ArrayList<>());
            pairs.get(hash).add(str);
        }

        return new ArrayList<>(pairs.values());
    }
}
