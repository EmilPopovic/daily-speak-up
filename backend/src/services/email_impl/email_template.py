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

def welcome_message():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Email</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            padding: 20px;
        }

        .email-container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .header {
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            padding: 40px 30px;
            text-align: center;
        }

        .logo-space {
            width: 180px;
            height: 60px;
            margin: 0 auto;
            background-color: rgba(255, 255, 255, 0.1);
            border: 2px dashed rgba(255, 255, 255, 0.3);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: rgba(255, 255, 255, 0.5);
            font-size: 12px;
            margin-bottom: 20px;
        }

        .header h1 {
            color: #ffffff;
            font-size: 28px;
            font-weight: 600;
            margin: 0;
        }

        .content {
            padding: 40px 30px;
            color: #1f2937;
        }

        .greeting {
            font-size: 20px;
            color: #1e40af;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .message {
            font-size: 16px;
            line-height: 1.6;
            color: #4b5563;
            margin-bottom: 20px;
        }

        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
            color: #ffffff;
            text-decoration: none;
            padding: 14px 32px;
            border-radius: 6px;
            font-weight: 600;
            margin: 20px 0;
            transition: transform 0.2s;
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
        }

        .features {
            background-color: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 20px;
            margin: 30px 0;
            border-radius: 4px;
        }

        .features h3 {
            color: #1e40af;
            font-size: 18px;
            margin-bottom: 12px;
        }

        .features ul {
            list-style: none;
            padding: 0;
        }

        .features li {
            padding: 8px 0;
            color: #4b5563;
            position: relative;
            padding-left: 25px;
        }

        .features li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #3b82f6;
            font-weight: bold;
        }

        .footer {
            background-color: #1e3a8a;
            padding: 30px;
            text-align: center;
            color: #bfdbfe;
            font-size: 14px;
        }

        .footer a {
            color: #93c5fd;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        .social-links {
            margin-top: 20px;
        }

        .social-links a {
            display: inline-block;
            margin: 0 10px;
            color: #93c5fd;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header with Logo Space -->
        <div class="header">
            <img width="100px"src="https://i.ibb.co/TBhqZTrW/DSU.png" alt="DailySpeakUp Logo">
            <h1>Welcome Aboard!</h1>
        </div>

        <!-- Main Content -->
        <div class="content">
            <p class="greeting">Hi there,</p>
            
            <p class="message">
                We're thrilled to have you join our community! Thank you for signing up and taking the first step towards an amazing journey with us.
            </p>

            <p class="message">
                Your account has been successfully created, and you're now ready to explore everything we have to offer.
            </p>

            <center>
                <a href="http://test.dailyspeak.app" class="cta-button">Get Started</a>
            </center>

            <div class="features">
                <h3>What's Next?</h3>
                <ul>
                    <li>Complete your profile to personalize your experience</li>
                    <li>Explore our features and discover what's possible</li>
                    <li>Connect with our community and start engaging</li>
                    <li>Start improving your rhetoric skills</li>
                </ul>
            </div>

            <p class="message">
                If you have any questions or need assistance, our support team is always here to help. Simply reply to this email or visit our help center.
            </p>

            <p class="message">
                Welcome to the family!<br>
                <strong style="color: #1e40af;">The DailySpeakUp Team</strong>
            </p>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p>© 2025 DailySpeakUp. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
    """