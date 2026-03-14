import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ---------------- SIDEBAR ----------------

st.sidebar.title("🧬 MedGraphX")

st.sidebar.image(
"https://images.unsplash.com/photo-1576091160550-2173dba999ef",
width=300
)

st.sidebar.markdown("### 👤 User Profile")
st.sidebar.write("Name: Manoj")
st.sidebar.write("Goal: Healthy Diet")

st.sidebar.progress(70)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
"Navigation",
[
"🏠 Dashboard",
"💊 Medicine & Food Safety",
"🥗 Healthy Menu",
"🍽 Meal Plan",
"📓 Food Diary",
"🏋 Exercises",
"📊 Progress",
"🧠 Health Insights"
]
)

# ---------------- DASHBOARD ----------------

if menu == "🏠 Dashboard":

    st.title("👋 Welcome Manoj")
    st.subheader("MedGraphX Smart Health Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        weight = 78
        change = -1.2
        arrow = "🔻" if change < 0 else "🔺"
        st.metric("⚖ Weight", f"{weight} kg", f"{arrow} {change}")

    with col2:
        steps = 8050
        change = 340
        arrow = "🔺" if change > 0 else "🔻"
        st.metric("👣 Steps Today", f"{steps}", f"{arrow} {change}")

    with col3:
        sleep = 6.5
        change = -0.4
        arrow = "🔻" if change < 0 else "🔺"
        st.metric("😴 Sleep", f"{sleep} hrs", f"{arrow} {change}")

    with col4:
        water = 1.3
        change = 0.3
        arrow = "🔺" if change > 0 else "🔻"
        st.metric("💧 Water Intake", f"{water} L", f"{arrow} {change}")

    st.markdown("---")

    st.subheader("📊 Daily Health Activity")

    data = {
        "Activity":["Steps","Calories Burn","Hydration","Sleep"],
        "Progress":[80,60,50,70]
    }

    df = pd.DataFrame(data)

    st.bar_chart(df.set_index("Activity"))

# ---------------- MEDICINE SAFETY ----------------

elif menu == "💊 Medicine & Food Safety":

    st.title("💊 Medicine & Food Interaction Checker")

    medicine = st.selectbox(
        "Select Medicine",
        ["Warfarin","Aspirin","Metformin","Ibuprofen","Paracetamol","Amoxicillin"]
    )

    medicine_data = {

        "Warfarin":{
            "avoid":["Spinach","Broccoli","Kale"],
            "safe":["Carrot","Cucumber","Rice"],
            "reason":"Vitamin K foods reduce blood thinning effect."
        },

        "Aspirin":{
            "avoid":["Alcohol","Spicy food","Fried food"],
            "safe":["Banana","Yogurt","Oatmeal"],
            "reason":"Spicy foods may irritate stomach."
        },

        "Metformin":{
            "avoid":["Sugary drinks","Candy"],
            "safe":["Whole grains","Vegetables","Nuts"],
            "reason":"Healthy fiber helps control diabetes."
        },

        "Ibuprofen":{
            "avoid":["Alcohol"],
            "safe":["Milk","Bread","Banana"],
            "reason":"Taking with food protects stomach."
        },

        "Paracetamol":{
            "avoid":["Alcohol"],
            "safe":["Light meals","Soup"],
            "reason":"Alcohol may damage liver."
        },

        "Amoxicillin":{
            "avoid":["Alcohol","Acidic drinks"],
            "safe":["Yogurt","Fruit"],
            "reason":"Probiotic foods restore gut bacteria."
        }

    }

    data = medicine_data[medicine]

    col1,col2 = st.columns(2)

    with col1:
        st.error("❌ Foods To Avoid")
        for food in data["avoid"]:
            st.write("•",food)

    with col2:
        st.success("✅ Recommended Foods")
        for food in data["safe"]:
            st.write("•",food)

    st.info("ℹ Reason: "+data["reason"])

    st.markdown("---")

    st.subheader("🩺 Diet Suggestions For Health Issues")

    issue = st.selectbox(
    "Select Health Issue",
    ["Diabetes","High Blood Pressure","Fever","Cold","Heart Health"]
    )

    issue_food = {

    "Diabetes":["Whole grains","Leafy vegetables","Nuts","Beans"],

    "High Blood Pressure":["Banana","Spinach","Low salt foods"],

    "Fever":["Soup","Coconut water","Fruit juices"],

    "Cold":["Ginger tea","Honey","Warm soup"],

    "Heart Health":["Oats","Avocado","Olive oil"]
    }

    st.success("Recommended Foods")

    for food in issue_food[issue]:
        st.write("•",food)

# ---------------- HEALTHY MENU ----------------

elif menu == "🥗 Healthy Menu":

    st.title("🥗 Healthy Food Suggestions")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.image("https://images.unsplash.com/photo-1498837167922-ddd27525d352")
        st.subheader("Vegetable Salad")
        st.write("Calories: 150 kcal")
        st.write("Protein: 4g")
        st.caption("Rich in vitamins and antioxidants")

    with col2:
        st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836")
        st.subheader("Healthy Breakfast Bowl")
        st.write("Calories: 250 kcal")
        st.write("Protein: 8g")
        st.caption("High protein fiber meal")

    with col3:
        st.image("https://images.unsplash.com/photo-1466637574441-749b8f19452f")
        st.subheader("Fruit Nutrition Bowl")
        st.write("Calories: 180 kcal")
        st.write("Protein: 3g")
        st.caption("Natural energy and hydration")

    st.success("Healthy foods improve recovery when taking medications.")

# ---------------- MEAL PLAN ----------------

elif menu == "🍽 Meal Plan":

    st.title("🍽 Weekly Meal Planner")

    meal_data = {
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Meal":["Oatmeal","Chicken Salad","Vegetable Soup","Grilled Fish","Fruit Bowl"]
    }

    st.table(pd.DataFrame(meal_data))

# ---------------- FOOD DIARY ----------------

elif menu == "📓 Food Diary":

    st.title("📓 Food Diary")

    food = st.text_input("Enter food you ate today")

    if st.button("Add Entry"):
        st.success(food+" added to diary")

# ---------------- EXERCISES ----------------

elif menu == "🏋 Exercises":

    st.title("🏋 Recommended Exercises")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.image("https://images.unsplash.com/photo-1594737625785-cf0cbd5b7a0b")
        st.write("Brisk Walking")
        st.caption("30 minutes cardio exercise")

    with col2:
        st.image("https://images.unsplash.com/photo-1517836357463-d25dfeac3438")
        st.write("Dumbbell Squats")
        st.caption("Strength training for legs")

    with col3:
        st.image("https://images.unsplash.com/photo-1599058917765-a780eda07a3e")
        st.write("Stretching")
        st.caption("Improves flexibility")

# ---------------- PROGRESS ----------------

elif menu == "📊 Progress":

    st.title("📊 Weekly Progress")

    st.write("Steps Goal Completion")
    st.progress(75)

    st.write("Workout Completion")
    st.progress(60)

# ---------------- HEALTH INSIGHTS ----------------

elif menu == "🧠 Health Insights":

    st.title("🧠 Health Insights")

    st.warning("Always check food interactions before taking medication.")

    st.success("Balanced meals improve medication effectiveness.")

    st.info("Drink enough water and avoid mixing unknown foods with medicines.")