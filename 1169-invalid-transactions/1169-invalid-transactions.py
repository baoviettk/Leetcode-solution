class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = {}
        result = set()
        for i, t in enumerate(transactions):
            name, time, amount, city =  t.split(",")
            if name not in hashmap:
                hashmap[name] = []
                if int(amount) > 1000:
                    result.add(i)
            else:
                prevTrans = hashmap[name]
                for j in range(len(prevTrans)):
                    prevName, prevTime, prevAmount, prevCity = transactions[prevTrans[j]].split(",")
                    if int(amount) > 1000:
                        result.add(i)
                    if abs(int(time) - int(prevTime)) <= 60 and city != prevCity:
                        result.add(i)
                        result.add(prevTrans[j]) 
            hashmap[name].append(i)
   
        return [transactions[t] for t in result]