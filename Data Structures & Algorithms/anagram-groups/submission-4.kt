class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val pairs = mutableMapOf<List<Int>, MutableList<String>>()
        
        for (str in strs) {
            val counts = IntArray(26)
            for (c in str) {
                counts[c - 'a']++
            }
            val key = counts.toList()
            pairs.putIfAbsent(key, mutableListOf())
            pairs.getValue(key).add(str)
        }
        
        return pairs.values.toList()
    }
}