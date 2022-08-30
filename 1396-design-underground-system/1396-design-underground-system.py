class UndergroundSystem:

    def __init__(self):
        self.average={}
        self.checkIn_map={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIn_map[id]=[stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # [name_in,time_in] = self.checkIn.pop(id)
        in_info = self.checkIn_map.pop(id)
        in_out=(in_info[0],stationName)
        # [total_hour, total_count]=self.average.pop(in_out,[0,0])
        avr_info=self.average.pop(in_out,[0,0])
        self.average[in_out]=[avr_info[0]+(t-in_info[1]),avr_info[1]+1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        in_out=(startStation,endStation)
        avr_info=self.average[in_out]
        return avr_info[0]/avr_info[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)