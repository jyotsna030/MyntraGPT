from flask import Flask, request, jsonify, send_from_directory, render_template
import pandas as pd

app = Flask(__name__)

def to_lowercase(value):
    if isinstance(value, str):
        return value.lower()
    else:
        return str(value).lower()

@app.route('/')
def index():
    # Serve the HTML file from the templates folder
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    # Serve static files (CSS, JS) from the static folder
    return send_from_directory('static', filename)

@app.route('/get-recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    responses = data['responses']

    # Convert responses to lowercase
    occasion = to_lowercase(responses[1])
    size = to_lowercase(responses[2][0]) if isinstance(responses[2], list) and len(responses[2]) > 0 else ''
    BodyType = to_lowercase(responses[3][0]) if isinstance(responses[3], list) and len(responses[3]) > 0 else ''
    preference = to_lowercase(responses[4][0]) if isinstance(responses[4], list) and len(responses[4]) > 0 else ''
    price = to_lowercase(responses[5][0]) if isinstance(responses[5], list) and len(responses[5]) > 0 else ''

    # Read the dataset
    df = pd.read_excel('F:/MyntraGPT/Chatbot/myntra correct data.xlsx')

    # Adding columns for sizes
    df['is_S'] = df['size'].apply(lambda x: 'S' in x.split(','))
    df['is_M'] = df['size'].apply(lambda x: 'M' in x.split(','))
    df['is_L'] = df['size'].apply(lambda x: 'L' in x.split(','))

    # Adding columns for body types
    df['is_apple'] = df['BodyType'].apply(lambda x: 'apple' in x.split(','))
    df['is_pear'] = df['BodyType'].apply(lambda x: 'pear' in x.split(','))
    df['is_hourglass'] = df['BodyType'].apply(lambda x: 'hourglass' in x.split(','))
    df['is_rectangle'] = df['BodyType'].apply(lambda x: 'rectangle' in x.split(','))

    # Apply the filtering based on the user-defined criteria
    filtered_df = df

    if occasion == 'traditional':
        if size == 'S':
            filtered_df = df[df['is_S']]
            
            if BodyType == 'apple':
                filtered_df = filtered_df[filtered_df['is_apple']]
                
                if preference == 'light':
                    filtered_df = filtered_df[filtered_df['preference'] == 'light']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]
                
                elif preference == 'dark':
                    filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

        elif size == 'M':
            filtered_df = df[df['is_M']]
            
            if BodyType == 'apple':
                filtered_df = filtered_df[filtered_df['is_apple']]
                
                if preference == 'light':
                    filtered_df = filtered_df[filtered_df['preference'] == 'light']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

                elif preference == 'dark':
                    filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

        elif size == 'L':
            filtered_df = df[df['is_L']]
            
            if BodyType == 'apple':
                filtered_df = filtered_df[filtered_df['is_apple']]
                
                if preference == 'light':
                    filtered_df = filtered_df[filtered_df['preference'] == 'light']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

                elif preference == 'dark':
                    filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

    elif occasion == 'western':
        if size == 'S':
            filtered_df = df[df['is_S']]
            
            if BodyType == 'apple':
                filtered_df = filtered_df[filtered_df['is_apple']]
                
                if preference == 'light':
                    filtered_df = filtered_df[filtered_df['preference'] == 'light']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]
                
                elif preference == 'dark':
                    filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

        elif size == 'M':
            filtered_df = df[df['is_M']]
            
            if BodyType == 'apple':
                filtered_df = filtered_df[filtered_df['is_apple']]
                
                if preference == 'light':
                    filtered_df = filtered_df[filtered_df['preference'] == 'light']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

                elif preference == 'dark':
                    filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

        elif size == 'L':
            filtered_df = df[df['is_L']]
            
            if BodyType == 'apple':
                filtered_df = filtered_df[filtered_df['is_apple']]
                
                if preference == 'light':
                    filtered_df = filtered_df[filtered_df['preference'] == 'light']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

                elif preference == 'dark':
                    filtered_df = filtered_df[filtered_df['preference'] == 'dark']
                    
                    if price == 'below_2300':
                        filtered_df = filtered_df[filtered_df['price'] < 2300]
                    elif price == 'below_900':
                        filtered_df = filtered_df[filtered_df['price'] < 900]
                    elif price == 'below_1500':
                        filtered_df = filtered_df[filtered_df['price'] < 1500]
                    elif price == 'below_5000':
                        filtered_df = filtered_df[filtered_df['price'] < 5000]

    # Print the product details (links and image URLs) for the filtered results
    products = filtered_df[['Link', 'Imagelink']].to_dict('records')

    if products:
        return jsonify({'products': products})
    else:
        return jsonify({'products': []})

if __name__ == '__main__':
    app.run(debug=True)
