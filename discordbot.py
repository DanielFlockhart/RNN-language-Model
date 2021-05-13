import discord
import os
import predict_words as rnn
import generate_voice as voice_gen
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing
from discord.ext import commands
import numpy as np
import time
    
client = discord.Client()
model = tf.saved_model.load('one_step')
states = None
chars = 100
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="Destroying Humanity"))

@client.event
async def on_message(message):
    global chars
    if message.content.startswith('chars'):
        chars = int(message.content.split("chars",1)[1])
        out = f'Character length set to : {chars}'
        await message.channel.send(out)
        
    if message.content.startswith('chat'):
        print(message.content)
        seed = message.content.split("chat",1)[1]
        print(seed)
        next_char = tf.constant([seed])
        result = [next_char]
        await message.channel.send(rnn.get_sentance(chars,seed,model,states,next_char,result))

    if message.content == "join":
        channel = message.author.voice.channel
        voice_gen.save_sound("Hello there - i have now joined the Voice call")
        channel = await channel.connect()
client.run('ODA2OTkxNjcxNTgwODE5NDY2.YBxfjw.GiHYSA_ILKHY2ohUCtn04ycCh2I')
