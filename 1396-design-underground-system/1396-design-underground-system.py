class UndergroundSystem:

    def __init__(self):
        self.average={}
        self.check_in_map={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_map[id]=[stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        [name_in,time_in] = self.check_in_map.pop(id)
        # in_info = self.check_in_map.pop(id)
        in_out=(name_in,stationName)
        [total_hour, total_count]=self.average.pop(in_out,[0,0])
        self.average[in_out]=[total_hour+(t-time_in),total_count+1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        in_out=(startStation,endStation)
        [total_hour, total_count]=self.average[in_out]
        return total_hour/total_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)