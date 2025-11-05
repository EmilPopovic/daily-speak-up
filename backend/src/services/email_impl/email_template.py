def place_holder():
    return "REPLACE_THIS_WITH_MESSAGE"

def basic_html_message():
    return """
        <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DailySpeakUp Notification</title>
<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #e6f0ff;
        margin: 0;
        padding: 0;
        color: #333333;
    }

    .email-container {
        max-width: 600px;
        margin: 40px auto;
        background: #f0f8ff;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid #d9e6ff;
    }

    .header {
        background: linear-gradient(135deg, #4facfe, #00f2fe);
        padding: 20px;
        text-align: center;
        color: #fff;
    }

    .header img {
        max-width: 80px;
        margin-bottom: 10px;
    }

    .header h1 {
        font-size: 24px;
        margin: 0;
    }

    .body {
        padding: 30px 20px;
        text-align: center;
    }

    .body p {
        font-size: 16px;
        line-height: 1.6;
        color: #1a1a1a;
    }

    .motivational {
        margin-top: 20px;
        font-style: italic;
        font-weight: bold;
        color: #0050b3;
        font-size: 18px;
    }

    .footer {
        background-color: #e6f0ff;
        text-align: center;
        font-size: 12px;
        color: #555555;
        padding: 15px 20px;
    }
</style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <!-- Logo placeholder -->
            <img src="https://i.ibb.co/TBhqZTrW/DSU.png" alt="DailySpeakUp Logo">
            <h1>DailySpeakUp Notification</h1>
        </div>
        <div class="body">
            <p>Hello there, we have a message for you!</p>
            <p>REPLACE_THIS_WITH_MESSAGE</p>
            <p class="motivational">"Speaking up sharpens your voice and hones your rhetorical skills."</p>
        </div>
        <div class="footer">
            &copy; 2025 DailySpeakUp. All rights reserved.
        </div>
    </div>
</body>
</html>

"""