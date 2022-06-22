list=['Model', 'Year', 'Category', 'Rating', 'Displacement', 'Engine type', 'Power', 'Top speed', 'Fuel system', 'Cooling system', 'Gearbox', 'Transmission type', 'Clutch', 'Fuel consumption', 'Greenhouse gases', 'Frame type', 'Front suspension', 'Rear suspension', 'Front tire', 'Rear tire', 'Front brakes', 'Rear brakes', 'Dry weight', 'Power/weight ratio', 'Seat height', 'Overall height', 'Overall length', 'Overall width', 'Wheelbase', 'Fuel capacity', 'Color options', 'Starter', 'Factory warranty', 'Comments', 'Update specs', 'Insurance costs', 'Finance options', 'Parts finder', 'Maintenance', 'Ask questions', 'Related bikes']

for i in list:
    print("elif(i=='"+i.replace(" ","_").replace("/","_").capitalize()+"'):")
    print("    obj."+i.replace(" ", "_").replace("/", "_").capitalize()+"=i")
