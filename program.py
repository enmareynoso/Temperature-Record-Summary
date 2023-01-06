from sub_classes import JSONFileTemperatureSummary, XMLFileTemperatureSummary,FlatFileTemperatureSummary


# Calculate the temperature summary for data.json and generate data.json.out
JSONProcessor = JSONFileTemperatureSummary()
JSONProcessor.template_method()

# Display the contents of the data.json.out file
with open('sample-files/data.json.out', 'r') as f:
    output = f.read()
    print(f"The summary for the JSON file is: \n {output}")
    print("\n") 

# Calculate the temperature summary for data.xml and generate data.xml.out
XMLProcessor = XMLFileTemperatureSummary()
XMLProcessor.template_method()

# Display the contents of the data.xml.out file
with open('sample-files/data.xml.out', 'r') as f:
    output = f.read()
    print(f"The summary for the XML file is: \n {output}")
    print("\n") 

#Calculate the temperature summary for data.flat and generate data.flat.out file
FLATProcessor = FlatFileTemperatureSummary()
FLATProcessor.template_method()

# Display the contents of the data.flat.out file
with open('sample-files/data.flat.out') as f:
    output = f.read()
    print(f"The summary for the flat file is: \n {output}")