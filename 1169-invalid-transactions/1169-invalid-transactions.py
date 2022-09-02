class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_map = defaultdict(set)
                
        invalid = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)            
            transaction_map[(time, name)].add(city)
                    
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            
            if amount > 1000:
                invalid.append(transaction)
                continue
            
            # check to see if there is a time within 60 minutes of this transaction
            for time in range(time-60, time+61):
                if (time, name) not in transaction_map:
                    continue
                sus_transaction = transaction_map[(time, name)]
                
                # check to see if there is another transaction from a diff city if so its invalid
                if city in sus_transaction:
                    sus_transaction.remove(city)
                    if len(sus_transaction) >= 1:
                        invalid.append(transaction)
                        break
                    sus_transaction.add(city)
                else:
                    invalid.append(transaction)
                    break
                                        
        return invalid 