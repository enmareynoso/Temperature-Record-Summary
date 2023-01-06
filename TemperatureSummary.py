from abc import ABC, abstractmethod

#this is the base class
class TemperatureSummary(ABC):
    def template_method(self):
          # Process the data and generate the output file
        data = self.parse_data()
        min_temp, max_temp, avg_temp = self.process_data(data)
        self.write_data(min_temp, max_temp, avg_temp)


    @abstractmethod
    def parse_data(self):
        # Reads and parses the data from the file
        pass

    def process_data(self, data):
        # Takes the temperature measures from the data and calculates the minimum, maximum, and average temperature
        temperatures = self.extract_temperatures(data)
        min_temp = min(temperatures)
        max_temp = max(temperatures)
        avg_temp = sum(temperatures) / len(temperatures)
        return min_temp, max_temp, avg_temp

    @abstractmethod
    def extract_temperatures(self, data):
        # Extracts the temperature measures from the data and returns a list of temperatures
        pass

    @abstractmethod
    def write_data(self, min_temp, max_temp, avg_temp):
        # Writes the minimum, maximum, and average temperature measures to a file
        pass



