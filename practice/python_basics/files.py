
try:
    with open("details.txt", "r") as file:
        lines = file.readlines();
        for line in lines:
            print(line);
except FileNotFoundError :
    print("File Not Found");


new_file_obj = open("write_file.txt", "w");
new_file_obj.write("Line1");
new_file_obj.write("line2");
listOfLines = ['Line3',"line4", "line5","line6"];
new_file_obj.writelines(listOfLines);