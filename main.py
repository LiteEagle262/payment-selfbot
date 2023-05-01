import discord #discord.py-self liberary USES SAME NAMESPACE
import tkinter as tk
import json,traceback
from tkinter import messagebox
from discord.ext import commands

#--load config--#
with open('config.json', 'r') as f:
    config_data = json.load(f)
    token = config_data['token']
    prefix = config_data['prefix']
    paypal = config_data['paypal']
    cashapp = config_data['cashapp']
    btc = config_data['btc']
    ltc = config_data['ltc']
    xmr = config_data['xmr']
    doge = config_data['doge']
    eth = config_data['eth']

client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)

@client.command(name="pay")
async def pay(ctx, method=None):
    if method == None:
        await ctx.send(f"Paypal: {paypal}\nCashapp: {cashapp}\nBTC: {btc}\nLTC: {ltc}\nXMR: {xmr}\nDOGE: {doge}\nETH: {eth}")
    elif method.lower() == "paypal":
        await ctx.send(paypal)
        await ctx.message.delete()
    elif method.lower() == "cashapp":
        await ctx.send(cashapp)
        await ctx.message.delete()
    elif method.lower() == "btc" or method.lower() == "bitcoin":
        await ctx.send(btc)
        await ctx.message.delete()
    elif method.lower() == "ltc" or method.lower() == "litecoin":
        await ctx.send(ltc)
        await ctx.message.delete()
    elif method.lower() == "xmr" or method.lower() == "monero":
        await ctx.send(xmr)
        await ctx.message.delete()
    elif method.lower() == "doge" or method.lower() == "dogecoin":
        await ctx.send(doge)
        await ctx.message.delete()
    elif method.lower() == "eth" or method.lower() == "ethereum":
        await ctx.send(eth)
        await ctx.message.delete()
    else:
        await ctx.send("Invalid Method Selected")
        await ctx.message.delete()
        
root = tk.Tk()
root.withdraw()
messagebox.showinfo(title="Selfbot Running", message="The Selfbot is now running!\n\nmade by liteeagle.me")

@client.event
async def on_error(event, *args, **kwargs):
    messagebox.showerror(title="Error", message="An error has occurred please restart if this doesnt go away.\n\nError: " + traceback.format_exc())
    traceback.print_exc()
   
client.run(token)
