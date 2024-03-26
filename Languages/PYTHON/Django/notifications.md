---
title: Python - Django Notifications
tags: studies, programação, notifications, python, django, channels, websocket, sse
use: Documentation
languages: Python
dependences: Django, Channels, Redis
---

<details> <summary>Table of Contents 🔖</summary>

- [Using Channels for Real-Time Notifications](#using-channels-for-real-time-notifications)
    - [Retrieving the notifications from the database](#retrieving-the-notifications-from-the-database)
  - [Sometimes the handshake don't make the connection](#sometimes-the-handshake-dont-make-the-connection)
  - [Sending specific notification per user](#sending-specific-notification-per-user)
    - [Create a mapping for the user sessions](#create-a-mapping-for-the-user-sessions)
    - [Without mapping](#without-mapping)
- [Using Server-Sent Events (SSE) for Notifications](#using-server-sent-events-sse-for-notifications)
- [Other REFERENCES](#other-references)

</details>

---

# Using Channels for Real-Time Notifications
-   `pip install channels`
-   redis
    -   ```shell
            sudo apt install lsb-release curl gpg
            curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
            echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee 
            /etc/apt/sources.list.d/redis.list
            sudo apt-get update
            sudo apt-get install redis```
        ```
        
    -   `pip install channels_redis~=3.3`
___

### Retrieving the notifications from the database

there's two possibilities to do that:

-   creating a custom `context_processors` inside of `setup.settings.TEMPLATES` this means that in every rendering django will load the queries automatically inside of the template (NOTE: this can be a litthe overkill and request a lot of memory depending on the queries)
-   calling using AJAX or HTMX to reetrieve only on a specific request

both of the methods above can be called async in order to reduce the page loading
___

## Sometimes the handshake don't make the connection

so i've setted a timeout to call the connection again

```js
event_socket.js:3 WebSocket connection to 'ws://127.0.0.1:8000/ws/event/broadcast/' failed: Connection closed before receiving a handshake response
createWebSocket @ event_socket.js:3
initializeWebSocket @ event_socket.js:64
(anonymous) @ event_socket.js:81
event_socket.js:50 Chat socket closed unexpectedly: CloseEvent
handleSocketClosure @ event_socket.js:50
eventNotificationSocket.onclose @ event_socket.js:72
event_socket.js:51 Reconnecting one more time...
```

```bash
WebSocket HANDSHAKING /ws/event/broadcast/ [127.0.0.1:52808]
HTTP GET /static/debug_toolbar/css/print.css 200 [0.00, 127.0.0.1:58846]
WebSocket DISCONNECT /ws/event/broadcast/ [127.0.0.1:52808]
HTTP GET /static/debug_toolbar/js/utils.js 200 [5.58, 127.0.0.1:58846]
HTTP GET /static/images/logo_byon_v3d.ico 200 [0.00, 127.0.0.1:58846]
WebSocket HANDSHAKING /ws/event/broadcast/ [127.0.0.1:57064]
WebSocket CONNECT /ws/event/broadcast/ [127.0.0.1:57064]
```
I was unsing a timespan of 3sec but somehow the past connection wasn't closed properlly before oppening a new one, so its now 5sec, and as shown above it looks good
___

## Sending specific notification per user

### Create a mapping for the user sessions
Yes, it's possible to send custom notifications to specific users without broadcasting to a group. You can achieve this by using a one-to-one communication approach between the server and each individual client. Here's a basic outline of how you can implement this:

Maintain a mapping of user IDs to WebSocket channels: When a user connects to the WebSocket server, store their WebSocket channel ID along with their user ID. This mapping allows the server to target specific users when sending notifications.

Send notifications directly to specific users: When you need to send a notification to a specific user, look up their WebSocket channel ID using their user ID from the mapping and send the notification directly to that channel.

Here's a simplified example of how you could implement this:
```python
# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            await self.accept()
            # Store the user's WebSocket channel ID along with their user ID
            await self.register_user_channel()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Remove the user's WebSocket channel ID from storage
        await self.unregister_user_channel()

    async def receive(self, text_data):
        data = json.loads(text_data)
        recipient_user_id = data.get('recipient_user_id')
        message = data.get('message')

        if recipient_user_id and message:
            await self.send_notification_to_user(recipient_user_id, message)

    @database_sync_to_async
    def register_user_channel(self):
        # Store the user's WebSocket channel ID along with their user ID
        UserChannel.objects.create(user=self.user, channel_name=self.channel_name)

    @database_sync_to_async
    def unregister_user_channel(self):
        # Remove the user's WebSocket channel ID from storage
        UserChannel.objects.filter(user=self.user, channel_name=self.channel_name).delete()

    async def send_notification_to_user(self, recipient_user_id, message):
        # Lookup the recipient's WebSocket channel ID using their user ID
        recipient_channel_name = await self.get_recipient_channel_name(recipient_user_id)
        if recipient_channel_name:
            # Send the notification directly to the recipient's channel
            await self.channel_layer.send(recipient_channel_name, {
                'type': 'send.notification',
                'message': message,
            })

    @database_sync_to_async
    def get_recipient_channel_name(self, recipient_user_id):
        # Lookup the recipient's WebSocket channel ID using their user ID
        try:
            user_channel = UserChannel.objects.get(user_id=recipient_user_id)
            return user_channel.channel_name
        except UserChannel.DoesNotExist:
            return None
```
In this example:

When a user connects to the WebSocket server, their user ID and WebSocket channel ID are stored in a database table called UserChannel.
When the server receives a message with a recipient user ID and a notification message, it looks up the recipient's WebSocket channel ID using their user ID from the UserChannel table.
If the recipient's channel ID is found, the server sends the notification directly to that channel.
You would need to implement the UserChannel model to store the mapping between user IDs and WebSocket channel IDs. This model should have fields for the user ID (user) and the WebSocket channel ID (channel_name).

### Without mapping
Yes, exactly! Each user could have their own unique room to which you send custom notifications. This approach allows you to send notifications specifically to individual users without broadcasting to a group.

Here's how you can achieve this:

When a user logs in or connects to the WebSocket, you create a unique room for that user.
When you need to send a notification to a specific user, you send it to their corresponding room.
Let's modify the consumer to create a unique room for each user:
```python
# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            self.room_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle received messages (e.g., subscribe/unsubscribe)
        pass

    async def send_notification(self, event):
        # Send notification to the WebSocket
        notification = event['notification']
        await self.send(text_data=json.dumps({
            'notification': notification
        }))
```
Now, when you want to send a notification to a specific user, you can send it to their unique room (user_<user_id>). You can trigger this notification from other parts of your application whenever necessary, such as when a new message is received or when a certain event occurs.

For example, in a Django view or in another consumer, you would trigger the notification like this:
```python
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def send_notification_to_user(user_id, notification):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {
            'type': 'send_notification',
            'notification': notification
        }
    )
```
This approach allows you to send custom notifications to specific users without broadcasting to a group. Each user effectively has their own private room to receive notifications.

---

# Using Server-Sent Events (SSE) for Notifications

> when using server-sent events, sending the header["Content-type"] "text/event-stream" how secure is this information (considering a Django server envirorment)

When using Server-Sent Events (SSE) in a Django server environment and sending the header `"Content-Type: text/event-stream"`, the security of this information largely depends on the context of your application and how you handle sensitive data.

1. **Data in Transit**: The header `"Content-Type: text/event-stream"` itself doesn't pose a significant security risk, as it merely indicates to the client how to interpret the response data. However, it's crucial to ensure that your SSE connection is established over HTTPS rather than HTTP. HTTPS encrypts the data transmitted between the server and the client, reducing the risk of interception or tampering.

2. **Sensitive Information**: Be cautious about the data you transmit via SSE. While the content of the SSE messages themselves is not inherently secure or insecure, you should avoid sending sensitive information directly in SSE messages if possible. For example, avoid sending plaintext passwords, session tokens, or other sensitive data. If you must send sensitive data, consider encrypting it before transmission.

3. **Authentication and Authorization**: Ensure that your SSE endpoints are properly authenticated and authorized. Only authenticated users should be allowed to establish SSE connections, and you should enforce appropriate access controls to prevent unauthorized access to sensitive resources.

4. **Cross-Origin Resource Sharing (CORS)**: Consider implementing CORS policies to restrict access to your SSE endpoints from unauthorized domains. This helps prevent cross-site scripting (XSS) attacks and other security vulnerabilities.

5. **Input Validation and Sanitization**: As with any web application, input validation and sanitization are essential for preventing injection attacks and other security vulnerabilities. Ensure that you validate and sanitize any user input before including it in SSE messages to prevent XSS, SQL injection, and other attacks.

6. **Django Security Best Practices**: Follow Django's security best practices, including keeping your Django version up-to-date, using secure authentication mechanisms, implementing CSRF protection, and enabling security features such as Content Security Policy (CSP) to mitigate common web application security risks.

By following these best practices and considering the security implications of using SSE in your Django application, you can help ensure that your SSE implementation is as secure as possible. Additionally, regularly reviewing and updating your security measures is essential to adapt to evolving threats and vulnerabilities.

___

# Other REFERENCES

- https://www.youtube.com/watch?v=DqCqFRYO4W8
- https://www.youtube.com/watch?v=sthCUcw5Zog&t
- https://www.youtube.com/watch?v=FcVwDEcu6K0

- https://www.youtube.com/watch?v=4HlNv1qpZFY
- https://www.youtube.com/watch?v=MziqE_2Euss
- 