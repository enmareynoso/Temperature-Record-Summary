import json
import xml.etree.ElementTree as ET
#this is to format the xml file
import xml.dom.minidom as minidom
from TemperatureSummary import TemperatureSummary

#this are the subclasses of the TemperatureSummary class, here are the implementations for each type of file (flat,xml and json)

class JSONFileTemperatureSummary(TemperatureSummary):
    def parse_data(self):
        with open('sample-files/data.json') as f:
            data = json.load(f)
        return data
    
    def extract_temperatures(self, data):
        temperatures = [measure['temperature'] for measure in data['measures']]
        return temperatures
    
    def write_data(self, min_temp, max_temp, avg_temp):
        data = {'min_temp': min_temp, 'max_temp': max_temp, 'avg_temp': avg_temp}
        with open('sample-files/data.json.out', 'w') as f:
            json.dump(data, f)


class XMLFileTemperatureSummary(TemperatureSummary):
    def parse_data(self):
        tree = ET.parse('sample-files/data.xml')
        root = tree.getroot()
        return root
    
    def extract_temperatures(self, data):
        temperatures = [float(row.find('measure').text) for row in data.findall('row')]
        return temperatures

    def write_data(self, min_temp, max_temp, avg_temp):
        data = {'min_temp': min_temp, 'max_temp': max_temp, 'avg_temp': avg_temp}
        root = ET.Element('temperatures')
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        tree = ET.ElementTree(root)
        xml_str = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(xml_str)
        with open('sample-files/data.xml.out', 'w') as f:
            f.write(reparsed.toprettyxml(indent='  '))


class FlatFileTemperatureSummary(TemperatureSummary):
    def parse_data(self):
        with open('sample-files/data.flat') as f:
            data = f.readlines()
        return data
    
    def extract_temperatures(self, data):
     temperatures = []
    # Skip the header line that was causing value error
     for line in data[1:]:
        temperature = float(line.split('|')[-1])
        temperatures.append(temperature)
        return temperatures

    def write_data(self, min_temp, max_temp, avg_temp):
        data = {'min_temp': min_temp, 'max_temp': max_temp, 'avg_temp': avg_temp}
        with open('sample-files/data.flat.out', 'w') as f:
            for key, value in data.items():
                f.write(f'{key}: {value}\n')