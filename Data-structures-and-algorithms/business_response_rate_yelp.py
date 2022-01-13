def business_responsiveness_rate(biz_owner_id, all_messages):

    received_messages = {(
                    message['sender'], 
                    message['recipient'], 
                    message['conversation_id']
                ) 
                for message in all_messages if message['recipient'] == biz_owner_id
            }
    responded_messages = {(
                    message['sender'], 
                    message['recipient'], 
                    message['conversation_id']
                )
                for message in all_messages if message['sender'] == biz_owner_id
            }

    response_rate = int(len(responded_messages)/len(received_messages) * 100)
    
    return response_rate

biz_owner_id = 42
all_messages = [
            {"sender": 1,  "recipient": 42, "conversation_id": 1},
            {"sender": 42, "recipient": 1,  "conversation_id": 1},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 3,  "recipient": 88, "conversation_id": 3},
            {"sender": 3,  "recipient": 42, "conversation_id": 4},
        ]

print(business_responsiveness_rate(biz_owner_id, all_messages))
