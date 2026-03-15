import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

# ---------------- CSS STYLE ----------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020617,#0f172a,#1e293b);
color:white;
font-family: 'Segoe UI', sans-serif;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#0f172a,#1e293b);
border-right:1px solid #334155;
}

section[data-testid="stSidebar"] *{
color:#e2e8f0;
}

h1{color:#f8fafc;}
h2{color:#22c55e;}
h3{color:#f87171;}
h4{color:#34d399;}

[data-baseweb="select"]{
background:#1f2937;
border-radius:10px;
border:1px solid #334155;
}

[data-testid="metric-container"]{
background:linear-gradient(135deg,#4f46e5,#22c55e);
padding:16px;
border-radius:14px;
box-shadow:0px 6px 18px rgba(0,0,0,0.4);
}

img{
border-radius:12px;
box-shadow:0px 6px 18px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

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
"🍽 Meal Plan"
]
)

# ---------------- DATA ----------------

food_list=[
"Spinach","Broccoli","Carrot","Cucumber","Rice","Apple",
"Banana","Milk","Bread","Chicken","Fish","Egg","Yogurt",
"Beans","Oats","Potato","Tomato","Avocado","Orange","Almonds"
]

medicine_list=[
"Warfarin","Aspirin","Metformin","Ibuprofen","Paracetamol",
"Amoxicillin","Atorvastatin"
]

food_interactions={
"Warfarin":{
"avoid":["Spinach","Broccoli","Kale"],
"safe":["Carrot","Cucumber","Rice"]
},
"Aspirin":{
"avoid":["Fish","Garlic"],
"safe":["Apple","Oats","Banana"]
},
"Metformin":{
"avoid":["Sugary Foods"],
"safe":["Beans","Oats","Vegetables"]
}
}

# ---------------- DASHBOARD ----------------

if menu=="🏠 Dashboard":

    col1,col2=st.columns([4,1])

    with col1:
        st.markdown("# 👋 Welcome Manoj")
        st.markdown("### MedGraphX Smart Health Dashboard")

    with col2:
        now=datetime.now()
        st.write("📅",now.strftime("%d %B %Y"))

    st.markdown("---")

    col1,col2,col3=st.columns(3)

    with col1:
        food=st.selectbox("Food",food_list)

    with col2:
        disease=st.selectbox(
        "Disease",
        ["None","Diabetes","Heart Disease","Blood Pressure"]
        )

    with col3:
        medicine=st.selectbox("Medicine",medicine_list)

    st.markdown("---")

    avoid=[]
    safe=[]
    risk="Low"
    risk_color="green"

    if medicine in food_interactions:

        avoid=food_interactions[medicine]["avoid"]
        safe=food_interactions[medicine]["safe"]

        if food in avoid:
            risk="High"
            risk_color="red"

        elif food in safe:
            risk="Low"
            risk_color="green"

        else:
            risk="Medium"
            risk_color="orange"

    else:
        avoid=["No major restrictions"]
        safe=["Apple","Rice","Vegetables"]
        risk="Low"

    st.markdown(
        f"<h3 style='color:{risk_color};font-weight:bold;'>⚠ Risk Level : {risk}</h3>",
        unsafe_allow_html=True
    )

    col1,col2=st.columns(2)

    with col1:
        st.markdown("### ❌ Foods To Avoid")
        for f in avoid:
            st.write(f"• {f}")

    with col2:
        st.markdown("### ✅ Recommended Foods")
        for f in safe:
            st.write(f"• {f}")

    st.markdown("---")

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric("Weight","78 kg","-1.2")

    with col2:
        st.metric("Steps","8050","+340")

    with col3:
        st.metric("Sleep","6.5 hrs","-0.4")

    with col4:
        st.metric("Water Intake","1.3 L","+0.3")

# ---------------- MEDICINE & FOOD SAFETY ----------------

elif menu=="💊 Medicine & Food Safety":

    st.markdown("# 💊 Medicine & Food Safety")

    medicine=st.selectbox("Select Medicine",medicine_list)
    food=st.selectbox("Select Food",food_list)

    st.markdown("---")

    avoid=[]
    safe=[]

    if medicine in food_interactions:
        avoid=food_interactions[medicine]["avoid"]
        safe=food_interactions[medicine]["safe"]

    col1,col2=st.columns(2)

    with col1:
        st.subheader("⚠ Foods To Avoid")
        for f in avoid:
            st.write(f"• {f}")

    with col2:
        st.subheader("✅ Safe Foods")
        for f in safe:
            st.write(f"• {f}")

    st.markdown("---")

    st.subheader("📌 Medicine Tips")

    st.write("• Always take medicines with water")
    st.write("• Avoid alcohol while taking medicines")
    st.write("• Follow doctor prescriptions")

# ---------------- HEALTHY MENU ----------------

elif menu=="🥗 Healthy Menu":

    st.markdown("# 🥗 Healthy Menu")

    col1,col2,col3=st.columns(3)

    with col1:
        st.image("https://images.unsplash.com/photo-1498837167922-ddd27525d352")
        st.write("### Vegetable Salad")
        st.write("Calories: 150 kcal")
        st.write("Protein: 4g")

    with col2:
        st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836")
        st.write("### Healthy Breakfast")
        st.write("Calories: 250 kcal")
        st.write("Protein: 8g")

    with col3:
        st.image("https://images.unsplash.com/photo-1466637574441-749b8f19452f")
        st.write("### Fruit Bowl")
        st.write("Vitamin C Rich")

    st.markdown("---")

    st.subheader("🥑 Superfoods")

    st.write("• Avocado – supports heart health")
    st.write("• Almonds – rich in healthy fats")
    st.write("• Salmon – high Omega-3")
    st.write("• Oats – good for cholesterol")
    st.write("• Yogurt – improves gut health")

    st.markdown("---")

    st.subheader("🍎 Daily Nutrition Tips")

    st.write("• Eat at least 5 servings of fruits and vegetables daily")
    st.write("• Reduce sugar intake")
    st.write("• Include protein in every meal")
    st.write("• Avoid processed foods")

# ---------------- MEAL PLAN ----------------

elif menu=="🍽 Meal Plan":

    st.markdown("# 🍽 Weekly Meal Planner")

    meal_data={
    "Day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "Meal":[
    "Oatmeal with Fruits",
    "Chicken Salad",
    "Vegetable Soup",
    "Grilled Fish",
    "Fruit Bowl",
    "Avocado Toast",
    "Salmon with Vegetables"]
    }

    st.table(pd.DataFrame(meal_data))

    st.markdown("---")

    st.subheader("🥗 Healthy Eating Tips")

    st.write("• Drink 2-3 liters of water daily")
    st.write("• Maintain balanced diet")
    st.write("• Exercise regularly")
    st.write("• Avoid junk food")

    st.markdown("---")

    col1,col2=st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c")
        st.caption("Balanced Diet")

    with col2:
        st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd")
        st.caption("Healthy Lifestyle Foods")