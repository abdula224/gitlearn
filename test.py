from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd

app = Flask(__name__)
# Load the trained model and other data

car_data = pd.read_csv('car_upto.csv')  # Load your training data for dropdowns
# Load models
lr_model = pickle.load(open("lr_model.pkl", "rb"))
rf_model = pickle.load(open("rf_model.pkl", "rb"))
xgb_model = pickle.load(open("xgb_model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

companies = sorted(car_data['company'].unique())
car_models_dict = car_data.groupby('company')['name'].apply(list).to_dict()
years = sorted(car_data['year'].unique(), reverse=True)
fuel_types = car_data['fuel_type'].unique()
@app.route('/')
def index():
    return render_template('index.html',companies=companies,fuel_type=fuel_types,
                           years=years)
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


    
@app.route('/compare_models', methods=['POST'])
def compare_models():
    data = request.get_json()
    company = data['company']
    model = data['car_model']
    year = int(data['year'])
    fuel_type = data['fuel_type']
    kms_driven = int(data['kilo_drives'])

    input_df = pd.DataFrame([[model, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=features, fill_value=0)

    predictions = {
     'Linear Regression': float(round(lr_model.predict(input_encoded)[0], 2)),
    'Random Forest': float(round(rf_model.predict(input_encoded)[0], 2)),
    'XGBoost': float(round(xgb_model.predict(input_encoded)[0], 2))
    }

    return jsonify(predictions)

@app.route('/get_price_chart_data')
def get_price_chart_data():
    # We'll use RF model here, but you can change to lr_model or xgb_model
    temp_df = car_data.copy()
    
    # Predict prices using the selected model
    try:
        temp_df['predicted_price'] = rf_model.predict(temp_df[features])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Compute average predicted price for top 10 models
    top_models = temp_df.groupby('name')['predicted_price'].mean().sort_values(ascending=False).head(10)
    
    labels = top_models.index.tolist()
    values = top_models.values.tolist()
    return jsonify({'labels': labels, 'values': values})


@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/get_models', methods=['POST'])
def get_models():
    data = request.get_json()
    company = data['company']
    models = sorted(list(set(car_models_dict.get(company, []))))
    return jsonify(models)
@app.route('/predict', methods=['POST'])
def predict():
    company = request.form['company']
    model = request.form['car_model']
    year = int(request.form['year'])
    fuel_type = request.form['fuel_type']
    kms_driven = int(request.form['kilo_drives'])
    ml_model = request.form['ml_model']

    # Create raw input dataframe
    input_df = pd.DataFrame([[model, company, year, kms_driven, fuel_type]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    # One-hot encode like during training
    input_encoded = pd.get_dummies(input_df)
    
    # Align with feature columns used during training
    input_encoded = input_encoded.reindex(columns=features, fill_value=0)

    # Choose the ML model
    if ml_model == "lr":
        pred = lr_model.predict(input_encoded)[0]
    elif ml_model == "rf":
        pred = rf_model.predict(input_encoded)[0]
    elif ml_model == "xgboost":
        pred = xgb_model.predict(input_encoded)[0]
    else:
        return "Invalid model selected", 400
    return f"💰 Estimated Car Price: ₹{round(pred,2)} lakhs"


if __name__ == '__main__':
    app.run(debug=True)
