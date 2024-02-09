from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api/fachinformatiker', methods=['GET'])
def fachinformatiker_endpoint():
    try:
        # Jalankan spider Scrapy
        subprocess.run(['scrapy', 'crawl', 'fachinformatiker'])
        return jsonify({"status": "Scraping completed!"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})

@app.route('/api/systemintegration', methods=['GET'])
def systemintegration_endpoint():
    try:
        # Jalankan spider Scrapy
        subprocess.run(['scrapy', 'crawl', 'systemintegration'])
        return jsonify({"status": "Scraping completed!"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})

@app.route('/api/digitalnetwork', methods=['GET'])
def digitalnetwork_endpoint():
    try:
        # Jalankan spider Scrapy
        subprocess.run(['scrapy', 'crawl', 'digitalnetwork'])
        return jsonify({"status": "Scraping completed!"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})


@app.route('/api/softwaredev', methods=['GET'])
def softwaredev_endpoint():
    try:
        # Jalankan spider Scrapy
        subprocess.run(['scrapy', 'crawl', 'softwaredev'])
        return jsonify({"status": "Scraping completed!"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})


@app.route('/api/data', methods=['GET'])
def data_endpoint():
    try:
        # Jalankan spider Scrapy
        subprocess.run(['scrapy', 'crawl', 'data'])
        return jsonify({"status": "Scraping completed!"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})



if __name__ == '__main__':
    app.run(debug=True)
