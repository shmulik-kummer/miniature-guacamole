from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)

def setup_logging():
    """Configure comprehensive logging for the Flask application."""
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configure RotatingFileHandler with 10MB max file size and 10 backup files
    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=10
    )
    
    # Set up file log format with detailed information
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Set up console handler with simpler format
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    
    # Configure the Flask app logger
    app.logger.setLevel(logging.DEBUG)  # Allow DEBUG and above
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    
    # Prevent duplicate logs from propagating to the root logger
    app.logger.propagate = False

# Initialize logging
setup_logging()

# Keep the existing calculate_area function as core logic
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width


# Create helath check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the service is running."""
    app.logger.info(f'Health check endpoint accessed from {request.remote_addr}')
    return jsonify({"status": "healthy"}), 200

@app.route('/area', methods=['GET'])
def get_area():
    """GET endpoint that calculates area from length and width query parameters."""
    # Log incoming request
    app.logger.info(f'Request to /area endpoint from {request.remote_addr}')
    app.logger.debug(f'Request arguments: {dict(request.args)}')
    
    # Extract parameters from query string
    length_param = request.args.get('length')
    width_param = request.args.get('width')
    
    # Check 1: Missing parameters
    if length_param is None or width_param is None:
        app.logger.warning(f'Missing parameters - length: {length_param}, width: {width_param}')
        return jsonify({"error": "Both 'length' and 'width' parameters are required."}), 400
    
    try:
        # Convert parameters to numeric type
        length = float(length_param)
        width = float(width_param)
        
        # Check 2: Invalid values (negative or zero)
        if length <= 0 or width <= 0:
            app.logger.warning(f'Invalid values (negative or zero) - length: {length}, width: {width}')
            return jsonify({"error": "Both 'length' and 'width' must be positive numbers."}), 400
        
        # Calculate area using existing function
        area = calculate_area(length, width)
        
        # Log successful calculation
        app.logger.info(f'Successful area calculation - length: {length}, width: {width}, area: {area}')
        
        # Return success response
        return jsonify({
            "length": length,
            "width": width,
            "area": area
        }), 200
        
    except ValueError as e:
        # Check 2: Non-numeric values
        app.logger.error(f'ValueError with invalid input - length_param: {length_param}, width_param: {width_param}')
        return jsonify({"error": "Both 'length' and 'width' must be valid numbers."}), 400
    except Exception as e:
        # Log unexpected exceptions with full stack trace
        app.logger.error(f'Unexpected exception occurred: {str(e)}', exc_info=True)
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.logger.info('Starting Flask application on 0.0.0.0:5000')
    app.run(host='0.0.0.0', debug=True)