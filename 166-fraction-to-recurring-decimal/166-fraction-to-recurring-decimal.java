class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator==0){
            return "0";
        }
        StringBuilder sb=new StringBuilder();
        sb.append((numerator>0)^(denominator>0)?"-":"");
        long num=Math.abs((long)numerator);
        long den=Math.abs((long)denominator);

        sb.append(num/den);
        num%=den;
        if (num==0){
            return sb.toString();
        }
        sb.append(".");
        Map<Long,Integer> map= new HashMap<Long,Integer>();
        while (num>0){
            if (map.containsKey(num)){
                int i=map.get(num);
                sb.insert(i,"(");
                sb.append(")");
                break;
            }
            map.put(num,sb.length());
            num*=10;
            sb.append(num/den);
            num%=den;

        }
        return sb.toString();
    }
}