import pickle

# Writing data to the file
f2 = "data.pkl"
data = {"name": "seshathri"}

with open(f2, "wb") as file:
    pickle.dump(data, file)

# Reading data from the file
with open(f2, "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
# Read in Binary
with open (f2,"rb") as file:
    f4=file.read()
print(f4)