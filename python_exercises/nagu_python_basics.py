# creating a list with 0 to 10 numbers
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print(type(my_numbers));
print(my_numbers);

# creating a tuple with first 5 even numbers
my_tuple = (2,4,6,8,10);
print(type(my_tuple));
print(my_tuple);

#creating a set with 1-15
my_unique_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
print(type(my_unique_numbers));
print(my_unique_numbers);

# creating a dictionary
my_info = { "name":"nagu", "age":38, "city":"Hyderabad"};
print(type(my_info));
print(my_info);

# if-else
if(my_info["age"] > 30) :
    print("Nagu is greater than 30.")
    print('His age is : ', my_info['age']);
else:
    print("He is below 30");
    print("his age is : ", my_info["age"]);

# for loop
for i in my_numbers:
    print(i*2);

# while loop
iter = 0;
while iter<=5 :
    print(iter);
    iter=iter+1;