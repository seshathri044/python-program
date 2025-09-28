driver_name="Seshathri_M"
#Basic
print(driver_name.lower())#seshathri_m
print(driver_name.upper())#SESHATHRI_M
print(driver_name.capitalize())#Seshathri_M

#UseCase 1// hiding mobile number 
mobile ="9999999998"
masked = mobile[:2]+ "******"+ mobile[-2:] # 99******98
print(masked)

#UseCase 2// Capitalize only first letter
song = "shape OF you"
artist ="SESHATHRI m"
formatted = f"{song.title()} - {artist.title()}"#Shape Of You - Seshathri M
print(formatted)

#UseCase 3 //Change the fixed location
location = "chennai central"
fixed_location = location.replace("chennai central","Thambaram")# Thambaram
print(fixed_location)

#UseCase 4 // Get the booking id 
message ="Your uber booking id is: UB12345.Please keep it safe"
booking_id= message.split(":")[1].split(".")[0] #// first split- UB12345.Please keep it safe// second split- UB12345
print(booking_id)

#UseCase 5 #in this sentence if it see zomato100 then need to print if block 
promo_msg ="use zomato100 to get 100 off on your first order"
if "zomato100" in promo_msg:
    print("offer applied")

#UseCase 6 # using find help to identify the position 
feedback ="the driver was polite and the ride was smooth"
print("position is:", feedback.find("polite"))

#UseCase 7 # In this two word only l and z need to be capitalized
name="luffy zoro"
initials= "".join([word[0].upper() for word in name.split()])
print(initials)

#UseCase 8 # IN this empty space are removed
dirt_input ="     airport     "
clean = dirt_input.strip()
print(clean)

#UseCase 9
word1 = " luffy is the Captain of Straw hat pirate"
word_count = len(word1.split())
print(word_count)