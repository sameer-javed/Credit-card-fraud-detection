import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
import streamlit as st

# Loading the data
CC_df = pd.read_csv(r"B:\Desktop\excel work\Excel file\creditcard.csv")

# Getting legit and fraud data
legit = CC_df[CC_df["Class"] == 0]
fraud = CC_df[CC_df["Class"] == 1]


# Balancing legit and fraud data
legit_sample = legit.sample(n=492,random_state=2)
cc_df2 =  pd.concat([legit_sample,fraud], axis = 0)


# Creating training and testing variables
X = cc_df2.drop(columns={'Class'})
Y = cc_df2['Class']
X_train , X_test , Y_train , Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y,random_state=10)


# inplementing into model
model = LogisticRegression()
model.fit(X_train,Y_train)

# Evaluate models performance
train_acc = accuracy_score(model.predict(X_train),Y_train)
test_acc = accuracy_score(model.predict(X_test),Y_test)


# Web App 
# st.title("Credit Card Fraud Detection")
# input_df = st.text_input('Input All Required Features: ')
# input_df_ls = input_df.split(',')

# submit = st.button("Submit")

# if submit:

#     features = np.asarray(input_df_ls, dtype=np.float64)
#     prediction = model.predict(features.reshape(1,-1))

#     if prediction[0] == 0:
#         st.write("Legitimate Transaction")
#     elif prediction[0] == 1:
#         st.write("Fraudulent Transaction")
#     else:
#         st.write("Invalid Input")



# # Title with enhanced style
# st.title("💳 Credit Card Fraud Detection App")

# # Input box for entering features
# st.markdown("<h3 style='color:blue;'>Please Enter All Required Features:</h3>", unsafe_allow_html=True)
# input_df = st.text_input('Input All Required Features (comma separated): ')
# input_df_ls = input_df.split(',')

# # Add some spacing
# st.markdown("<br>", unsafe_allow_html=True)

# # Submit button with custom style
# submit = st.button("🔍 Check Transaction")

# if submit:
#     try:
#         # Convert input list to numpy array
#         features = np.asarray(input_df_ls, dtype=np.float64)

#         # Assuming model is preloaded
#         prediction = model.predict(features.reshape(1, -1))

#         # Styling for the output
#         if prediction[0] == 0:
#             st.markdown("<h3 style='color:green;'>✅ Legitimate Transaction</h3>", unsafe_allow_html=True)
#         elif prediction[0] == 1:
#             st.markdown("<h3 style='color:red;'>⚠️ Fraudulent Transaction Detected!</h3>", unsafe_allow_html=True)
#         else:
#             st.markdown("<h3 style='color:orange;'>❌ Invalid Input</h3>", unsafe_allow_html=True)

#     except ValueError:
#         st.markdown("<h3 style='color:red;'>❌ Invalid input format. Please enter valid numbers.</h3>", unsafe_allow_html=True)
#     except Exception as e:
#         st.markdown(f"<h3 style='color:red;'>⚠️ Error: {str(e)}</h3>", unsafe_allow_html=True)

# # Footer or additional information
# st.markdown("<br><br><hr><center>🛡️ Developed for secure transactions detection</center>", unsafe_allow_html=True)


# # Title with enhanced style
# st.title("💳 Credit Card Fraud Detection App")

# # Section with example data for users who don't have input data
# st.markdown("<h3 style='color:blue;'>Example Input Data:</h3>", unsafe_allow_html=True)
# example_data = "5000, 20, 2, 3, 1, 0"  # Example input data (you can modify as needed)
# st.text_area("Example Data", example_data)

# # Button to autofill the input box with example data
# if st.button("Use Example Data"):
#     input_df = example_data
# else:
#     input_df = st.text_input('Input All Required Features (comma separated): ')

# input_df_ls = input_df.split(',')

# # Add some spacing
# st.markdown("<br>", unsafe_allow_html=True)

# # Submit button with custom style
# submit = st.button("🔍 Check Transaction")

# if submit:
#     try:
#         # Convert input list to numpy array
#         features = np.asarray(input_df_ls, dtype=np.float64)

#         # Assuming model is preloaded
#         prediction = model.predict(features.reshape(1, -1))

#         # Styling for the output
#         if prediction[0] == 0:
#             st.markdown("<h3 style='color:green;'>✅ Legitimate Transaction</h3>", unsafe_allow_html=True)
#         elif prediction[0] == 1:
#             st.markdown("<h3 style='color:red;'>⚠️ Fraudulent Transaction Detected!</h3>", unsafe_allow_html=True)
#         else:
#             st.markdown("<h3 style='color:orange;'>❌ Invalid Input</h3>", unsafe_allow_html=True)

#     except ValueError:
#         st.markdown("<h3 style='color:red;'>❌ Invalid input format. Please enter valid numbers.</h3>", unsafe_allow_html=True)
#     except Exception as e:
#         st.markdown(f"<h3 style='color:red;'>⚠️ Error: {str(e)}</h3>", unsafe_allow_html=True)

# # Footer or additional information
# st.markdown("<br><br><hr><center>🛡️ Developed for secure transactions detection</center>", unsafe_allow_html=True)



# Title with enhanced style
st.title("Credit Card Fraud Detection App")
st.title('💳')

# Input box for entering features
st.markdown("<h3 style='color:blue;'>Enter Your Input Data:</h3>", unsafe_allow_html=True)
input_df = st.text_input('Input All Required Features (comma separated):')

# Split the input into a list of features
input_df_ls = input_df.split(',')

# Submit button with custom style
submit = st.button("🔍 Check Transaction")

if submit:
    try:
        # Convert input list to numpy array
        features = np.asarray(input_df_ls, dtype=np.float64)

        # Assuming model is preloaded
        prediction = model.predict(features.reshape(1, -1))

        # Styling for the output
        if prediction[0] == 0:
            st.markdown("<h3 style='color:green;'>✅ Legitimate Transaction</h3>", unsafe_allow_html=True)
        elif prediction[0] == 1:
            st.markdown("<h3 style='color:red;'>⚠️ Fraudulent Transaction Detected!</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color:orange;'>❌ Invalid Input</h3>", unsafe_allow_html=True)

    except ValueError:
        st.markdown("<h3 style='color:red;'>❌ Invalid input format. Please enter valid numbers.</h3>", unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"<h3 style='color:red;'>⚠️ Error: {str(e)}</h3>", unsafe_allow_html=True)

# Example data section (showing pre-defined input examples)
st.markdown("<h3 style='color:blue;'>Example Input Data:</h3>", unsafe_allow_html=True)

# Example input data, providing 10 to 20 sample inputs as comma-separated values
example_data = """1st example Input \n
157494,0.063874553,0.389685239,1.259622569,0.828357062,-0.108208732,1.033438343,-0.264416431,0.31954552,-0.163201739,0.157694032,0.312819247,0.159510445,-0.004187737,0.059653133,0.991690728,-0.437695543,0.083359429,1.223178825,2.945979901,0.346218436,0.289471004,0.99154231,-0.130143687,0.363557292,-0.715818529,0.951479104,0.192853575,0.179328828,28.75\n
2nd example Input \n
7535,0.026779226,4.132463897,-6.560599968,6.348556673,1.329665669,-2.513478848,-1.6891022,0.303252801,-3.139409057,-6.045467798,6.754625448,-8.948178579,0.702724998,-10.7338541,-1.379519857,-1.638960115,-1.746350136,0.776744098,-1.327356635,0.587743219,0.370508651,-0.576752473,-0.669605372,-0.75990753,1.60505555,0.540675396,0.737040382,0.496699108,1\n
3rd example Input \n
79242,1.183994578,-0.44807862,0.768094951,-0.969185305,-0.794956763,0.160657893,-0.752546995,0.266971843,1.563054879,-0.957999299,1.20747151,1.467886128,0.027138971,0.033541787,0.835002662,-0.448181766,-0.243188054,0.32716021,0.610123682,-0.128406223,0.046717489,0.390121876,-0.060567333,-0.281072496,0.444974853,-0.654362116,0.106635843,0.018623271,1\n
4th example Input \n
11092,0.378274504,3.914796789,-5.726872015,6.094140959,1.698875264,-2.807313947,-0.591118213,-0.123495593,-2.530712814,-5.15309461,4.654088423,-7.839538998,1.37181858,-9.634689713,-0.739596856,-0.663203946,0.891934541,0.978675639,-2.005476603,0.440439441,0.149895683,-0.601967246,-0.613724336,-0.403113688,1.568445256,0.521883934,0.52793775,0.411910406,1\n
5th example Input \n
155288,0.189727867,-3.389540139,-1.93483047,0.593070766,-0.310143575,2.111224241,0.396798176,0.383007572,0.827281898,-0.432787456,0.719322833,1.00699121,-0.282058407,0.380588898,0.147765322,-0.24114562,0.112277637,-1.204097022,-0.527651818,1.525508959,0.178944942,-1.305701928,-0.267148101,-0.932573051,-1.100856295,0.133896364,-0.172111115,0.084995705,888.61\n
6th example Input \n
11131,-1.426623313,4.141986232,-9.804103442,6.666273003,-4.749526793,-2.073129006,-10.08993116,2.791345299,-3.249515617,-11.42045097,10.85301165,-15.96920752,0.546690085,-14.69072913,0.9123374,-12.22718928,-18.58736621,-6.920761861,3.166998907,1.410677653,1.865678768,0.407809282,0.605809354,-0.769348118,-1.746336829,0.502039517,1.97725833,0.711606531,1\n
7th example Input \n
31029,-4.239697545,2.719970505,0.080645857,-0.260728291,-1.127608908,-0.356352636,0.010576631,0.339323501,1.595508308,1.919936239,-1.430729067,-0.768672983,-1.723495129,-0.279105248,0.045990457,-0.364806975,0.124366644,-0.331790489,0.615144616,-0.270131718,-0.215800585,-0.526524123,-0.189470049,-0.000286475,0.223106389,-0.070679887,-3.975735197,-1.796222385,13.92\n
8th example Input \n
12093,-4.696795224,2.693867479,-4.475132713,5.467684549,-1.556758075,-1.549420289,-4.104214873,0.553934075,-1.498468131,-4.594951763,5.275505851,-11.34902855,0.374549235,-8.138694884,0.548570894,-6.653594347,-10.24675541,-4.191066267,0.991486122,-0.158970549,0.573898081,-0.080162775,0.318407817,-0.245862203,0.338238432,0.032270621,-1.508457934,0.608074683,0\n
9th example Input \n
141521,1.642553682,-0.06775083,-0.853478327,3.999156486,0.329187273,0.518731833,0.211837997,0.051751477,-0.647546436,1.426959125,-0.401795372,0.392711893,-0.66121782,0.113509668,-3.015716979,0.325363598,-0.53026592,-0.061078049,-0.712166887,-0.079215141,0.161733992,0.439325822,-0.149252133,-0.320311945,0.262189758,0.178509341,-0.057448394,-0.049253218,131.99\n
10th example Input \n
12393,-4.064004738,3.100934891,-1.188498004,3.26463274,-1.903562358,0.320350587,-0.954940039,-3.27753492,2.820828662,1.01511288,3.187186897,-7.004327284,0.872710605,-6.220605353,-0.90444463,-3.075091885,-5.044735692,-1.718082685,-0.662462068,-0.531897693,1.688665431,-0.078844698,0.193730927,0.479495954,-0.506603057,-0.409862744,-3.036271329,-0.630605199,179.66\n
11th example Input \n
165842,2.090906678,0.029476545,-2.205431873,-0.14393492,0.670140496,-1.123926548,0.623794859,-0.351002598,0.016145524,0.198986496,0.990860926,0.609000541,-0.751662029,1.115581974,-0.223799608,-0.405083734,-0.479626291,0.04157275,0.395268405,-0.235545226,0.191537052,0.591622268,-0.009908586,0.806597201,0.402023582,0.186132526,-0.099102743,-0.082262273,6.78
"""
st.text_area("Example Inputs (copy these):", example_data,height=160)


# Footer or additional information
st.markdown("<br><br><hr><center>🛡️ Developed for secure transactions detection</center>", unsafe_allow_html=True)