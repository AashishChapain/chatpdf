css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,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">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''