from flask import Flask, request, jsonify

app = Flask(__name__)

# Keep the existing calculate_area function as core logic
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


# Create helath check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the service is running."""
    return jsonify({"status": "healthy"}), 200

@app.route('/area', methods=['GET'])
def get_area():
    """GET endpoint that calculates area from length and width query parameters."""
    # Extract parameters from query string
    length_param = request.args.get('length')
    width_param = request.args.get('width')
    
    # Check 1: Missing parameters
    if length_param is None or width_param is None:
        return jsonify({"error": "Both 'length' and 'width' parameters are required."}), 400
    
    try:
        # Convert parameters to numeric type
        length = float(length_param)
        width = float(width_param)
        
        # Check 2: Invalid values (negative or zero)
        if length <= 0 or width <= 0:
            return jsonify({"error": "Both 'length' and 'width' must be positive numbers."}), 400
        
        # Calculate area using existing function
        area = calculate_area(length, width)
        
        # Return success response
        return jsonify({
            "length": length,
            "width": width,
            "area": area
        }), 200
        
    except ValueError:
        # Check 2: Non-numeric values
        return jsonify({"error": "Both 'length' and 'width' must be valid numbers."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)