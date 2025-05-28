import java.math.BigInteger;
class Solution {
    static int fun(BigInteger ss, int ti){
        BigInteger tot = BigInteger.ZERO;
        if (ti == 0) return ss.intValue();
        while (!ss.equals(BigInteger.ZERO)) {
            tot = tot.add(ss.mod(BigInteger.TEN));
            ss = ss.divide(BigInteger.TEN);
        }
        return fun(tot,ti-1);
    }
    public int getLucky(String s, int k) {
        int[] a=new int[26];
        for(char x:s.toCharArray()) a[x-'a']++;
        int su=0;
        String st="";
        for(int j=0;j<s.length();j++){
            // for(int i=0;i<26;i++){
            int cc=s.charAt(j)-'a';
            // System.out.println(a[cc]);
            if(a[cc]>=1){
                st+=(cc+1);
                // System.out.println(s.charAt(j));
                a[cc]--;
                }
            // }
        }
        
        // System.out.println(fun(BigInteger.parseBigInteger(st),k));
        BigInteger value = new BigInteger(st, 10);

        return fun(value,k);
    }
}
