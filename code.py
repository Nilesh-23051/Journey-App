# from flask import Flask, request
# import json
# import datetime

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.get_json()

#     if data:
#         # Log event for debugging
#         with open("webhook_log.txt", "a") as f:
#             f.write(f"\n\n--- Event at {datetime.datetime.now()} ---\n")
#             json.dump(data, f, indent=2)
        
#         # Print summary to terminal
#         repo_name = data.get("repository", {}).get("full_name")
#         pusher = data.get("pusher", {}).get("name")
#         commit_msg = data.get("head_commit", {}).get("message")
#         print(f"[{repo_name}] Change pushed by {pusher}: {commit_msg}")
        
#         # You can plug in email/Slack/Discord notifications here
        
#         return "Webhook received", 200
#     else:
#         return "No data", 400

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event')

    if event_type:
        # Log event type with timestamp
        with open("webhook_log.txt", "a") as f:
            f.write(f"\n\n--- {event_type.upper()} event at {datetime.datetime.now()} ---\n")

        # Print event type to terminal
        print(f"Received GitHub event: {event_type}")

        return "Event received", 200
    else:
        return "No event type", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
