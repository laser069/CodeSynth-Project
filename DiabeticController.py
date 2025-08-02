import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyDfIbEFplrw1O0t4ze56ovUF7p8UCAA63U")
model = genai.GenerativeModel("gemini-1.5-flash")

Name = input("Your Name:")
Age = int(input("Age:"))
Gender =input("Gender:")
BMI = int(input("BMI:"))
Glucose = int(input("Glucose:"))
BloodPressure = int(input("Blood Pressure: "))

model.generate_content(f"My Name is {Name},I am {Age},My Gender is{Gender},BMI:{BMI},BloodPressure:{BloodPressure}")

CronicDiseases = input("Any Diseases:")
if CronicDiseases.strip() == "":
    CronicDiseases = "Null"

outputformat = '''
{
    "BMR":
    "pre-breafast":{
    ..
    },
  "breakfast": {
    "calories": 

  },
  post-breakfast:{
  ..
  },

  "lunch": {
    "calories":

  },
  "post_lunch":{
    ..
  }
  "snacks":{
  }
  "dinner": {
    "calories": 

  }
  "post-dinner":{
  ..
  }
}
'''

response = model.generate_content(f'''Details of a person:
Glucose: {Glucose}
BloodPressure: {BloodPressure}
BMI: {BMI}
Age: {Age}
Gender: {Gender}
 act as a nutrition tracker
 calculate  (Basal Metabolic Rate)
 mind the cronic disease and calculate BMR and give data accordingly

  calorie intake per meal with the (pre-breakfast,breakfast,post-breakfast,lunch,snacks,dinner break the calories in calculated bmr into 3 meals in json format)
Breakfast: 20-30% of daily calories

Lunch: 30-35% of daily calories

Dinner: 25-30% of daily calories

Others: 5-15% of daily calories
        
              for a person this age, glucose,blood pressure,BMI (only output calorie,if the inputs are legit) dont add comments in the output Format:{outputformat}''')
print(response.text)
part1, part2 = response.text.split("```json", 1)

result = part2.split("```", 1)[0]



with open('Recommended.json', 'w') as f:
    f.write(result)


with open("Recommended.json","r") as food_data:
    data = json.load(food_data)


pre_breakfast = input("pre-breakfast")
breakfast = input("BreakFast:")
post_breakfast = input("post_breakfast:")
lunch = input("Lunch:")
post_lunch = input("Post Lunch:")
snacks = input("Snacks:")
dinner = input("Dinner:")
post_dinner = input("Post dinner:")
food_format = '''

    {
      "Food time":post_breakfast
      "item": "milk",
      "calories": 100
    },

'''
food_response = model.generate_content(f'''
    Calculate Calories for the following:
    {pre_breakfast}
    {breakfast}
    {post_breakfast}
    {lunch}
    {post_lunch}
    {snacks}
    {dinner}
    {post_dinner}
    give them in json format :{food_format}with no comments

''')



part1, part2 = food_response.text.split("```json", 1)

# Split the second part based on the end delimiter
result = part2.split("```", 1)[0]


raw_data = json.dumps(food_response.text)
with open('food_data.json', 'w') as f:
    f.write(result)


