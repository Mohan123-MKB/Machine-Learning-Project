# 🚖 Uber Rides Prediction Web App  

A simple Machine Learning web application built with **Flask** that predicts the **number of weekly Uber rides** based on input features.  

---

## 📌 Features
- Web interface with **form inputs** (Price per Week, Population, Monthly Income, Average Parking per Month).  
- Machine Learning model trained using **scikit-learn**.  
- Prediction displayed directly on the web page.  

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)  
- **Frontend**: HTML + CSS  
- **ML Libraries**: scikit-learn, NumPy, Pandas  
- **Serialization**: Pickle  

---

## 📂 Project Structure
Uber-Rides-Prediction/
│── static/ # CSS files
│── templates/ # HTML templates (index.html)
│── model.pkl # Trained ML model
│── app.py # Flask app
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── taxi.csv # Dataset 
|__ MLMODEL.ipynb # Model Building



----------------------------------------

---

## 🚀 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/uber-rides-prediction.git
   cd uber-rides-prediction
2. **Create a virtual environment**
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
3. **Install dependencies**
pip install -r requirements.txt
4. **Run the Flask app**
python app.py
5. **Open in browser**
#http://127.0.0.1:5000/predict


------------------------------
🎯 Usage

1) Enter values for:
      Price per Week
      Population
      Monthly Income
      Average Parking per Month
2) Click Predict Results.
3) The app will display the predicted number of rides per week.

------------------------
Input:

Price per Week: 200
Population: 5000
Monthly Income: 30000
Average Parking per Month: 50

Output:

Number of weekly rides: 245

